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


"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.gban REASON
.ungban REASON"""


import asyncio
from userbot.events import register
from userbot import ALIVE_NAME, G_BAN_LOGGER_GROUP, bot
# imported from uniborg by @heyworld

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.gbanb(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Setel G_BAN_LOGGER_GROUP di vars jika tidak, modul tidak akan berfungsi.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/gban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**gbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**Pengguna diblokir oleh {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()


@register(outgoing=True, pattern="^.ungbanb(?: |$)(.*)")
async def _(event):
    if G_BAN_LOGGER_GROUP is None:
        await event.edit("Setel G_BAN_LOGGER_GROUP di vars jika tidak, modul tidak akan berfungsi.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await bot.send_message(
            G_BAN_LOGGER_GROUP,
            "/ungban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()
    await event.reply("**ungbanning...**")
    asyncio.sleep(3.5)
    await event.edit(f"**Pemblokiran pengguna dibatalkan oleh {DEFAULTUSER}**")
    asyncio.sleep(5)
    await event.delete()
