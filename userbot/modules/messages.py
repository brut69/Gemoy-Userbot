# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
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


from asyncio import sleep

from telethon.errors import rpcbaseerrors

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.purge$")
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        return await purg.edit("`Mohon Balas Ke Pesan ⛧ `")

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id, f"`𝑩𝒆𝒓𝒉𝒂𝒔𝒊𝒍 𝑴𝒆𝒏𝒈𝒉𝒂𝒑𝒖𝒔 𝑷𝒆𝒔𝒂𝒏`\
        \nJumlah Pesan Yang Dihapus {str(count)} Pesan")
    """
    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "𝑩𝒆𝒓𝒉𝒂𝒔𝒊𝒍 𝑴𝒆𝒏𝒈𝒉𝒂𝒑𝒖𝒔 𝑷𝒆𝒔𝒂𝒏 " + str(count) + " Pesan Berhasil  Dibersihkan.")
    """
    await sleep(2)
    await done.delete()


@register(outgoing=True, pattern=r"^\.purgeme")
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`𝑩𝒆𝒓𝒉𝒂𝒔𝒊𝒍 𝑴𝒆𝒏𝒈𝒉𝒂𝒑𝒖𝒔 𝑷𝒆𝒔𝒂𝒏,` " + str(count) + " `Pesan Telah Dihapus ⛧`",
    )
    """
    if BOTLOG:
        await delme.client.send_message(
            BOTLOG_CHATID,
            "`Telah Menghapus Pesan,` " + str(count) + " Pesan Telah Dihapus ⛧`")
    """
    await sleep(2)
    i = 1
    await smsg.delete()


@register(outgoing=True, pattern=r"^\.del$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "`Berhasil Menghapus Pesan ⛧`")
            """
        except rpcbaseerrors.BadRequestError:
            await delme.edit("`Tidak Bisa Menghapus Pesan`")
            """
            if BOTLOG:
                await delme.client.send_message(
                    BOTLOG_CHATID, "`Tidak Bisa Menghapus Pesan`")
            """


@register(outgoing=True, pattern=r"^\.edit")
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i += 1
    """
    if BOTLOG:
        await edit.client.send_message(BOTLOG_CHATID,
                                       "`Berhasil Mengedit Pesan ツ`")
   """


@register(outgoing=True, pattern=r"^\.sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    """
    if BOTLOG:
        await destroy.client.send_message(BOTLOG_CHATID,
                                          "`⛧ SD Berhasil Dilakukan ⛧`")
    """


CMD_HELP.update({"purge": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.purge`"
                 "\nPenggunaan : Membersihkan semua pesan mulai dari pesan yang dibalas."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.purgeme` <angka>"
                 "\nPenggunaan: Menghapus jumlah pesan anda, yang mau anda hapus."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙 : `.del`"
                 "\nPenggunaan: Menghapus pesan, balas ke pesan."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.edit` <pesan baru>"
                 "\nPenggunaan: Ganti pesan terakhir Anda dengan <pesan baru>."
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sd` <x> <pesan>"
                 "\nPenggunaan: Membuat pesan yang hancur sendiri dalam x detik."
                 "\n**NOTE**: Jaga di bawah 80 detik karena bot Anda akan tertidur."})
