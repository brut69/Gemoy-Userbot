# Ported By VCKYOU @VckyouuBitch
# Credits © Geez-Project
# Ya gitu deh:')
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


from shutil import rmtree
from userbot.events import register
from userbot import CMD_HELP
from userbot.utils import googleimagesdownload


@register(outgoing=True, pattern="^.img (.*)")
async def goimg(event):
    query = event.pattern_match.group(1)
    if not query:
        return await event.edit("`Berikan sesuatu untuk ditelusuri...`")
    await event.edit("`Memproses Tetap Sabar...`")
    if ";" in query:
        try:
            lmt = int(query.split(";")[1])
            query = query.split(";")[0]
        except BaseExceptaion:
            lmt = 5
    else:
        lmt = 5
    gi = googleimagesdownload()
    args = {
        "keywords": query,
        "limit": lmt,
        "format": "jpg",
        "output_directory": "./downloads/",
    }
    pth = gi.download(args)
    ok = pth[0][query]
    await event.client.send_file(event.chat_id, ok, caption=query, album=True)
    rmtree(f"./downloads/{query}/")
    await event.delete()


CMD_HELP.update(
    {
        "image": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.img` <pencarian_kueri>\
         \nPenggunaan: Melakukan pencarian gambar di Google dan menampilkan 5 gambar."
    }
)
