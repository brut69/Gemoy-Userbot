# Ported By @VckyouuBitch From Geez - Projects
# Copyright © Geez - Projects
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


from youtube_dl import YoutubeDL

from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=".yt(a|v|sa|sv) (.*)", disable_errors=True)
async def download_from_youtube_(event):
    opt = event.pattern_match.group(1).lower()
    if opt == "a":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("Beri saya URL (youtube) untuk mengunduh audio!")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("`Berikan Tautan Audio Langsung Untuk Mengunduh`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "v":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        url = event.pattern_match.group(2).lower()
        if not url:
            return await event.edit("Beri saya URL (youtube) untuk mengunduh video!")
        try:
            request.get(url)
        except BaseException:
            return await event.edit("`Berikan Tautan Video Langsung Untuk Mengunduh`")
        xx = await event.edit(get_string("com_1"))
    elif opt == "sa":
        ytd = YoutubeDL(
            {
                "format": "bestaudio",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp3",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("Beri saya kueri penelusuran (youtube) untuk mengunduh audio!"
                                    )
        xx = await event.edit("`Mencari di YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("`Mengunduh lagu audio...`")
    elif opt == "sv":
        ytd = YoutubeDL(
            {
                "format": "best",
                "writethumbnail": True,
                "addmetadata": True,
                "geo-bypass": True,
                "nocheckcertificate": True,
                "outtmpl": "%(id)s.mp4",
            }
        )
        try:
            query = event.text.split(" ", 1)[1]
        except IndexError:
            return await event.edit("Beri saya kueri penelusuran (youtube) untuk mengunduh video!"
                                    )
        xx = await event.edit("`Menelusuri YouTube...`")
        url = await get_yt_link(query)
        await xx.edit("`Mengunduh lagu video...`")
    else:
        return
    await download_yt(xx, event, url, ytd)


CMD_HELP.update({
    "ytdownload":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.yta` <(youtube) link>\
   \nPenggunaan : Unduh audio dari tautan.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ytv <(youtube) link>`\
   \nPenggunaan : Unduh video dari tautan.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ytsa <(youtube) permintaan pencarian>`\
   \nPenggunaan : Cari dan unduh audio dari youtube.\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ytsv <(youtube) permintaan pencarian>`\
   \nPenggunaan : Cari dan unduh video dari youtube."
})
