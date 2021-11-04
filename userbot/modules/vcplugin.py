# Credits: @mrismanaziz
# Thanks To @tofik_dn || https://github.com/tofikdn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0deLunatic0de
#
#
# port to different userbot @dunottagme
#

import asyncio

from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
from telethon.tl import types
from telethon.utils import get_display_name
from youtubesearchpython import VideosSearch

#from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import edit_or_reply
from userbot.utils.queues.queues import (
    QUEUE,
    add_to_queue,
    clear_queue,
    get_queue,
    pop_an_item,
)


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1)
        for r in search.result()["result"]:
            ytid = r["id"]
            songname = r["title"]
            url = f"https://www.youtube.com/watch?v={ytid}"
        return [songname, url]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format, link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        f"{format}",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    return 0, stderr.decode()


async def skip_item(chat_id, h):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    try:
        x = int(h)
        songname = chat_queue[x][0]
        chat_queue.pop(x)
        return songname
    except Exception as e:
        print(e)
        return 0


async def skip_current_song(chat_id):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    if len(chat_queue) == 1:
        await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        return 1
    songname = chat_queue[1][0]
    url = chat_queue[1][1]
    link = chat_queue[1][2]
    type = chat_queue[1][3]
    RESOLUSI = chat_queue[1][4]
    if type == "Audio":
        await call_py.change_stream(
            chat_id,
            AudioPiped(
                url,
            ),
        )
    elif type == "Video":
        if RESOLUSI == 720:
            hm = HighQualityVideo()
        elif RESOLUSI == 480:
            hm = MediumQualityVideo()
        elif RESOLUSI == 360:
            hm = LowQualityVideo()
        await call_py.change_stream(
            chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
        )
    pop_an_item(chat_id)
    return [songname, link, type]


@register(outgoing=True, pattern="^.play(?: |$)(.*)")
async def vc_play(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.audio
        and not replied.voice
        and not title
        or not replied
        and not title
    ):
        await edit_or_reply(event, "**🤔 Silahkan Masukan Judul Lagu**")
    elif replied and not replied.audio and not replied.voice or not replied:
        response = await edit_or_reply(event, "`⏳ Searching ...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        if search == 0:
            await response.edit(
                "**Tidak Dapat Menemukan Lagu** `Coba cari dengan Judul yang Lebih Spesifik`"
            )
        else:
            songname = search[0]
            url = search[1]
            format = "bestaudio"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await response.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                await response.edit(
                    f"👥 **Lagu Ditambahkan Ke antrian »** `#{pos}`\n\n**👣 Judul:** [{songname}]({url})\n**👥 Chat ID:** `{chat_id}`\n👤 **Atas permintaan:** {from_user}"
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            ytlink,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                    await response.edit(
                        f"👣 **Judul:** [{songname}]({url})\n**👥 Chat ID:** `{chat_id}`\n👥 **Status:** `Sedang Memutar`\n👤 **Atas permintaan:** {from_user}",
                        link_preview=False,
                    )
                except Exception as ep:
                    await response.edit(f"`{ep}`")

    else:
        response = await edit_or_reply(replied, "`📥 Downloading`")
        dl = await replied.download_media()
        link = replied.link
        if replied.audio:
            songname = "Telegram Music Player..."
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await response.edit(
                f"👥 **Lagu Ditambahkan Ke antrian »** `#{pos}`\n\n**👣 Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👤 **Atas permintaan:** {from_user}"
            )
        else:
            await call_py.join_group_call(
                chat_id,
                AudioPiped(
                    dl,
                ),
                stream_type=StreamType().pulse_stream,
            )
            add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            await response.edit(
                f"👣 **Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👥 **Status:** `Sedang Memutar`\n👤 **Atas permintaan:** {from_user}",
                link_preview=False,
            )


@register(outgoing=True, pattern="^.vplay(?: |$)(.*)")
async def vc_vplay(event):
    title = event.pattern_match.group(1)
    replied = await event.get_reply_message()
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.video
        and not replied.document
        and not title
        or not replied
        and not title
    ):
        return await edit_or_reply(event, "**🤔 Silahkan Masukan Judul Video**")
    if replied and not replied.video and not replied.document:
        xnxx = await edit_or_reply(event, "`⏳ Searching ...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit(
                "**Tidak Dapat Menemukan Video** `Coba cari dengan Judul yang Lebih Spesifik`"
            )
        else:
            songname = search[0]
            url = search[1]
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                await xnxx.edit(
                    f"📺 **Video Ditambahkan Ke antrian »** `#{pos}`\n\n**👣 Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👤 **Atas permintaan:** {from_user}"
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    await xnxx.edit(
                        f"**👣 Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👥 **Status:** `Sedang Memutar Video`\n👤 **Atas permintaan:** {from_user}",
                        link_preview=False,
                    )
                except Exception as ep:
                    await xnxx.edit(f"`{ep}`")

    elif replied:
        xnxx = await edit_or_reply(replied, "`Downloading`")
        dl = await replied.download_media()
        link = replied.link
        if len(event.text.split()) < 2:
            RESOLUSI = 720
        else:
            pq = event.text.split(maxsplit=1)[1]
            RESOLUSI = int(pq)
        if replied.video or replied.document:
            songname = "Telegram Video Player..."
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
            await xnxx.edit(
                f"📺 **Video Ditambahkan Ke antrian »** `#{pos}`\n\n👣 **Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👤 **Atas permintaan:** {from_user}"
            )
        else:
            if RESOLUSI == 360:
                hmmm = LowQualityVideo()
            elif RESOLUSI == 480:
                hmmm = MediumQualityVideo()
            elif RESOLUSI == 720:
                hmmm = HighQualityVideo()
            await call_py.join_group_call(
                chat_id,
                AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                stream_type=StreamType().pulse_stream,
            )
            add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
            await xnxx.edit(
                f"👣 **Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👥 **Status:** `Sedang Memutar Video`\n👤 **Atas permintaan:** {from_user}",
                link_preview=False,
            )
    else:
        xnxx = await edit_or_reply(event, "`⏳Searching ...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit("**Tidak Menemukan Video untuk Keyword yang Diberikan**")
        else:
            songname = search[0]
            url = search[1]
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                await xnxx.edit(
                    f"📺 **Video Ditambahkan Ke antrian »** `#{pos}`\n\n👣 **Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👤 **Atas permintaan:** {from_user}"
                )
            else:
                try:
                    await call_py.join_group_call(
                        chat_id,
                        AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    await xnxx.edit(
                        f"👣 **Judul:** [{songname}]({url})\n**🫂 Chat ID:** `{chat_id}`\n👥 **Status:** `Sedang Memutar Video`\n👤 **Atas permintaan:** {from_user}",
                        link_preview=False,
                    )
                except Exception as ep:
                    await xnxx.edit(f"`{ep}`")


@register(outgoing=True, pattern="^.leave(?: |$)(.*)")
async def vc_leave(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await edit_or_reply(event, "**Menghentikan Streaming**")
        except Exception as e:
            await edit_or_reply(event, f"**ERROR:** `{e}`")
    else:
        await edit_or_reply(event, "**Tidak Sedang Memutar Streaming**")


@register(outgoing=True, pattern="^.skip(?: |$)(.*)")
async def vc_skip(event):
    chat_id = event.chat_id
    if len(event.text.split()) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await edit_or_reply(event, "**Tidak Sedang Memutar Streaming**")
        elif op == 1:
            await edit_or_reply(
                event, "`Antrian Kosong, Meninggalkan Obrolan Suara...`"
            )
        else:
            await edit_or_reply(
                event,
                f"**⏭ Melewati Lagu**\n**🎧 Sekarang Memutar** - [{op[0]}]({op[1]})",
                link_preview=False,
            )
    else:
        skip = event.text.split(maxsplit=1)[1]
        DELQUE = "**Menghapus Lagu Berikut Dari Antrian:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x != 0:
                    hm = await skip_item(chat_id, x)
                    if hm != 0:
                        DELQUE = DELQUE + "\n" + f"**#{x}** - {hm}"
            await event.edit(DELQUE)


@register(outgoing=True, pattern="^.pause(?: |$)(.*)")
async def vc_pause(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await edit_or_reply(event, "**Streaming Dijeda**")
        except Exception as e:
            await edit_or_reply(event, f"**ERROR:** `{e}`")
    else:
        await edit_or_reply(event, "**Tidak Sedang Memutar Streaming**")


@register(outgoing=True, pattern="^.resume(?: |$)(.*)")
async def vc_resume(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await edit_or_reply(event, "**Streaming Dilanjutkan**")
        except Exception as e:
            await edit_or_reply(event, f"**ERROR:** `{e}`")
    else:
        await edit_or_reply(event, "**Tidak Sedang Memutar Streaming**")


@register(outgoing=True, pattern="^.playlist(?: |$)(.*)")
async def vc_playlist(event):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await edit_or_reply(
                event,
                f"**🎧 Sedang Memutar:**\n• [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`",
                link_preview=False,
            )
        else:
            PLAYLIST = f"**🎧 Sedang Memutar:**\n**• [{chat_queue[0][0]}]({chat_queue[0][2]})** | `{chat_queue[0][3]}` \n\n**• Daftaf Putar:**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                PLAYLIST = PLAYLIST + "\n" + \
                    f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`"
            await edit_or_reply(event, PLAYLIST, link_preview=False)
    else:
        await edit_or_reply(event, "**Tidak Sedang Memutar Streaming**")


@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)


CMD_HELP.update(
    {
        "vcplugin":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.play` <Judul Lagu/Link YT>\
        \nPenggunaan: Untuk Memutar Lagu di voice chat group dengan akun kamu\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vplay` <Judul Video/Link YT>\
        \nPenggunaan: Untuk Memutar Video di voice chat group dengan akun kamu\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.end`\
        \nPenggunaan: Untuk Memberhentikan video/lagu yang sedang putar di voice chat group\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.skip`\
        \n\nPenggunaan: Untuk Melewati video/lagu yang sedang di putar\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pause`\
        \nPenggunaan: Untuk memberhentikan video/lagu yang sedang diputar\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.resume`\
        \nPenggunaan: Untuk melanjutkan pemutaran video/lagu yang sedang diputar\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.playlist`\
        \nPenggunaan: Untuk menampilkan daftar putar Lagu/Video\
    "
    }
)
