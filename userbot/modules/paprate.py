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

from userbot import CMD_HELP, bot
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.pap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE3NDI2OTE0Mzg5ODA4OA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIxNDMzMTAxNjA1ODU2OA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIxMTMyNjM3NTY0NjUzMg=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIxMDMyNDgyODg0MjUyMA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIwNzMyMDE4ODQzMDQ4NA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIwNjMxODY0MTYyNjQ3Mg=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIwNTMxNzA5NDgyMjQ2MA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIwNDMxNTU0ODAxODQ0OA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTIwMjMxMjQ1NDQxMDQyNA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5OTMwNzgxMzk5ODM4OA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5NzMwNDcyMDM5MDM2NA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5NTMwMTYyNjc4MjM0MA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5MzI5ODUzMzE3NDMxNg=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5MjI5Njk4NjM3MDMwNA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE5MDI5Mzg5Mjc2MjI4MA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE4OTI5MjM0NTk1ODI2OA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE4NzI4OTI1MjM1MDI0NA=="
    chat = "https://t.me/fybpap_bot?start=Z2V0LTE4ODI5MDc5OTE1NDI1Ng=="
    await event.edit("```Pencarian Pap```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Buka blokir @fybpap_bot dan coba lagi, atau join dahulu ke Channel @ratefyb```")
            return
        if response.text.startswith(
                "**Maaf saya tidak bisa mendapatkan pap dari**"):
            await event.edit("```Saya pikir ini Anda harus join Channel dahulu ke @ratefyb```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "paprate":
    "????????????????????????????: `.pap` <link/code> \
\nPenggunaan: lihat adult pap. Kek"})
