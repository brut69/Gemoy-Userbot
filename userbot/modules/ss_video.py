# Copyright (C) 2020 Alfiananda P.A
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


import asyncio
import os
import time

from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import progress


@register(outgoing=True, pattern=r"^\.ssvideo(?: |$)(.*)")
async def ssvideo(event):
    if not event.reply_to_msg_id:
        await event.edit("`Balas ke media apa pun..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`membalas video..`")
        return
    try:
        frame = int(event.pattern_match.group(1))
        if frame > 10:
            return await event.edit("`Hei..jangan terlalu banyak bicara`")
    except BaseException:
        return await event.edit("`Silakan masukkan nomor bingkai!`")
    if reply_message.photo:
        return await event.edit("`Hei..ini adalah gambar!`")
    if (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        return await event.edit("`File tidak didukung..`")
    elif (
        DocumentAttributeFilename(file_name="sticker.webp")
        in reply_message.media.document.attributes
    ):
        return await event.edit("`File tidak didukung..`")
    c_time = time.time()
    await event.edit("`Mengunduh media..`")
    ss = await bot.download_media(
        reply_message,
        "anu.mp4",
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[DOWNLOAD]")
        ),
    )
    try:
        await event.edit("`Pengolahan..`")
        command = f"vcsi -g {frame}x{frame} {ss} -o ss.png "
        os.system(command)
        await event.client.send_file(
            event.chat_id,
            "ss.png",
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        os.system("rm -rf *.png")
        os.system("rm -rf *.mp4")
    except BaseException as e:
        os.system("rm -rf *.png")
        os.system("rm -rf *.mp4")
        return await event.edit(f"{e}")


CMD_HELP.update({"ssvideo": "????????????????????????????: `.ssvideo` <bingkai>\
\nPenggunaan: ke ss bingkai video per bingkai"})
