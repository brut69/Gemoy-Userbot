# Ported by Aidil Aryanto
#
# Gemoy-Userbot (Telegram Userbot Project )
# Copyright (C) 2021 @dunottagme

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot.events import register
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY, CMD_HELP


@register(outgoing=True, pattern=r'^\.spotnow(:? |$)(.*)?')
async def _(event):
    if event.fwd_from:
        return
    chat = "@SpotifyNowBot"
    now = f"/now"
    await event.edit("`Pengolahan...`")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(now)
            response = await conv.get_response()
            """ - jangan spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("`Silakan buka blokir` @SpotifyNowBot`...`")
            return
        if response.text.startswith("kamu adalah"):
            await event.edit("`Anda tidak mendengarkan apa pun di Spotify saat ini`")
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
            return
        if response.text.startswith("Iklan."):
            await event.edit("`Anda sedang mendengarkan iklan yang mengganggu itu.`")
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
            return
        else:
            downloaded_file_name = await event.client.download_media(
                response.media,
                TEMP_DOWNLOAD_DIRECTORY
            )
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
            )
            """ - pembersihan obrolan setelah selesai - """
            await event.client.delete_messages(conv.chat_id,
                                               [msg.id, response.id])
    await event.delete()
    return os.remove(downloaded_file_name)


CMD_HELP.update({
    "spotify": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.spotnow`"
    "\nPenggunaan: Tunjukkan apa yang Anda dengarkan di spotify."
    "\n@SpotifyNowBot"
})
