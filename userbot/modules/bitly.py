# Copyright (C) 2020 azrim.
# All rights reserved.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from bitlyshortener import Shortener
from re import match
from userbot import CMD_HELP, BITLY_TOKEN, BOTLOG, BOTLOG_CHATID
from userbot.events import register


@register(outgoing=True, pattern=r"^\.bitly(?: |$)(.*)")
async def shortener(short):
    """
        Shorten link using bit.ly API
    """
    if BITLY_TOKEN is not None:
        token = [f'{BITLY_TOKEN}']
        reply = await short.get_reply_message()
        message = short.pattern_match.group(1)
        if message:
            pass
        elif reply:
            message = reply.text
        else:
            await short.edit("`Error! No URL given!`")
            return
        link_match = match(r'\bhttps?://.*\.\S+', message)
        if not link_match:
            await short.edit("`Kesalahan! Harap berikan url yang valid!`\ncontoh: https://google.com")
            return
        urls = [f'{message}']
        bitly = Shortener(tokens=token, max_cache_size=8192)
        raw_output = bitly.shorten_urls(urls)
        string_output = f"{raw_output}"
        output = string_output.replace("['", "").replace("']", "")
        await short.edit(f"`Tautan Anda berhasil dipersingkat!`\nIni tautan Anda {output}")
        if BOTLOG:
            await short.client.send_message(BOTLOG_CHATID, f"`#SHORTLINK \\Ini Tautan Anda!`\\dan {output}")
    else:
        await short.edit("Setel token API bit.ly terlebih dahulu\nDapatkan dari [di sini](https://bitly.com/a/sign_up)")


CMD_HELP.update(
    {
        "bytly": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bytly` <URL>"
        "\nPenggunaan: Tautkan URL ke byt.ly ads.
        "
    })
