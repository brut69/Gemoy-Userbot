# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the LicenseLicense
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


""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /Â¯ )")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ ")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â€¢Â´")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â€¢Â´\n            \\              (")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â€¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â€¢Â´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await pong.edit(f"**❕𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏❕**… "
                    f"\n%sms` \n"
                    f"📢 𝙼𝚢 𝚂𝚎𝚗𝚜𝚎𝚒 : "
                    f"\n`{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝘔𝘦𝘮𝘶𝘭𝘢𝘪 𝘛𝘦𝘴𝘵 𝘍𝘪𝘴𝘪𝘬**")
    await asyncio.sleep(1)
    await pong.edit("__𝙂𝘼𝙈𝙊𝙉_________________")
    await pong.edit("___________𝙐𝙎𝙀𝙍𝘽𝙊𝙏_______")
    await asyncio.sleep(1)
    await pong.edit("`0%     ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    await pong.edit("`4%     █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    await pong.edit("`8%     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    await pong.edit("`36%   █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
    await pong.edit("`52%   █████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
    await pong.edit("`88%.  █████████████████████▒▒▒▒ `")
    await pong.edit("`100% █████████████████████████ `")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await pong.edit(f"**❕𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 𝘗𝘐𝘕𝘎𝘌𝘙❕**\n"
                    f"✨ 𝙿𝚒𝚗𝚐𝚎𝚛 : "
                    f"`%sms` \n"
                    f"🟢 𝙾𝚗𝚕𝚒𝚗𝚎 : "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.mping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`......`")
    await pong.edit("`........`")
    await pong.edit("`...𝙂.....`")
    await pong.edit("`...𝙂𝘼.....`")
    await pong.edit("`...𝙂𝘼𝙈.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉.......`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊.....`")
    await pong.edit("`...𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏.....`")
    await asyncio.sleep(1)
    await pong.edit("🌟")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await asyncio.sleep(1)
    await pong.edit(f"❕🧑‍💻 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧑‍💻 ❕\n"
                    f"✨ 𝙿𝚒𝚗𝚐𝚎𝚛 : "
                    f"`%sms` \n"
                    f"⏰ 𝚂𝚒𝚜𝚊 𝚆𝚊𝚔𝚝𝚞: "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("🎮")
    await asyncio.sleep(2)
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 ___________________🚒`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _________________🚒__`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _______________🚒____`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _____________🚒______`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 ___________🚒________`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _________🚒__________`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _______🚒____________`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 _____🚒______________`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽 ___🚒________________`")
    await pong.edit("`𝙳𝙸𝙽 𝙳𝙸𝙽⚡____________________`")
    await pong.edit("🔥")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await asyncio.sleep(2)
    await pong.edit(f"🚦𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏🚦 \n"
                    f"🤒 𝙺𝚎𝚜𝚎𝚑𝚊𝚝𝚊𝚗 : "
                    f"`%sms` \n"
                    f"🤕 𝙿𝚎𝚛𝚊𝚠𝚊𝚝𝚊𝚗 𝚍𝚊𝚕??𝚖 : "
                    f"`{uptime}` \n"
                    f"😷 𝙿𝚊𝚜𝚒𝚎𝚗 𝚁𝚊𝚠𝚊𝚝 𝙹𝚊𝚕𝚊𝚗 : `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("𝘔𝘦𝘮𝘶𝘭𝘢𝘪 𝘛𝘦𝘴𝘵 𝘒𝘦𝘤𝘦𝘱𝘢𝘵𝘢𝘯 𝘑𝘢𝘳𝘪𝘯𝘨𝘢𝘯....")
    await asyncio.sleep(1)
    await pong.edit("𝘔𝘰𝘩𝘰𝘯 𝘔𝘦𝘯𝘶𝘯𝘨𝘨𝘶....")
    await asyncio.sleep(1)
    await pong.edit("⭐")
    await asyncio.sleep(1)
    await pong.edit("🌟")
    await asyncio.sleep(1)
    await pong.edit("✨")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await pong.edit(f"🧑‍💻 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🧑‍💻 \n"
                    f"⚡ 𝚂𝚒𝚐𝚗𝚊𝚕 𝚂𝚝𝚛𝚎𝚗𝚐 : "
                    f"`%sms` \n"
                    f"⏰ 𝙳𝚞𝚛𝚊𝚜𝚒 𝙺𝚎𝚌𝚎𝚙𝚊𝚝𝚊𝚗 : "
                    f"`{uptime}` \n"
                    f"👤 𝙼𝚊𝚜𝚝𝚎𝚛 : `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil jaringan:\n**"
                   "✧**Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f"**━━━━━━━━━━━━━━━━━**\n\n"
                   "✧**Download :** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧**Upload :** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧**Ping :** "
                   f"`{result['ping']}` \n"
                   "✧**ISP :** "
                   f"`{result['client']['isp']}` \n"
                   "✧**BOT:** 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n\n"
                   f"**━━━━━━━━━━━━━━━━━** ")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`𝘗𝘖𝘕𝘎____________🚶`")
    await pong.edit("`𝘗𝘖𝘕𝘎___________🚶_`")
    await pong.edit("`𝘗𝘖𝘕𝘎__________🏃__`")
    await pong.edit("`𝘗𝘖𝘕𝘎_________🏃___`")
    await pong.edit("`𝘗𝘖𝘕𝘎________⛹️____`")
    await pong.edit("`𝘗𝘖𝘕𝘎_______⛹️_____`")
    await pong.edit("`𝘗𝘖𝘕𝘎______🤾______`")
    await pong.edit("`𝘗𝘖𝘕𝘎_____🤾_______`")
    await pong.edit("`𝘗𝘖𝘕𝘎____⛹️________`")
    await pong.edit("`𝘗𝘖𝘕𝘎___⛹️_________`")
    await pong.edit("`𝘗𝘖𝘕𝘎__🤾__________`")
    await pong.edit("`𝘗𝘖𝘕𝘎_🤸___________`")
    end = datetime.now()
    duration = (end - start).microseconds / 10000
    await asyncio.sleep(1)
    await pong.edit("⭐")
    await asyncio.sleep(2)
    await pong.edit("✨ 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 \n`%sms`" % (duration))


@register(outgoing=True, pattern="^.kping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("📢 𝙏𝙊𝙏𝙏...")
    await pong.edit("📢 𝙏𝙊𝙊𝙏𝙏...")
    await pong.edit("💦 𝘾𝙍𝙊𝙊𝙏𝙏...")
    await pong.edit("💦💦 𝙉𝙂𝙀𝙉...𝙏𝙊𝙊𝙏𝙏...")
    await pong.edit("🥵🥵🥵 𝙈𝙄𝙎𝙄 𝙈𝘼𝙐 𝙉𝙂𝙀𝙉𝙏𝙊𝙊𝙏𝙏...")
    await asyncio.sleep(1)
    await pong.edit("8==𝗗")
    await pong.edit("8====𝗗")
    await pong.edit("8=====𝗗")
    await pong.edit("8======𝗗")
    await pong.edit("8========𝗗")
    await pong.edit("8==========𝗗")
    await pong.edit("👉👈")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✨ 𝙆𝙊𝙉𝙏𝙊𝙇 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 !!** \n**🤏 𝙿𝙰𝙽𝙹𝙰𝙽𝙶 𝚂𝙸 𝙺𝙾𝙽𝚃𝙾𝙻𝙻** : `%sms`\n**🥵 𝙳𝚄𝚁𝙰𝚂𝙸 𝙼𝙰𝙸𝙽 𝙺𝙾𝙽𝚃𝙾𝙻𝙻** : `{uptime}`\n**🤤 𝙴𝙼𝙿𝚄 𝙽𝚈𝙰 𝙺𝙾𝙽𝚃𝙾𝙻𝙻** :`{ALIVE_NAME}`" % (duration))


CMD_HELP.update({
    "ping":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` | `.kping` | `.lping` | `.mping` | `.pings` | `.sping`\
         \nPenggunaan: Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.speed`\
         \nPenggunaan: Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \nPenggunaan: Sama Seperti Perintah Ping."})
