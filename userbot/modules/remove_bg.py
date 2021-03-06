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
import os

import requests
from telethon.tl.types import MessageMediaPhoto

from userbot import CMD_HELP, REM_BG_API_KEY, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register


@register(outgoing=True, pattern=r"^\.rbg(?: |$)(.*)")
async def kbg(remob):
    """For .rbg command, Remove Image Background."""
    if REM_BG_API_KEY is None:
        return await remob.edit(
            "`Error: Remove.BG API key missing! Add it to environment vars or config.env.`"
        )
    input_str = remob.pattern_match.group(1)
    message_id = remob.message.id
    if remob.reply_to_msg_id:
        message_id = remob.reply_to_msg_id
        reply_message = await remob.get_reply_message()
        await remob.edit("`Processing..`")
        try:
            if isinstance(
                reply_message.media, MessageMediaPhoto
            ) or "image" in reply_message.media.document.mime_type.split("/"):
                downloaded_file_name = await remob.client.download_media(
                    reply_message, TEMP_DOWNLOAD_DIRECTORY
                )
                await remob.edit("`Removing background from this image..`")
                output_file_name = await ReTrieveFile(downloaded_file_name)
                os.remove(downloaded_file_name)
            else:
                await remob.edit("`How do I remove the background from this ?`")
        except Exception as e:
            return await remob.edit(str(e))
    elif input_str:
        await remob.edit(
            f"`Removing background from online image hosted at`\n{input_str}"
        )
        output_file_name = await ReTrieveURL(input_str)
    else:
        return await remob.edit("`I need something to remove the background from.`")
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "removed_bg.png"
            await remob.client.send_file(
                remob.chat_id,
                remove_bg_image,
                caption="Background removed using remove.bg",
                force_document=True,
                reply_to=message_id,
            )
            await remob.delete()
    else:
        await remob.edit(
            "**Error (Invalid API key, I guess ?)**\n`{}`".format(
                output_file_name.content.decode("UTF-8")
            )
        )


# this method will call the API, and return in the appropriate format
# with the name provided.
async def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
    return r


async def ReTrieveURL(input_url):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    data = {"image_url": input_url}
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        data=data,
        allow_redirects=True,
        stream=True,
    )
    return r


CMD_HELP.update(
    {
        "removebg": "????????????????????????????: `.rbg` <Tautkan ke Gambar> atau balas gambar apa pun\
         \n**Warning**: tidak berfungsi pada stiker.\
        \nPenggunaan: Menghapus latar belakang gambar menggunakan remove.bg API."
    }
)
