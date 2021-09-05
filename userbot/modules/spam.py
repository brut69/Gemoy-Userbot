# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

import asyncio
from asyncio import sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.cspam (.*)")
async def tmeme(e):
    cspam = str(e.pattern_match.group(1))
    message = cspam.replace(" ", "")
    await e.delete()
    for letter in message:
        await e.respond(letter)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#CSPAM\n"
            "TSpam berhasil dieksekusi")


@register(outgoing=True, pattern="^.wspam (.*)")
async def tmeme(e):
    wspam = str(e.pattern_match.group(1))
    message = wspam.split()
    await e.delete()
    for word in message:
        await e.respond(word)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#WSPAM\n"
            "WSpam berhasil dieksekusi")


@register(outgoing=True, pattern="^.spam (.*)")
async def spammer(e):
    counter = int(e.pattern_match.group(1).split(' ', 1)[0])
    spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
    await e.delete()
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    if BOTLOG:
        await e.client.send_message(BOTLOG_CHATID, "#SPAM\n"
                                    "Spam berhasil dieksekusi")


@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    message = e.text
    text = message.split()
    counter = int(text[1])
    link = str(text[2])
    await e.delete()
    for _ in range(1, counter):
        await e.client.send_file(e.chat_id, link)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#PICSPAM\n"
            "PicSpam berhasil dieksekusi")


@register(outgoing=True, pattern="^.delayspam (.*)")
async def spammer(e):
    spamDelay = float(e.pattern_match.group(1).split(' ', 2)[0])
    counter = int(e.pattern_match.group(1).split(' ', 2)[1])
    spam_message = str(e.pattern_match.group(1).split(' ', 2)[2])
    await e.delete()
    for _ in range(1, counter):
        await e.respond(spam_message)
        await sleep(spamDelay)
    if BOTLOG:
        await e.client.send_message(
            BOTLOG_CHATID, "#DelaySPAM\n"
            "DelaySpam berhasil dieksekusi")


CMD_HELP.update({
    "`spammer`": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cspam` <text>\
\nPenggunaan: Spam teks huruf demi huruf.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.spam` <count> <text>\
\nPenggunaan: Membanjiri teks dalam obrolan !!\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.wspam` <text>\
\nPenggunaan: Spam teks kata demi kata.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.picspam` <count> <tautan ke gambar/gif>\
\nPenggunaan: Seolah SMS spam saja tidak cukup!!\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.delayspam` <tunda> <hitung> <teks>\
\nPenggunaan: `.bigspam` tetapi dengan penundaan khusus.\
\n\n**NOTE**: `Spam dengan risiko Anda sendiri!!`"
})
