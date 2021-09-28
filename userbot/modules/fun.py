# Copyright by @danish
# Recode by @mrismanaziz
# @SharingUserbot
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

import cv2
import PIL

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import progress


@register(outgoing=True, pattern=r"^\.honka(?: |$)(.*)")
async def frg(animu):
    text = animu.pattern_match.group(1)
    if not text:
        await animumedit("**Silahkan Masukan Kata!**")
    else:
        sticcers = await bot.inline_query("honka_says_bot", f"{text}.")
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await animu.edit(
            "`You cannot send inline results in this chat (caused by SendInlineBotResultRequest)`"
        )
    await animu.delete()


@register(outgoing=True, pattern=r"^\.rgif(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    reply = await event.get_reply_message()
    await event.edit("`Checking...`")
    download = await bot.download_media(reply.media)
    img = cv2.VideoCapture(download)
    ret, frame = img.read()
    cv2.imwrite("danish.png", frame)
    danish = PIL.Image.open("danish.png")
    dark, python = danish.size
    cobra = f"""ffmpeg -f lavfi -i color=c=00ff00:s={dark}x{python}:d=10 -loop 1 -i danish.png -filter_complex "[1]rotate=angle=PI*t:fillcolor=none:ow='hypot(iw,ih)':oh=ow[fg];[0][fg]overlay=x=(W-w)/2:y=(H-h)/2:shortest=1:format=auto,format=yuv420p" -movflags +faststart danish.mp4 -y"""
    await event.edit("```Processing ...```")
    if event.reply_to_msg_id:
        event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cobra, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    await event.edit("```Uploading...```")
    c_time = time.time()
    await event.client.send_file(
        event.chat_id,
        "danish.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, event, c_time, "[UPLOAD]")
        ),
    )
    await event.delete()
    os.system("rm -f downloads/*.jpg")
    os.system("rm -f downloads/*.png")
    os.system("rm -f downloads/*.webp")
    os.system("rm -f *.jpg")
    os.system("rm -f *.png")
    os.remove("danish.mp4")


CMD_HELP.update(
    {
        "rgif": "𝙋𝙡𝙪𝙜𝙞𝙣: `rgif`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gif` <sambil reply ke media>\
        \nPenggunaan: Untuk mengubah gambar jadi gif memutar.\
    "
    }
)


CMD_HELP.update(
    {
        "fun": "𝙋𝙡𝙪𝙜𝙞𝙣: `fun`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.rst` <text>\
        \nPenggunaan: Untuk membuat stiker teks dengan templat stiker acak.\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.honka` <text>\
        \nPenggunaan: Untuk membuat stiker teks dengan templat stiker Honka bot.\
    "
    }
)
