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


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP, ALIVE_NAME
from platform import uname


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.igsave ?(.*)")
async def igsaver(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Reply Ke Link Instagram Ya..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Link Media Instagram Untuk di Download`")
        return
    chat = "@SaveAsBot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Sedang Memproses...`")
        return
    await event.edit("`Sedang Memproses...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=523131145)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.edit("`Mohon Pergi ke ` @SaveAsbot `Lalu Tekan Start dan Coba Lagi.`")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "Uhmm Sepertinya Private."
            )
        else:
            await event.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Download By {DEFAULTUSER}**",
            )
            await event.client.send_read_acknowledge(conv.chat_id)
            await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
            await event.delete()


CMD_HELP.update({"igsaver": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.igsave`"
                 "\nPenggunaan: Download Postingan di Instagram, Silahkan Salin Link Postingan Instagram Yang Ingin Anda Download Lalu Kirim Link, atau Reply dan Ketik `.igsaver`"})
