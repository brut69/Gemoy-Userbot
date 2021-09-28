# Port By @VckyouuBitch From GeezProjects
# Copyright © 2021 Geez-ProjectsGeez-Projects
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


from telethon.tl.types import (
    ChannelParticipantsKicked,
)

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^\.allunban(?: |$)(.*)", groups_only=True)
async def _(event):
    await event.edit("`Sedang Mencari List Banning.`")
    p = 0
    (await event.get_chat()).title
    async for i in event.client.iter_participants(
        event.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await event.client.edit_permissions(event.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await event.edit("`Sukses Menghapus List Banning`")


CMD_HELP.update(
    {
        "allunban": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.allunban`\
    \nPenggunaan: Membatalkan semua Ban Di Anggota Grup."
    }
)
