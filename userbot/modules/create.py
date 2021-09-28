# lorduserbot
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

from telethon.tl import functions
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.buat (gb|gc|ch)(?: |$)(.*)")
async def telegraphs(grop):
    """ For .create command, Creating New Group & Channel """
    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):
        if grop.fwd_from:
            return
        type_of_group = grop.pattern_match.group(1)
        group_name = grop.pattern_match.group(2)
        if type_of_group == "gb":
            try:
                result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@MissRose_bot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name
                ))
                created_chat_id = result.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await grop.edit("Grup/Channel {} Berhasil Dibuat. Tekan [{}]({}) Untuk Melihatnya".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))
        elif type_of_group == "gc" or type_of_group == "ch":
            try:
                r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                    title=group_name,
                    about="`Selamat Datang Di Channel Ini!`",
                    megagroup=False if type_of_group == "c" else True
                ))
                created_chat_id = r.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await grop.edit("Grup/Channel {} Berhasil Dibuat. Tekan [{}]({}) Untuk Melihatnya".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))

CMD_HELP.update({
    "membuat": "\
Membuat\
\nPenggunaan: Untuk membuat Channel, Grup dan Grup bersama Bot.\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.buat gc` <nama grup>\
\nPenggunaan: Membuat grup mu.\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.buat gb` <nama grup>\
\nPenggunaan: Membuat Grup bersama bot.\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.buat ch` <nama channel>\
\nPenggunaan: Membuat sebuah Channel.\
"})
