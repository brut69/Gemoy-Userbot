# Port By @VckyouuBitch From Geez-Project
# Credits © Geez - projectsprojects
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


import os
import urllib

from telethon.tl import functions
from userbot.events import register
from userbot import (
    CMD_HELP,
    bot,
    ALIVE_NAME,
)
from userbot import TEMP_DOWNLOAD_DIRECTORY


OFFLINE_TAG = f"{ALIVE_NAME} #𝗢𝗙𝗙𝗟𝗜𝗡𝗘🔴"
ONLINE_TAG = f"{ALIVE_NAME} #𝗢𝗡𝗟𝗜𝗡𝗘🟢"
PROFILE_IMAGE = os.environ.get(
    "PROFILE_IMAGE", "https://telegra.ph/file/249f27d5b52a87babcb3f.jpg"
)


@register(outgoing=True, pattern="^.offline(?: |$)(.*)")
# pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Sudah dalam Mode Offline.**")
        return
    await event.edit("**Mengubah Profil menjadi Offline...**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(
        "https://telegra.ph/file/249f27d5b52a87babcb3f.jpg", "donottouch.jpg"
    )
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Mengubah profil menjadi OffLine.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    last_name = ""
    first_name = OFFLINE_TAG
    try:
        await bot(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nSaya Offline sekarang.**".format(
            first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@register(outgoing=True, pattern="^.unoff(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    user_it = "me"
    user = await event.client.get_entity(user_it)
    if user.first_name.startswith(OFFLINE_TAG):
        await event.edit("**Mengubah Profil menjadi Online...**")
    else:
        await event.edit("**Sudah Online.**")
        return
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    urllib.request.urlretrieve(PROFILE_IMAGE, "donottouch.jpg")
    photo = "donottouch.jpg"
    if photo:
        file = await event.client.upload_file(photo)
        try:
            await bot(functions.photos.UploadProfilePhotoRequest(file))
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
        else:
            await event.edit("**Mengubah profil menjadi Online.**")
    try:
        os.system("rm -fr donottouch.jpg")
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:disable=E0602
    first_name = ONLINE_TAG
    last_name = ""
    try:
        await bot(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                last_name=last_name, first_name=first_name
            )
        )
        result = "**`{} {}`\nSaya Online !**".format(first_name, last_name)
        await event.edit(result)
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


CMD_HELP.update(
    {
        "offline": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.offline`\
         \nPenggunaan: `Tambahkan tag offline di nama Anda dan ubah foto profil menjadi hitam`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.unoff`\
         \nPenggunaan: `Hapus Tag Offline dari nama Anda\ndan ubah foto profil menjadi vars PROFILE_IMAGE.`"
    }
)
