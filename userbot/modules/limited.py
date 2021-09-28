# Credits By @VckyouuBitch From Geez - Project
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

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Memeriksa Apakah Anda Terbatas...`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Bos! Silakan Buka Blokir @SpamBot`")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update({"limit": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.limit`"
                 "\nPenggunaan: ngecek akun limit"})
