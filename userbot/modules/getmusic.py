# Copyright (C) 2020 Aidil Aryanto.
# Vsong ported by AnggaR69S
# All rights reserved.
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
import glob
import os
import time
from asyncio.exceptions import TimeoutError

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pylast import User
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeVideo

from userbot import CMD_HELP, LASTFM_USERNAME, bot, lastfm
from userbot.events import register
from userbot.utils import chrome, progress


async def getmusicvideo(cat):
    video_link = ""
    search = cat
    driver = await chrome()
    driver.get("https://www.youtube.com/results?search_query=" + search)
    user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for i in user_data:
        video_link = i.get_attribute("href")
        break
    command = 'youtube-dl -f "[filesize<50M]" --merge-output-format mp4 ' + video_link
    os.system(command)


@register(outgoing=True, pattern=r"^\.nsong (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Kesalahan: Tidak ada scrobble saat ini yang ditemukan.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@WooMaiBot"
    link = f"/netease {track}"
    await event.edit("`Mencari...`")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Mengunduh...Mohon tunggu`")
            try:
                msg = await conv.send_message(link)
                response = await conv.get_response()
                respond = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("```Silakan buka blokir @WooMaiBot dan coba lagi```")
                return
            await event.edit("`Mengirim Musik Anda...`")
            await asyncio.sleep(3)
            await bot.send_file(event.chat_id, respond)
        await event.client.delete_messages(
            conv.chat_id, [msg.id, response.id, respond.id]
        )
        await event.delete()
    except TimeoutError:
        return await event.edit("`Kesalahan: `@WooMaiBot` tidak merespons!.`")


@register(outgoing=True, pattern=r"^\.lsong(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Masukkan tautan yang valid untuk mengunduh dari`")
    else:
        await event.edit("`Mengunduh...`")
    chat = "@MusicsHunterBot"
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg_start = await conv.send_message("/start")
                response = await conv.get_response()
                msg = await conv.send_message(d_link)
                details = await conv.get_response()
                song = await conv.get_response()
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("`Buka blokir `@MusicsHunterBot` dan coba lagi`")
                return
            await bot.send_file(event.chat_id, song, caption=details.text)
            await event.client.delete_messages(
                conv.chat_id, [msg_start.id, response.id, msg.id, details.id, song.id]
            )
            await event.delete()
    except TimeoutError:
        return await event.edit("`Kesalahan: `@MusicsHunterBot` tidak merespons!.`")


@register(outgoing=True, pattern=r"^\.ssong (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    if event.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            return await event.edit("`Kesalahan: Tidak ada data scrobbling yang ditemukan.`")
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = event.pattern_match.group(2)
        song = event.pattern_match.group(3)
    track = str(artist) + " - " + str(song)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Mendapatkan Musik Anda```")
    try:
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Mengunduh...`")
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                msg = await bot.send_message(chat, track)
                respond = await response
                res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
                )
                r = await res
                """- don't spam notif -"""
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Buka blokir `@SpotifyMusicDownloaderBot` dan coba lagi`")
                return
            await bot.forward_messages(event.chat_id, respond.message)
        await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Kesalahan: `@SpotifyMusicDownloaderBot` tidak merespons!.`"
        )


@register(outgoing=True, pattern=r"^\.vsong(?: |$)(.*)")
async def _(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
        await event.edit("`Tunggu..! Saya menemukan lagu video Anda..`")
    elif reply:
        query = str(reply.message)
        await event.edit("`Tunggu..! Saya menemukan lagu video Anda..`")
    else:
        await event.edit("`Apa yang Seharusnya Saya Temukan?`")
        return
    await getmusicvideo(query)
    l = glob.glob(("*.mp4")) + glob.glob(("*.mkv")) + glob.glob(("*.webm"))
    if l:
        await event.edit("`Ya.. saya menemukan sesuatu.`")
    else:
        await event.edit(f"`Maaf.. saya tidak dapat menemukan apa pun dengan` **{query}**")
        return
    try:
        loa = l[0]
        metadata = extractMetadata(createParser(loa))
        duration = 0
        width = 0
        height = 0
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        os.system("cp *mp4 thumb.mp4")
        os.system("ffmpeg -i thumb.mp4 -vframes 1 -an -s 480x360 -ss 5 thumb.jpg")
        thumb_image = "thumb.jpg"
        c_time = time.time()
        await event.client.send_file(
            event.chat_id,
            loa,
            force_document=False,
            thumb=thumb_image,
            allow_cache=False,
            caption=query,
            supports_streaming=True,
            reply_to=reply_to_id,
            attributes=[
                DocumentAttributeVideo(
                    duration=duration,
                    w=width,
                    h=height,
                    round_message=False,
                    supports_streaming=True,
                )
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(d, t, event, c_time, "[UPLOAD]", loa)
            ),
        )
        await event.edit(f"**{query}** `Berhasil Diunggah..!`")
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
    except BaseException:
        os.remove(thumb_image)
        os.system("rm *.mkv *.mp4 *.webm")
        return


CMD_HELP.update({"getmusic": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nsong <Artist - Song Title>`"
                 "\nPenggunaan: Unduh musik dengan nama (@WooMaiBot)"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lsong <Spotify/Deezer Link>`"
                 "\nPenggunaan: Unduh musik melalui tautan (@MusicsHunterBot)"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ssong <Artist - Song Title>`"
                 "\nPenggunaan: Unduh musik berdasarkan nama (@SpotifyMusicDownloaderBot)"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nsong now`"
                 "\nPenggunaan: Unduh scrobble LastFM saat ini dengan @WooMaiBot"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ssong now`"
                 "\nPenggunaan: Unduh scrobble LastFM saat ini dengan @SpotifyMusicDownloaderBot"
                 "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vsong` <Artist - Song Title>"
                 "\nPenggunaan: Menemukan dan mengunggah klip video.\\in"})
