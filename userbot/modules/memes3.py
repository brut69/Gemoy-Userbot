

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("AING DI GHOSTING")
        sleep(2)
        await e.edit("😭😭😭")
        sleep(2)
        await e.edit("AING SETESS")
        sleep(1)
        await e.edit("KENAPA COBAK")
        sleep(1)
        await e.edit("JADIAN CUMA JADI PELAMPIASAN")
        sleep(1)
        await e.edit("CUMA JADI BADUT")
        sleep(1)
        await e.edit("DAH SENENG KAU TINGGAL")
        sleep(1)
        await e.edit("GITU AJA KAN?")
        sleep(1)
        await e.edit("DEMI APASI")
        sleep(1)
        await e.edit("KAU")
        sleep(1)
        await e.edit("TEGA")
        sleep(1)
        await e.edit("HANCURIN")
        sleep(1)
        await e.edit("APA YANG UDAH")
        sleep(1)
        await e.edit("KITA")
        sleep(1)
        await e.edit("BANGUN")
        sleep(1)
        await e.edit("🤧🤧🤧")
        sleep(1)
        await e.edit("DEMI APA COBA?")
        sleep(1)
        await e.edit("COBA JELASIN")
        sleep(1)
        await e.edit("APA YANG BUAT KAU")
        sleep(1)
        await e.edit("TEGA LAKUIN SEMUA INI")
        sleep(1)
        await e.edit("APA..?? 😠😠")
        sleep(1)
        await e.edit("KENAPA..?? 😡😡")
        sleep(1)
        await e.edit("ATAU ADA SIAPA..?? 🤬🤬")
        sleep(1)
        await e.edit("😭😭😭😭")
        sleep(1)
        await e.edit("ADA YG MAU SAMA AKU TAK 👉👈")
        sleep(3)
        await e.edit("PLISS DAH...🥺🥺")
        sleep(1)
        await e.edit("SESEORANG YG MAU NERIMA AKU")
        sleep(1)
        await e.edit("😔😔😔😔")
        sleep(1)
        await e.edit("MAU GAK JADI TEMEN HIDUPKU?")
        sleep(1)
        await e.edit("**🤪𝗧𝗔𝗣𝗜 𝗕𝗢𝗢𝗡𝗚🤪**")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *NIH GUA KASIH BUAT MU!!`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *E G DENG, UDH DI KSH GRATIS NTAR KAU RUSAKIN`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  -PARAH`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "story":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi Wajib  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ GOBLOK   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "**Skuy kenalin Dev 𝙂𝙀𝙈𝙊𝙔-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 dulu yook**"
            "**Yusuf mungkin terkenalnya. Nama lain untuk di Dev 𝙍𝙊𝙈 adalah @brut69 dari 𝙍𝘼𝙎𝙏𝘼𝙈𝙊𝘿69™**"
            "**Mo kepoin lebih lanjut sabi sih**"
            "**Silakan PM ke @dunottagme or @jsminebot**"
            "**Untuk bot Music yang bisa dipakai sabi @RemMusic_bot @RinMusicOS_bot @CallMusicPlusBot ©²¹**"
            "**Gitu aja sih. Lebih detailnya silakan PM aje. Bhahaha**"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

CMD_HELP.update({
    "memes2":
    "`.nah` ; `.huh` ; `.owner`\
    \nUsage: cobain.\
    \n\n`.bunga` ; `.buah`\
    \nUsage: animasi.\
    \n\n`.waktu`\
    \nUsage: animasi."
})

CMD_HELP.update({
    "memes3":
    "`.hua`\
    \nUsage: nangis.\
    \n\n`.cinta` ; `.canda`\
    \nUsage: liat sendiri"
})
