# Alvin Gans
# Copyright (C) 2019 The Raphielscape Company LLC.
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


from io import BytesIO
from random import choice, randint
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont
from requests import get

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.imp (.*)")
async def f_load(message):
    clrs = {
        "red": 1,
        "lime": 2,
        "green": 3,
        "blue": 4,
        "cyan": 5,
        "brown": 6,
        "purple": 7,
        "pink": 8,
        "orange": 9,
        "yellow": 10,
        "white": 11,
        "black": 12,
    }
    clr = randint(1, 12)
    text = message.pattern_match.group(1)
    reply = await message.get_reply_message()
    if text in clrs:
        clr = clrs[text]
        text = None
    if not text:
        if not reply:
            await bruh(message, message.sender)
            return
        if not reply.text:
            await bruh(message, reply.sender)
            return
        text = reply.pattern_match.group(1)

    if text.split(" ")[0] in clrs:
        clr = clrs[text.split(" ")[0]]
        text = " ".join(text.split(" ")[1:])

    if text == "colors":
        await message.edit(
            ("Cores disponíveis:\n" + "\n".join(f"• `{i}`" for i in list(clrs.keys())))
        )

        return

    url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"
    font = ImageFont.truetype(BytesIO(get(url + "bold.ttf").content), 60)
    imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    text_ = "\n".join("\n".join(wrap(part, 30)) for part in text.split("\n"))
    w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new("RGBA", (w + 30, h + 30))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000"
    )
    w = imposter.width + text.width + 10
    h = max(imposter.height, text.height)
    image = Image.new("RGBA", (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    output = BytesIO()
    output.name = "imposter.webp"
    image.save(output)
    output.seek(0)
    await message.delete()
    await message.client.send_file(message.to_id, output, reply_to=reply)


async def bruh(message, user):
    fn = user.first_name
    ln = user.last_name
    name = fn + (" " + ln if ln else "")
    name = "***" + name
    await message.edit(name + choice([" ", " Tidak "]) + "Adalah Seorang Penipu! ***")


CMD_HELP.update(
    {
        "amongus": "𝙋𝙡𝙪𝙜𝙞𝙣: `amongus`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.imposter`\
        \nPenggunaan: Kirimkan gambar seorang impostor Among US dengan kalimat dari Anda.\
    "
    }
)
