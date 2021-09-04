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
            await event.edit("**`Command Tidak Ditemukan, Harap Ketik Command Dengan Benar`**")
            await asyncio.sleep(200)
            await event.delete()
    else:
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`\t ✿  "
        await event.edit("** 𝙂 𝙀 𝙈 𝙊 𝙔  -  𝙐 𝙎 𝙀 𝙍 𝘽 𝙊 𝙏 **\n\n"
                         f"**✿ 𝗢𝗪𝗡𝗘𝗥 {DEFAULTUSER}**\n**✿ 𝗣𝗟𝗨𝗚𝗜𝗡𝗦 : {len(modules)}**\n\n"
                         "**• 𝗢𝗨𝗥 𝗠𝗘𝗡𝗨 :**\n"
                         f"✿ {string}✿\n\n")
        await event.reply(f"\n**Contoh** : Ketik <`.help ping`> Untuk Informasi Pengunaan.\nAtau Bisa Juga Ketik `.helpme` Untuk Menu Yang Lainnya.")
        await asyncio.sleep(1000)
        await event.delete()
