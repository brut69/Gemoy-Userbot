# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

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
    await pong.edit(f"ã€  __Test__ **PING** __|â”|âŽ†__ ãƒ… "
                    f"\n  â˜ž `%sms` \n"
                    f"ã€  __My__ **User** __|â”|âŽ†__ ãƒ… "
                    f"\n  â˜ž `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("ðŸ”¥")
    await pong.edit("__**...ðŸ’ 𝙂𝙀𝙈𝙊𝙔ðŸ’ ...**__")
    await pong.edit("__**.....𝙐𝙎𝙀𝙍𝘽𝙊𝙏.....**__")
    await pong.edit("__**......𝖲𝖤𝖫𝖠𝖫𝖴 𝖲𝖠𝖡𝖠𝖱......**__")
    await pong.edit("**0% â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’**")
    await pong.edit("**20% â–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’**")
    await pong.edit("**40% â–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’**")
    await pong.edit("**60% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’**")
    await pong.edit("**80% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’**")
    await pong.edit("**100% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**â•°â”â–  𝙂𝙀𝙈𝙊𝙔 𝘗𝘐𝘕𝘎𝘌𝘙 â–â”â•¯**\n"
                    f"â˜ž __ping:__ "
                    f"`%sms` \n"
                    f"â˜ž __i'm online:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`.....ðŸ”¥𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏ðŸ”¥.....`")
    await pong.edit("`ðŸ”¥`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"â€¢âŽšâ€¢ âŽ† 𝙂𝙀𝙈𝙊𝙔 **𝘗𝘖𝘕𝘎 !**\n"
                    f"â˜ž  𝘗𝘐𝘕𝘎"
                    f"`%sms` \n"
                    f"â˜ž  𝘚𝘐𝘚𝘈 𝘞𝘈𝘒𝘛𝘜"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’**")
    await pong.edit("**20% â–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’**")
    await pong.edit("**40% â–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’**")
    await pong.edit("**60% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’**")
    await pong.edit("**80% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’**")
    await pong.edit("**100% â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"- 𝙂 𝙀 𝙈 𝙊 𝙔 -\n"
                    f"**â˜ž sinyal  :** "
                    f"`%sms` \n"
                    f"**â˜ž i'm online  :** "
                    f"`{uptime}` \n"
                    f"__|â”|âŽ†__ **User :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**𝘔𝘦𝘮𝘶𝘭𝘢𝘪 𝘊𝘩𝘦𝘤𝘬 𝘒𝘢𝘯𝘵𝘰𝘯𝘨**")
    await pong.edit("**𝘗𝘭𝘦𝘢𝘴𝘦 𝘞𝘢𝘪𝘵 𝘧𝘰𝘳 ...🙄🤔**")
    await pong.edit("🤨")
    await pong.edit("🧐")
    await pong.edit("😒")
    await pong.edit("😠")
    await pong.edit("😤")
    await pong.edit("😡")
    await pong.edit("🤬")
    await pong.edit("🤪")
    await pong.edit("😂")
    await pong.edit("**𝘽𝙝𝙖𝙖𝙠𝙨🤣**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"å**𝘗𝘐𝘕𝘎 𝘗𝘖𝘕𝘎 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏**å\n"
                    f"â•âŽ† **𝘗𝘐𝘕𝘎:** "
                    f"`%sms` \n"
                    f"â•âŽ† **𝘚𝘐𝘚𝘈 𝘋𝘜𝘐𝘛:** "
                    f"`{uptime}` \n"
                    f"**âœ âž² 𝘋𝘰𝘮𝘱𝘦𝘵:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...🤗`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil jaringan:\n**"
                   "ðŸ›  **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\n\n"
                   "âœ§ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "âœ§ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "âœ§ **Ping:** "
                   f"`{result['ping']}` \n"
                   "âœ§ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "âœ§ **BOT:** ð™ƒð™šð™­ð™­ð™–-ð™ð™Žð™€ð™ð˜½ð™Šð™ðŸ”¥\n\n"
                   f" â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â” ")


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
    await pong.edit("`𝘗𝘖𝘕𝘎...........ðŸ”¥`")
    await pong.edit("`𝘗𝘖𝘕𝘎..........ðŸ”¥.`")
    await pong.edit("`𝘗𝘖𝘕𝘎.........ðŸ”¥..`")
    await pong.edit("`𝘗𝘖𝘕𝘎........ðŸ”¥...`")
    await pong.edit("`𝘗𝘖𝘕𝘎.......ðŸ”¥....`")
    await pong.edit("`𝘗𝘖𝘕𝘎......ðŸ”¥.....`")
    await pong.edit("`𝘗𝘖𝘕𝘎.....ðŸ”¥......`")
    await pong.edit("`𝘗𝘖𝘕𝘎....ðŸ”¥.......`")
    await pong.edit("`𝘗𝘖𝘕𝘎...ðŸ”¥........`")
    await pong.edit("`𝘗𝘖𝘕𝘎..ðŸ”¥.........`")
    await pong.edit("`𝘗𝘖𝘕𝘎.ðŸ”¥..........`")
    await pong.edit("`𝘗𝘖𝘕𝘎ðŸ”¥...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("âŽšâŽ† 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 **𝘗𝘐𝘕𝘎 𝘗𝘖𝘕𝘎 !**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` | `.lping` | `.xping` | `.pings` | `.sping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."})
