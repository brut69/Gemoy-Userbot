# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import asyncio
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register
from platform import uname

modules = CMD_HELP

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**`Perintah Tidak Ditemukan, Harap Ketik Perintah Dengan Benar`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ☻ "
        await event.edit("⟢ 𝙂 𝙀 𝙈 𝙊 𝙔  -  𝙐 𝙎 𝙀 𝙍 𝘽 𝙊 𝙏 ⟣\n\n"
                         f"👤 𝗢𝗪𝗡𝗘𝗥 {DEFAULTUSER}\n📂 𝗣𝗟𝗨𝗚𝗜𝗡𝗦 {len(modules)}\n"
                         "🛠️ 𝙁𝙊𝙇𝙇𝙊𝙒𝙄𝙉𝙂 𝙊𝙍𝘿𝙀𝙍𝙎 𝘼𝙑𝘼𝙄𝙇𝘼𝘽𝙇𝙀\n"
                         f"☻{string}\n\n")
        await asyncio.sleep(6)
        await event.reply(f"\n**𝘊𝘰𝘯𝘵𝘰𝘩** : Ketik `.help ping` Untuk Informasi Pengunaan.\nAtau Ketik `.helpme` Untuk Menu Lainnya.")
        await asyncio.sleep(1000)
        await event.delete()
