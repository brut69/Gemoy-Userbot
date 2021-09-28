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


from userbot.events import register
from userbot import CMD_HELP, bot

#
# Port By @VckyouuBitch From GeezProject
#
@register(outgoing=True, pattern=r"^\.tmsg (.*)")
async def _(event):
    k = await event.get_reply_message()
    if k:
        a = await bot.get_messages(event.chat_id, 0, from_user=k.sender_id)
        return await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")
    u = event.pattern_match.group(1)
    if not u:
        u = "me"
    a = await bot.get_messages(event.chat_id, 0, from_user=u)
    await event.edit(f"Total Message Dari {u}. Total Chats `{a.total}`")

CMD_HELP.update(
    {
        "totalmsg": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tmsg` | `.tmsg` <username>\
    \nPenggunaan: Mengembalikan jumlah pesan total pengguna dalam obrolan saat ini."
    }
)
