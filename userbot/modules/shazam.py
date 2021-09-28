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


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.shazam(?: |$)(.*)")
async def _(event):
    "Untuk membalikkan pencarian musik dengan bot."
    if not event.reply_to_msg_id:
        return await event.edit("```Membalas pesan audio.```")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("```Mengidentifikasi lagu```")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio diterima"):
                    return await event.edit(
                        "Terjadi kesalahan saat mengidentifikasi lagu. Coba gunakan pesan audio berdurasi 5-10 detik."
                    )
                await event.edit("```Tunggu sebentar...```")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**Judul : **{result.text.splitlines()[0]}\
        \n\n**Details : **__{result.text.splitlines()[2]}__"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id, [start_msg.id, send_audio.id, check.id, result.id, response.id]
            )
    except TimeoutError:
        return await event.edit("`Error: `@auddbot` tidak merespons, coba lagi nanti")

CMD_HELP.update(
    {
        "shazam": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shazam <membalas suara/audio>"
        "\nPenggunaan: Membalikkan file audio pencarian menggunakan (@auddbot)"
    }
)
