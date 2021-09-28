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

""" Userbot module for getting information about the server. """

from platform import uname


from userbot import ALIVE_NAME, BOT_VER, is_mongo_alive, is_redis_alive
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.db$")
async def amireallydbs(dbs):
    if not is_mongo_alive() and not is_redis_alive():
        db = "Both Mongo and Redis Database seems to be failing!"
    elif not is_mongo_alive():
        db = "Mongo DB seems to be failing!"
    elif not is_redis_alive():
        db = "Redis Cache seems to be failing!"
    else:
        db = "Databases functioning normally!"
    await dbs.edit(""
                   f"**User :** `{DEFAULTUSER}` \n"
                   f"**Status Database:** `{db}`\n"
                   f"**𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 :** `{BOT_VER}`"
                   "")
