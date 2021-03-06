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

"""Count the Number of Dialogs you have in your Telegram Account
Syntax: .stats"""

import logging
import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from userbot.events import register

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)
logger = logging.getLogger(__name__)


@register(outgoing=True, pattern=r"^.stats(?: |$)(.*)")
async def stats(event: NewMessage.Event) -> None:  # pylint: disable = R0912, R0914, R0915
    """Perintah untuk mendapatkan statistik tentang akun"""
    await event.edit('`Mengumpulkan statistik, Tunggu Master`')
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity

        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog,
            # limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1

            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1

        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1

        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1

        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time

    full_name = inline_mention(await event.client.get_me())
    response = f'???? **Statistik untuk {full_name}** \n\n'
    response += f'**Obrolan Pribadi:** {private_chats} \n'
    response += f'   ??? `Pengguna: {private_chats - bots}` \n'
    response += f'   ??? `Bot: {bots}` \n'
    response += f'**Grup:** {groups} \n'
    response += f'**Saluran:** {broadcast_channels} \n'
    response += f'**Admin di Grup:** {admin_in_groups} \n'
    response += f'   ??? `Pencipta: {creator_in_groups}` \n'
    response += f'   ??? `Hak Admin: {admin_in_groups - creator_in_groups}` \n'
    response += f'**Admin di Saluran:** {admin_in_broadcast_channels} \n'
    response += f'   ??? `Pencipta: {creator_in_channels}` \n'
    response += f'   ??? `Hak Admin: {admin_in_broadcast_channels - creator_in_channels}` \n'
    response += f'**Belum dibaca:** {unread} \n'
    response += f'**Sebutan yang Belum Dibaca:** {unread_mentions} \n\n'
    response += f'__It Telah mengambil:__ {stop_time:.02f}s \n'

    await event.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
