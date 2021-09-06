# Credits By @VckyouuBitch From Geez-Project
# Tolong Haragai ya:)
# Kalo emg Bisa Menghargai seseorang pasti pahamm la ya:)
# Credits © Geez - Projects

import os

import moviepy.editor as m

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.getaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("`Balas Ke Audio Saja..`")
        return
    await event.edit("`pengolahan...`")
    d = os.path.join("resources/extras", "ul.mp3")
    await event.edit("`Mengunduh... File Besar Membutuhkan Waktu..`")
    await event.client.download_media(ureply, d)
    await event.edit("`Selesai.. Sekarang balas video yang ingin Anda tambahkan Audio`")


@register(outgoing=True, pattern="^.addaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("`Balas Ke Gif/Video Di mana Anda ingin menambahkan audio.`")
        return
    xx = await event.edit("`pengolahan...`")
    ultt = await ureply.download_media()
    ls = os.listdir("resources/extras")
    z = "ul.mp3"
    x = "resources/extras/ul.mp3"
    if z not in ls:
        await event.edit("`Pertama, balas audio dengan .aw`")
        return
    video = m.VideoFileClip(ultt)
    audio = m.AudioFileClip(x)
    out = video.set_audio(audio)
    out.write_videofile("ok.mp4", fps=30)
    await event.client.send_file(
        event.chat_id,
        file="ok.mp4",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    os.remove("ok.mp4")
    os.remove(x)
    os.remove(ultt)
    await xx.delete()

CMD_HELP.update(
    {
        "getaudio": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getaudio`\
         \nPenggunaan: Unduh Audio Untuk memasukkan Video/Gif yang Anda inginkan..\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.addaudio`\
         \nPenggunaan: Ini akan menempatkan audio di atas ke video/gif yang dibalas.."
    }
)
