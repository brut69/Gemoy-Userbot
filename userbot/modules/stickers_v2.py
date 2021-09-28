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
import io
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.itos$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Bruh ini bukan pesan gambar, balas pesan gambar")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("Bruh, ini bukan gambar")
        return
    chat = "@buildstickerbot"
    await event.edit("Membuat Sticker..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=164977173))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("buka blokir saya (@buildstickerbot) dan coba lagi")
            return
        if response.text.startswith("Hi!"):
            await event.edit("Bisakah Anda menonaktifkan pengaturan privasi penerusan Anda untuk selamanya?")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
            await event.client.delete_message(event.chat_id, [msg.id, response.id])


@register(outgoing=True, pattern="^.get$")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Mohon Maaf, Balas Ke Sticker Terlebih Dahulu.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`Mohon Maaf, Balas Ke Sticker Terlebih Dahulu.`")
        return
    chat = "@stickers_to_image_bot"
    await event.edit("`Sedang Mengubah Sticker Menjadi Gambar...`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            msg = await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Mohon Maaf, Buka Blokir @stickers_to_image_bot Lalu Coba Lagi.")
            return
        if response.text.startswith("I understand only stickers"):
            await event.edit("`Maaf, Saya Tidak Bisa Mengubah Ini Menjadi Gambar, Periksa Kembali Apakah Itu Sticker Animasi ?`")
        else:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=611085086))
            response = await response
            if response.text.startswith("..."):
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=611085086))
                response = await response
                await event.delete()
                await event.client.send_message(event.chat_id, response.message, reply_to=reply_message.id)
                await event.client.delete_message(event.chat_id, [msg.id, response.id])
            else:
                await event.edit("`Tolong Coba Lagi.`")
        await bot.send_read_acknowledge(conv.chat_id)


@register(outgoing=True, pattern="^.stoi$")
async def sticker_to_png(sticker):
    if not sticker.is_reply:
        await sticker.edit("`Informasi NULL untuk diambil...`")
        return False

    img = await sticker.get_reply_message()
    if not img.document:
        await sticker.edit("`Mohon Maaf, Ini Bukanlah Sticker`")
        return False

    await sticker.edit("`Berhasil Mengambil Sticker Ini !`")
    image = io.BytesIO()
    await sticker.client.download_media(img, image)
    image.name = "sticker.png"
    image.seek(0)
    await sticker.client.send_file(
        sticker.chat_id, image, reply_to=img.id, force_document=True
    )
    await sticker.delete()
    return


CMD_HELP.update({
    "stickpic": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.itos`"
    "\nPenggunaan: Balas ke sticker atau gambar/n`.itos` untuk mengambil sticker bukan ke pack."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.get`"
    "\nPenggunaan: Balas ke sticker untuk mendapatkan file 'PNG' sticker."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stoi`"
    "\nPenggunaan: Balas Ke sticker untuk mendapatkan file 'PNG' sticker."})
