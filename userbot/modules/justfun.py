# Based Plugins
# Ported For Lord-Userbot By liualvinas/Alvin
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini!!!
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


from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@register(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Ported For Lord-Userbot By liualvinas/Alvin


CMD_HELP.update(
    {
        "justfun": "𝙋𝙡𝙪𝙜𝙞𝙣: `justfun`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.xogame`\
        \nPenggunaan: Game xo-game bot\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mod` <nama app>\
        \nPenggunaan: Dapatkan applikasi mod\
    "
    }
)


CMD_HELP.update(
    {
        "secretchat": "𝙋𝙡𝙪𝙜𝙞𝙣: `secretchat`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.wp` <teks> <username/id>\
        \nPenggunaan: Memberikan pesan rahasia haya orang yang di tag yang bisa melihat\
        \n**Contoh**: `.wp` aku sayang kamu\
    "
    }
)
