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


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern=r"^\.getid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Reply Ke Pesan`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Mohon Balas Ke Reply```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Mohon Reply Ke Pesan`")
        return
    await event.edit("`Mencari ID.......`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bot Sedang Error`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Mohon Maaf, Orang Ini Tidak Mempunyai ID`")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update({
    "getid":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getid`"
    "\nPenggunaan: Balas Ke Pesan Pengguna Untuk Mendapatkan ID Nya."
})
