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


from telethon.errors import ChatSendInlineForbiddenError, ChatSendStickersForbiddenError
from userbot.events import register
from userbot import CMD_HELP, bot


@register(outgoing=True, pattern=r"^\.frog (.*)")
async def honkasays(event):
    await event.edit("`Sedang Memproses, Mohon Tunggu Sebentar...`")
    text = event.pattern_match.group(1)
    if not text:
        return await event.edit("Beri Aku Bebeberapa Text, Contoh : `.honka space <text>`")
    try:
        if not text.endswith("."):
            text = text + "."
        if len(text) <= 9:
            results = await bot.inline_query("honka_says_bot", text)
            await results[2].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        elif len(text) >= 14:
            results = await bot.inline_query("honka_says_bot", text)
            await results[0].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        else:
            results = await bot.inline_query("honka_says_bot", text)
            await results[1].click(
                event.chat_id,
                silent=True,
                hide_via=True,
            )
        await event.delete()
    except ChatSendInlineForbiddenError:
        await event.edit("`Mohon Maaf, Saya Tidak Bisa Menggunakan Hal-Hal Sebaris Disini.`")
    except ChatSendStickersForbiddenError:
        await event.edit("Mohon Maaf, Tidak Bisa Mengirim Sticker Disini.")


CMD_HELP.update(
    {
        "honkasay": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.frog` space <text>\
    \nPenggunaan: Menampilkan Pesan <text> di Sticker Animasi."
    }
)
