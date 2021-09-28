# Port By @VckyouuBitch From Geez - Project
# Copyright © Geez - Project
# Credits By UltroidUltroid
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


from telethon.tl.types import ChannelParticipantAdmin as admin
from telethon.tl.types import ChannelParticipantCreator as owner
from telethon.tl.types import UserStatusOffline as off
from telethon.tl.types import UserStatusOnline as onn
from telethon.tl.types import UserStatusRecently as rec
from telethon.utils import get_display_name

from userbot.events import register
from userbot import CMD_HELP


@register(
    outgoing=True,
    pattern=r"^\.tag(on|off|all|bots|rec|admins|owner)?(.*)",
    disable_errors=True,
)
async def _(e):
    okk = e.text
    lll = e.pattern_match.group(2)
    users = 0
    o = 0
    nn = 0
    rece = 0
    if lll:
        xx = f"{lll}"
    else:
        xx = ""
    async for bb in e.client.iter_participants(e.chat_id, 99):
        users = users + 1
        x = bb.status
        y = bb.participant
        if isinstance(x, onn):
            o = o + 1
            if "on" in okk:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, off):
            nn = nn + 1
            if "off" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(x, rec):
            rece = rece + 1
            if "rec" in okk:
                if not (bb.bot or bb.deleted):
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if isinstance(y, owner):
            if "admin" or "owner" in okk:
                xx += f"\n👑 [{get_display_name(bb)}](tg://user?id={bb.id}) 👑"
        if isinstance(y, admin):
            if "admin" in okk:
                if not bb.deleted:
                    xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "all" in okk:
            if not (bb.bot or bb.deleted):
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
        if "bot" in okk:
            if bb.bot:
                xx += f"\n[{get_display_name(bb)}](tg://user?id={bb.id})"
    await e.client.send_message(e.chat_id, xx)
    await e.delete()


CMD_HELP.update({
    "tags": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag all`"
    "\nPenggunaan: Tandai 100 Anggota obrolan teratas."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag admin`"
    "\nPenggunaan: Tag Admin obrolan itu."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag owner`"
    "\nPenggunaan: Tag Pemilik obrolan itu."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag bot`"
    "\nPenggunaan: Tandai Bot dari obrolan itu."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag rec`"
    "\nPenggunaan: Tandai Anggota Aktif baru-baru ini."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag on`"
    "\nPenggunaan: Tandai Anggota online (hanya berfungsi jika privasi tidak aktif)."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tag off`"
    "\nPenggunaan: Tandai Anggota Offline (hanya berfungsi jika privasi tidak aktif)."
})
