# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Modified by Vckyouuu @VckyouuBitch
# Using By Geez Project GPL-3.0 License
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



import io
import textwrap


from PIL import Image, ImageDraw, ImageFont
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.stick (.*)")
async def stext(event):
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Text Anda.`")
        return

    await event.delete()

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 220
    font = ImageFont.truetype(
        "userbot/files/RobotoMono-Regular.ttf",
        size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(
            "userbot/files/RobotoMono-Regular.ttf",
            size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2,
         (512 - height) / 2),
        sticktext,
        font=font,
        fill="white")

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream)


CMD_HELP.update({
    "sticktex": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stick` <text>"
    "\nPenggunaan: Mengubah Teks/Kata-Kata, Menjadi Stiker Anda."
})
