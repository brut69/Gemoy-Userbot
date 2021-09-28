# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
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


""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("`𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙏𝙞𝙙𝙖𝙠 𝘿𝙞𝙩𝙚𝙢𝙪𝙠𝙖𝙣, 𝙃𝙖𝙧𝙖𝙥 𝙆𝙚𝙩𝙞𝙠 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝘿𝙚𝙣𝙜𝙖𝙣 𝘽𝙚𝙣𝙖𝙧`")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t 🤔 "
        await event.edit("⟢ 𝙂 𝘼 𝙈 𝙊 𝙉  -  𝙐 𝙎 𝙀 𝙍 𝘽 𝙊 𝙏 ⟣\n\n"
                         f"🧑‍💻 𝑫𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒓 {DEFAULTUSER}\n📂 𝑷𝒍𝒖𝒈𝒊𝒏𝒔 {len(modules)}\n"
                         "🛠️ 𝑭𝒐𝒍𝒍𝒐𝒘 𝒕𝒉𝒆 𝒂𝒗𝒂𝒊𝒍𝒂𝒃𝒍𝒆 𝒄𝒐𝒎𝒎𝒂𝒏𝒅𝒔\n📝 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 .𝐡𝐞𝐥𝐩 𝐚𝐝𝐦𝐢𝐧\n\n"
                         f"🤔{string}\n")
        await asyncio.sleep(1000)
        await event.delete()
