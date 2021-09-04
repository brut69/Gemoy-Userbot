# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
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
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**𝘛𝘌𝘚𝘛 𝘗𝘐𝘕𝘎𝘌𝘙**… "
                    f"\n%sms` \n"
                    f"𝖬𝗒 𝖴𝗌𝖾𝗋"
                    f"\n`{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝘔𝘦𝘮𝘶𝘭𝘢𝘪 𝘛𝘦𝘴𝘵 𝘍𝘪𝘴𝘪𝘬**")
    await pong.edit("__**...𝙂𝙀𝙈𝙊𝙔...**__")
    await pong.edit("__**.....𝙐𝙎𝙀𝙍𝘽𝙊𝙏.....**__")
    await asyncio.sleep(1)
    await pong.edit("__**......𝖲𝖤𝖫𝖠𝖫𝖴 𝖲𝖠𝖡𝖠𝖱......**__")
    await pong.edit("**0% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**20% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**40% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**60% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**80% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**100% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**–  𝙂𝙀𝙈𝙊𝙔 𝘗𝘐𝘕𝘎𝘌𝘙  –**\n"
                    f"𝘗𝘐𝘕𝘎 : "
                    f"`%sms` \n"
                    f"𝘖𝘯𝘭𝘪𝘯𝘦 : "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`...𝙂.....`")
    await pong.edit("`...𝙂𝙀.....`")
    await pong.edit("`...𝙂𝙀𝙈.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 .....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊.....`")
    await pong.edit("`...𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏.....`")
    await pong.edit("`🤪`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await asyncio.sleep(0.1)
    await pong.edit(f"𝙂𝙀𝙈𝙊𝙔 **𝘗𝘖𝘕𝘎 !**\n"
                    f"𝘗𝘐𝘕𝘎"
                    f"`%sms` \n"
                    f"𝘚𝘐𝘚𝘈 𝘞𝘈𝘒𝘛𝘜"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await asyncio.sleep(0.1)
    await pong.edit("**0% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**20% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**40% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**60% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**80% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    await pong.edit("**100% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await asyncio.sleep(1)
    await pong.edit(f"- 𝙂 𝙀 𝙈 𝙊 𝙔 -\n"
                    f"**sinyal  :** "
                    f"`%sms` \n"
                    f"**i'm online  :** "
                    f"`{uptime}` \n"
                    f"**User :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝘔𝘦𝘮𝘶𝘭𝘢𝘪 𝘊𝘩𝘦𝘤𝘬 𝘒𝘢𝘯𝘵𝘰𝘯𝘨**")
    await pong.edit("**𝘗𝘭𝘦𝘢𝘴𝘦 𝘞𝘢𝘪𝘵 𝘧𝘰𝘳 ...**")
    await asyncio.sleep(0.1)
    await pong.edit("🙄")
    await asyncio.sleep(0.1)
    await pong.edit("🤔")
    await asyncio.sleep(0.1)
    await pong.edit("😏")
    await asyncio.sleep(0.1)
    await pong.edit("😤")
    await asyncio.sleep(0.1)
    await pong.edit("😡")
    await asyncio.sleep(0.1)
    await pong.edit("🤬")
    await asyncio.sleep(0.1)
    await pong.edit("🤪")
    await asyncio.sleep(0.1)
    await pong.edit("😂")
    await asyncio.sleep(0.1)
    await pong.edit("🤣")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**😭 𝙂𝙀𝙈𝙊𝙔 - 𝙐𝙎𝙀𝙍𝘽𝙊𝙏**\n"
                    f"**💰 𝘚𝘐𝘚𝘈 𝘚𝘈𝘓𝘋𝘖 :** "
                    f"`%sms` \n"
                    f"**😭 𝘏𝘈𝘉𝘐𝘚 𝘋𝘈𝘓𝘈𝘔 :** "
                    f"`{uptime}` \n"
                    f"**🏧 𝘙𝘌𝘒𝘌𝘕𝘐𝘕𝘎 𝘈/𝘕 :** `{ALIVE_NAME}`" % (duration))


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
                   "✧**BOT:** 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n\n"
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
    await pong.edit("`𝘗𝘖𝘕𝘎...........🚶`")
    await pong.edit("`𝘗𝘖𝘕𝘎..........🚶.`")
    await pong.edit("`𝘗𝘖𝘕𝘎.........🏃..`")
    await pong.edit("`𝘗𝘖𝘕𝘎........🏃...`")
    await pong.edit("`𝘗𝘖𝘕𝘎.......⛹️....`")
    await pong.edit("`𝘗𝘖𝘕𝘎......⛹️.....`")
    await pong.edit("`𝘗𝘖𝘕𝘎.....🤾......`")
    await pong.edit("`𝘗𝘖𝘕𝘎....🤾.......`")
    await pong.edit("`𝘗𝘖𝘕𝘎...⛹️........`")
    await pong.edit("`𝘗𝘖𝘕𝘎..⛹️.........`")
    await pong.edit("`𝘗𝘖𝘕𝘎.🤾..........`")
    await pong.edit("`𝘗𝘖𝘕𝘎🤸...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await asyncio.sleep(1)
    await pong.edit("🤪 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 **𝘗𝘖𝘕𝘎 !**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` | `.lping` | `.xping` | `.pings` | `.sping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."})
