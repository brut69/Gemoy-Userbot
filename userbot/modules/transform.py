# Authored by @Khrisna_Singhal
# Ported from Userge by Alfiananda P.A

import os
import random
import numpy as np
from colour import Color
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image, ImageOps, ImageDraw, ImageFont
from telethon.tl.types import DocumentAttributeFilename

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register

bground = "black"


@register(outgoing=True, pattern=r"^\.(ascii|asciis)$")
async def ascii(event):
    if not event.reply_to_msg_id:
        await event.edit("`Balas ke Media apa pun..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`reply to a image/sticker/video`")
        return
    await event.edit("`Mengunduh Media..`")
    if reply_message.photo:
        IMG = await bot.download_media(
            reply_message,
            "ascii.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "ASCII.tgs",
        )
        os.system("lottie_convert.py ASCII.tgs ascii.png")
        IMG = "ascii.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "ascii.mp4",
        )
        extractMetadata(createParser(video))
        os.system("ffmpeg -i ascii.mp4 -vframes 1 -an -s 480x360 -ss 1 ascii.png")
        IMG = "ascii.png"
    else:
        IMG = await bot.download_media(
            reply_message,
            "ascii.png",
        )
    try:
        await event.edit("`Pengolahan..`")
        list = await random_color()
        color1 = list[0]
        color2 = list[1]
        bgcolor = bground
        await asciiart(IMG, color1, color2, bgcolor)
        cmd = event.pattern_match.group(1)
        if cmd == "asciis":
            os.system("cp ascii.png ascii.webp")
            ascii_file = "ascii.webp"
        else:
            ascii_file = "ascii.png"
        await event.client.send_file(
            event.chat_id,
            ascii_file,
            force_document=False,
            reply_to=event.reply_to_msg_id,
        )
        await event.delete()
        os.system("rm *.png")
        os.system("rm *.webp")
        os.system("rm *.mp4")
        os.system("rm *.tgs")
    except BaseException as e:
        os.system("rm *.png")
        os.system("rm *.webp")
        os.system("rm *.mp4")
        os.system("rm *.tgs")
        return await event.edit(str(e))


async def asciiart(IMG, color1, color2, bgcolor):
    chars = np.asarray(list(" .,:irs?@9B&#"))
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height / letter_width
    img = Image.open(IMG)
    widthByLetter = round(img.size[0] * 0.15 * WCF)
    heightByLetter = round(img.size[1] * 0.15)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img / img.max()) ** 2.2 * (chars.size - 1)
    lines = ("\n".join(("".join(r)
                        for r in chars[img.astype(int)]))).split("\n")
    nbins = len(lines)
    colorRange = list(Color(color1).range_to(Color(color2), nbins))
    newImg_width = letter_width * widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)
    leftpadding = 0
    y = 0
    lineIdx = 0
    for line in lines:
        color = colorRange[lineIdx]
        lineIdx += 1
        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height
    IMG = newImg.save("ascii.png")
    return IMG


# this is from userge
async def random_color():
    color = [
        "#" + "".join([random.choice("0123456789ABCDEF") for k in range(6)])
        for i in range(2)
    ]
    return color


@register(outgoing=True, pattern=r"^\.asciibg(?: |$)(.*)")
async def _(event):
    BG = event.pattern_match.group(1)
    if BG.isnumeric():
        return await event.edit("`Harap masukkan warna bukan angka!`")
    elif BG:
        global bground
        bground = BG
    else:
        return await event.edit("`silakan masukkan bg dari ascii`")
    await event.edit(f"`Berhasil menyetel bg ascii ke` **{BG}**")


Converted = TEMP_DOWNLOAD_DIRECTORY + "sticker.webp"


@register(outgoing=True, pattern=r"^\.(mirror|flip|ghost|bw|poster)$")
async def transform(event):
    if not event.reply_to_msg_id:
        await event.edit("`Balas ke Media apa pun..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`membalas gambar/stiker`")
        return
    await event.edit("`Mengunduh Media..`")
    if reply_message.photo:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        os.system("lottie_convert.py transform.tgs transform.png")
        transform = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        os.system(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        transform = "transform.png"
    else:
        transform = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        await event.edit("`Mengubah media ini..`")
        cmd = event.pattern_match.group(1)
        im = Image.open(transform).convert("RGB")
        if cmd == "mirror":
            IMG = ImageOps.mirror(im)
        elif cmd == "flip":
            IMG = ImageOps.flip(im)
        elif cmd == "ghost":
            IMG = ImageOps.invert(im)
        elif cmd == "bw":
            IMG = ImageOps.grayscale(im)
        elif cmd == "poster":
            IMG = ImageOps.posterize(im, 2)
        IMG.save(Converted, quality=95)
        await event.client.send_file(
            event.chat_id, Converted, reply_to=event.reply_to_msg_id
        )
        await event.delete()
        os.system("rm -rf *.mp4")
        os.system("rm -rf *.tgs")
        os.remove(transform)
        os.remove(Converted)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.rotate(?: |$)(.*)")
async def rotate(event):
    if not event.reply_to_msg_id:
        await event.edit("`Balas ke media apa pun..`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("`membalas gambar/stiker`")
        return
    await event.edit("`Mengunduh Media..`")
    if reply_message.photo:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    elif (
        DocumentAttributeFilename(file_name="AnimatedSticker.tgs")
        in reply_message.media.document.attributes
    ):
        await bot.download_media(
            reply_message,
            "transform.tgs",
        )
        os.system("lottie_convert.py transform.tgs transform.png")
        rotate = "transform.png"
    elif reply_message.video:
        video = await bot.download_media(
            reply_message,
            "transform.mp4",
        )
        extractMetadata(createParser(video))
        os.system(
            "ffmpeg -i transform.mp4 -vframes 1 -an -s 480x360 -ss 1 transform.png"
        )
        rotate = "transform.png"
    else:
        rotate = await bot.download_media(
            reply_message,
            "transform.png",
        )
    try:
        value = int(event.pattern_match.group(1))
        if value > 360:
            raise ValueError
    except ValueError:
        value = 90
    await event.edit("`Memutar media Anda..`")
    im = Image.open(rotate).convert("RGB")
    IMG = im.rotate(value, expand=1)
    IMG.save(Converted, quality=95)
    await event.client.send_file(
        event.chat_id, Converted, reply_to=event.reply_to_msg_id
    )
    await event.delete()
    os.system("rm -rf *.mp4")
    os.system("rm -rf *.tgs")
    os.remove(rotate)
    os.remove(Converted)


CMD_HELP.update(
    {
        "transform": ">`.ghost`"
        "\nUsage: Tingkatkan citramu menjadi hantu!."
        "\n\n>`.ascii`"
        "\nUsage: membuat seni ascii dari media"
        "\n\n>`.asciis`"
        "\nUsage: sama tetapi unggah hasil sebagai stiker"
        "\n\n>`.asciibg <color>`"
        "\nUsage: Sekarang untuk menggunakan modul ASCII, ubah warna latar belakang pertama melewati"
        "\n\n>`.flip`"
        "\nUsage: Untuk membalik gambar Anda"
        "\n\n>`.mirror`"
        "\nUsage: Untuk mencerminkan gambar Anda"
        "\n\n>`.bw`"
        "\nUsage: Untuk Mengubah gambar berwarna Anda menjadi gambar b/w!"
        "\n\n>`.poster`"
        "\nUsage: Untuk posterisasi gambar Anda!"
        "\n\n>`.rotate <value>`"
        "\nUsage: Untuk memutar gambar Anda\n* Nilainya berkisar 1-360 jika tidak maka akan memberikan nilai default yaitu 90"
    }
)
