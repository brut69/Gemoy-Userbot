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

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


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


@register(outgoing=True, pattern=r"^\.tetris(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@brugamebot"
    tetris = "tetris"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, tetris)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.puzzle(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@brugamebot"
    bubble = "bubble"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, bubble)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.gmbot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@gamebot"
    corsairs = "corsairs"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, corsairs)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.glbot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@gamebot"
    lumberjack = "lumberjack"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, lumberjack)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.whisp(?: |$)(.*)")
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


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    async with bot.conversation("@truthordaresbot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/truth')
            response = await response
        except YouBlockedUserError:
            await event.reply("```un-Block @truthordaresbot ploxx```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    async with bot.conversation("@truthordaresbot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/dare')
            response = await response
        except YouBlockedUserError:
            await event.reply("```un-Block @truthordaresbot ploxx```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.spill(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    async with bot.conversation("@Spillgame_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/spill ')
            response = await response
        except YouBlockedUserError:
            await event.reply("```un-Block @Spillgame_bot ploxx```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.fmulai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    async with bot.conversation("@Familys100_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/mulai')
            response = await response
        except YouBlockedUserError:
            await event.reply("```un-Block @Familys100_bot ploxx```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.fnext(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    async with bot.conversation("@Familys100_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=774181428))
            await conv.send_message(f'/next')
            response = await response
        except YouBlockedUserError:
            await event.reply("```un-Block @Familys100_bot ploxx```")
            return
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)


CMD_HELP.update({
    "games": "\
????????????????????????????: `.xogame`\
\nPenggunaan: Mainkan game XO bersama temanmu.\
\n????????????????????????????: `.mod <nama app>`\
\nPenggunaan: Dapatkan applikasi mod\
\n????????????????????????????: `.whisp <teks> <username/ID>`\
\nPenggunaan: Berikan pesan rahasia."
})


CMD_HELP.update({
    "games1": "\
????????????????????????????: `.truth`\
\nPenggunaan: Tantangan kejujuran.\
\n????????????????????????????: `.dare`\
\nPenggunaan: Tantangan lain.\
\n????????????????????????????: `.spill`\
\nPenggunaan: Spill pertanyaan.\
\n????????????????????????????: `.fmulai`\
\nPenggunaan: Kuis Family 100.\
\n????????????????????????????: `.fnext`\
\nPenggunaan: Kuis Family 100."
})

CMD_HELP.update({
    "games2": "\
????????????????????????????: `.tetris`\
\nPenggunaan: Jadul Game.\
\n????????????????????????????: `.puzzle`\
\nPenggunaan: Idem atas weh.\
\n????????????????????????????: `.gmbot`\
\nPenggunaan: Lets play bruh.\
\n????????????????????????????: `.glbot`\
\nPenggunaan: Play bae."
})
