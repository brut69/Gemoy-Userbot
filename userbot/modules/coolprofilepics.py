# credits to the respective owner xD
# imported by @heyworld
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


import requests
import re
import random

import urllib
import os

from telethon.tl import functions

import asyncio


from userbot.events import register
from userbot import CMD_HELP

COLLECTION_STRING = [
    "epic-fantasy-wallpaper",
    "castle-in-the-sky-wallpaper",
    "fantasy-forest-wallpaper",
    "fantasy-wallpaper-1080p",
    "toothless-wallpaper-hd",
    "japanese-art-wallpaper",
    "star-wars-landscape-wallpaper",
    "4k-sci-fi-wallpaper",
    "minion-screensavers-wallpaper",
    "zootopia-hd-wallpaper",
    "gravity-falls-hd-wallpaper",
    "cool-cartoon-wallpaper",
    "disney-movie-wallpaper",
    "cute-pokemon-wallpapers",
    "4k-anime-wallpaper",
    "balance-druid-wallpaper",
    "harry-potter-wallpaper",
    "funny-meme-wallpaper",
    "minimalist-hd-wallpaper",
    "cute-animal-wallpaper-backgrounds",
    "3840-x-1080-wallpaper",
    "wallpaper-outer-space",
    "best-wallpapers-in-the-world",
    "funny-desktop-backgrounds",
    "funny-cats-wallpapers",
    "cool-cat-wallpaper",
    "doge-wallpaper-hd",
    "ice-cream-cone-wallpaper",
    "food-wallpaper-background",
    "snowy-christmas-scenes-wallpaper",
    "life-quotes-wallpaper"
]


async def animepp():

    os.system("rm -rf donot.jpg")
    rnd = random.randint(0, len(COLLECTION_STRING) - 1)
    pack = COLLECTION_STRING[rnd]
    pc = requests.get("http://getwallpapers.com/collection/" + pack).text
    f = re.compile(r'/\w+/full.+.jpg')
    f = f.findall(pc)
    fy = "http://getwallpapers.com" + random.choice(f)
    print(fy)

    if not os.path.exists("f.ttf"):
        urllib.request.urlretrieve(
            "https://github.com/rebel6969/mym/raw/master/Rebel-robot-Regular.ttf", "f.ttf")
    urllib.request.urlretrieve(fy, "donottouch.jpg")


@register(outgoing=True, pattern="^.pprandom(?: |$)(.*)")
async def main(event):
    await event.edit("`Sedang Mengubah Photo Profile Anda...`")

    while True:
        await animepp()

        file = await event.client.upload_file("donottouch.jpg")

        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(3600)  # Edit this to your required needs

CMD_HELP.update({
    "randompp": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pprandom`"
    "\nPenggunaan: Mengubah Photo Profile Anda Secara Random."})
