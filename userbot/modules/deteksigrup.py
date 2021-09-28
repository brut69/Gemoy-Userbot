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

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.(?:dgrup|dg)\s?(.*)?")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not event.reply_to_msg_id:
        await event.edit("```Mohon Balas Ke Pesan Pengguna atau ketik .dgrup (ID/Username) Yang mau Anda deteksi```")
        return
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit.event("`Mohon Berikan ID/Username untuk menemukan Riwayat`"
                                 )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    event = await event.edit("`Sedang Mendeteksi...`")
    async with bot.conversation(chat) as conv:
        try:
            await conv.send_message(f"{uid}")
        except YouBlockedUserError:
            await steal.reply(
                "```Mohon Unblock @tgscanrobot Dan Coba Lagi```"
            )
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.edit(response.text)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CMD_HELP.update({
    "deteksirup":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.dgrup` or `.dg`\
    \nPenggunaan: Melihat Riwayat Grup Yang Pernah / Sedang dimasuki."
})
