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


@register(outgoing=True, pattern=r"^\.hentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    await event.edit("```Pengolahan```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Buka blokir @nHentaiBot dan coba lagi```")
            return
        if response.text.startswith(
                "**Maaf saya tidak bisa mendapatkan manga dari **"):
            await event.edit("```Saya pikir ini bukan tautan yang benar```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "hemtai":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.hentai` <link/code> \
\nPenggunaan: lihat nhentai di telegra.ph XD"})
