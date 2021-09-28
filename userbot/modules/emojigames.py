# fix by @heyworld for OUB
# bug fixed by @d3athwarrior
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

from telethon.tl.types import InputMediaDice
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎲'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎲'))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎯'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎯'))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.basket(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🏀'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🏀'))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.bowl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎳'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎳'))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('⚽'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('⚽'))
        except BaseException:
            pass


@register(outgoing=True, pattern="^.ding(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    await event.delete()
    r = await event.reply(file=InputMediaDice('🎰'))
    if input_str:
        try:
            required_number = int(input_str)
            while not r.media.value == required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice('🎰'))
        except BaseException:
            pass


CMD_HELP.update({
    "emojigames":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.dice` 1-6 or `.dart` 1-6 or `.ball` 1-5 `.basket` 1-5 or `.bowl` `.ding`\
\nPenggunaan: hahaha hanya keajaiban.\nPeringatan:`Jangan gunakan nilai lain atau bot akan mogok`"
})
