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
            await event.edit("`πππ§ππ£π©ππ πππππ  πΏππ©ππ’πͺπ ππ£, πππ§ππ₯ πππ©ππ  πππ§ππ£π©ππ πΏππ£πππ£ π½ππ£ππ§`")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\tβ‘"
        await event.edit("β’ π πΌ π π π  -  π π π π π½ π π β£\n\n"
                         f"π§βπ» π«ππππππππ {DEFAULTUSER}\nπ π·ππππππ {len(modules)}\n"
                         "π οΈ π­πππππ πππ πππππππππ ππππππππ\nπ ππ±ππ¦π©π₯π `.help ping`\n\n"
                         f"π€{string}\n")
        await asyncio.sleep(1000)
        await event.delete()
