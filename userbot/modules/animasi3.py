# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
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


""" Userbot module for having some fun with people. """

import os
import urllib
import requests
from re import sub
from cowpy import cow
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint


from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, ALIVE_NAME
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================

TRUTH_STR = [
    "Menurutmu kemana kamu akan pergi?",
    "Hah? Apa? Apakah mereka lolos?",
    "ZZzzZZzz... Hah? Apa? Oh, hanya mereka lagi, lupakan.",
    "Kembali kesini!",
    "Tidak terlalu cepat...",
    "Awas ke dinding!",
    "Jangan tinggalkan aku sendiri dengan mereka !!",
    "Kamu lari, kamu mati.",
    "Bercanda, aku ada dimana-mana",
    "Kamu akan menyesali itu ...",
    "Kamu juga bisa mencoba /kickme, kudengar itu menyenangkan.",
    "Ganggu orang lain, tidak ada yang peduli.",
    "Kamu bisa lari, tapi kamu tidak bisa bersembunyi.",
    "Apakah hanya itu yang kamu punya?",
    "Saya di belakang Anda...",
    "Anda punya teman!",
    "Kita bisa melakukan ini dengan cara mudah, atau cara sulit.",
    "Anda tidak mengerti, bukan?",
    "Ya, sebaiknya kau lari!",
    "Tolong, ingatkan saya apakah saya peduli?",
    "Aku akan lari lebih cepat jika jadi kamu.",
    "Itu pasti droid yang kami cari.",
    "Semoga peluang selalu menguntungkan Anda.",
    "Kata-kata terakhir yang terkenal.",
    "Dan mereka menghilang selamanya, tidak pernah terlihat lagi.",
    "Oh, lihat aku! Saya sangat keren, saya bisa lari dari bot orang ini",
    "Ya ya, cukup ketuk /kickme.",
    "Ini, ambil cincin ini dan pergilah ke Mordor saat kamu melakukannya.",
    "Legenda mengatakan, mereka masih berjalan...",
    "Tidak seperti Harry Potter, orang tuamu tidak bisa melindungimu dariku.",
    "Ketakutan menyebabkan kemarahan. Kemarahan mengarah pada kebencian. Kebencian menyebabkan penderitaan. Jika Anda terus berlari dalam ketakutan, Anda mungkin"
    "jadilah Vader berikutnya.",
    "Beberapa kalkulasi nanti, saya telah memutuskan minat saya pada kejahatan Anda tepat 0.",
    "Legenda mengatakan, mereka masih berjalan.",
    "Teruskan, kami tidak yakin kami menginginkanmu di sini.",
    "Kamu seorang penyihir- Oh. Tunggu. Kamu bukan Harry, terus bergerak.",
    "JANGAN BERLARI DI SINI!",
    "Hasta la vista, sayang.",
    "Siapa yang membiarkan anjing keluar?",
    "Ini lucu, karena tidak ada yang peduli.",
    "Ah, sayang sekali, Aku suka yang itu.",
    "Terus terang, sayangku, aku tidak peduli.",
    "Milkshake saya membawa semua anak laki-laki ke halaman... Jadi lari lebih cepat!",
    "Anda tidak bisa MENANGANI kebenaran!",
    "Dahulu kala, di galaksi yang sangat jauh... Seseorang akan peduli tentang itu, Tapi sekarang tidak lagi.",
    "Hei, lihat mereka! Mereka lari dari palu yang tak terelakkan... Manis.",
    "Han menembak lebih dulu, Aku juga.",
    "Apa yang kamu kejar, kelinci putih?",
    "Seperti yang dikatakan The Doctor... LARI!",
]

DARE_STR = [
    "Menurutmu kemana kamu akan pergi?",
    "Hah? Apa? Apakah mereka lolos?",
    "ZZzzZZzz... Hah? Apa? Oh, hanya mereka lagi, lupakan.",
    "Kembali kesini!",
    "Tidak terlalu cepat...",
    "Awas ke dinding!",
    "Jangan tinggalkan aku sendiri dengan mereka !!",
    "Kamu lari, kamu mati.",
    "Bercanda, aku ada dimana-mana",
    "Kamu akan menyesali itu ...",
    "Kamu juga bisa mencoba /kickme, kudengar itu menyenangkan.",
    "Ganggu orang lain, tidak ada yang peduli.",
    "Kamu bisa lari, tapi kamu tidak bisa bersembunyi.",
    "Apakah hanya itu yang kamu punya?",
    "Saya di belakang Anda...",
    "Anda punya teman!",
    "Kita bisa melakukan ini dengan cara mudah, atau cara sulit.",
    "Anda tidak mengerti, bukan?",
    "Ya, sebaiknya kau lari!",
    "Tolong, ingatkan saya apakah saya peduli?",
    "Aku akan lari lebih cepat jika jadi kamu.",
    "Itu pasti droid yang kami cari.",
    "Semoga peluang selalu menguntungkan Anda.",
    "Kata-kata terakhir yang terkenal.",
    "Dan mereka menghilang selamanya, tidak pernah terlihat lagi.",
    "Oh, lihat aku! Saya sangat keren, saya bisa lari dari bot orang ini",
    "Ya ya, cukup ketuk /kickme.",
    "Ini, ambil cincin ini dan pergilah ke Mordor saat kamu melakukannya.",
    "Legenda mengatakan, mereka masih berjalan...",
    "Tidak seperti Harry Potter, orang tuamu tidak bisa melindungimu dariku.",
    "Ketakutan menyebabkan kemarahan. Kemarahan mengarah pada kebencian. Kebencian menyebabkan penderitaan. Jika Anda terus berlari dalam ketakutan, Anda mungkin"
    "jadilah Vader berikutnya.",
    "Beberapa kalkulasi nanti, saya telah memutuskan minat saya pada kejahatan Anda tepat 0.",
    "Legenda mengatakan, mereka masih berjalan.",
    "Teruskan, kami tidak yakin kami menginginkanmu di sini.",
    "Kamu seorang penyihir- Oh. Tunggu. Kamu bukan Harry, terus bergerak.",
    "JANGAN BERLARI DI SINI!",
    "Hasta la vista, sayang.",
    "Siapa yang membiarkan anjing keluar?",
    "Ini lucu, karena tidak ada yang peduli.",
    "Ah, sayang sekali, Aku suka yang itu.",
    "Terus terang, sayangku, aku tidak peduli.",
    "Milkshake saya membawa semua anak laki-laki ke halaman... Jadi lari lebih cepat!",
    "Anda tidak bisa MENANGANI kebenaran!",
    "Dahulu kala, di galaksi yang sangat jauh... Seseorang akan peduli tentang itu, Tapi sekarang tidak lagi.",
    "Hei, lihat mereka! Mereka lari dari palu yang tak terelakkan... Manis.",
    "Han menembak lebih dulu, Aku juga.",
    "Apa yang kamu kejar, kelinci putih?",
    "Seperti yang dikatakan The Doctor... LARI!",
]


SPILL_STR = [
    "Menurutmu kemana kamu akan pergi?",
    "Hah? Apa? Apakah mereka lolos?",
    "ZZzzZZzz... Hah? Apa? Oh, hanya mereka lagi, lupakan.",
    "Kembali kesini!",
    "Tidak terlalu cepat...",
    "Awas ke dinding!",
    "Jangan tinggalkan aku sendiri dengan mereka !!",
    "Kamu lari, kamu mati.",
    "Bercanda, aku ada dimana-mana",
    "Kamu akan menyesali itu ...",
    "Kamu juga bisa mencoba /kickme, kudengar itu menyenangkan.",
    "Ganggu orang lain, tidak ada yang peduli.",
    "Kamu bisa lari, tapi kamu tidak bisa bersembunyi.",
    "Apakah hanya itu yang kamu punya?",
    "Saya di belakang Anda...",
    "Anda punya teman!",
    "Kita bisa melakukan ini dengan cara mudah, atau cara sulit.",
    "Anda tidak mengerti, bukan?",
    "Ya, sebaiknya kau lari!",
    "Tolong, ingatkan saya apakah saya peduli?",
    "Aku akan lari lebih cepat jika jadi kamu.",
    "Itu pasti droid yang kami cari.",
    "Semoga peluang selalu menguntungkan Anda.",
    "Kata-kata terakhir yang terkenal.",
    "Dan mereka menghilang selamanya, tidak pernah terlihat lagi.",
    "Oh, lihat aku! Saya sangat keren, saya bisa lari dari bot orang ini",
    "Ya ya, cukup ketuk /kickme.",
    "Ini, ambil cincin ini dan pergilah ke Mordor saat kamu melakukannya.",
    "Legenda mengatakan, mereka masih berjalan...",
    "Tidak seperti Harry Potter, orang tuamu tidak bisa melindungimu dariku.",
    "Ketakutan menyebabkan kemarahan. Kemarahan mengarah pada kebencian. Kebencian menyebabkan penderitaan. Jika Anda terus berlari dalam ketakutan, Anda mungkin"
    "jadilah Vader berikutnya.",
    "Beberapa kalkulasi nanti, saya telah memutuskan minat saya pada kejahatan Anda tepat 0.",
    "Legenda mengatakan, mereka masih berjalan.",
    "Teruskan, kami tidak yakin kami menginginkanmu di sini.",
    "Kamu seorang penyihir- Oh. Tunggu. Kamu bukan Harry, terus bergerak.",
    "JANGAN BERLARI DI SINI!",
    "Hasta la vista, sayang.",
    "Siapa yang membiarkan anjing keluar?",
    "Ini lucu, karena tidak ada yang peduli.",
    "Ah, sayang sekali, Aku suka yang itu.",
    "Terus terang, sayangku, aku tidak peduli.",
    "Milkshake saya membawa semua anak laki-laki ke halaman... Jadi lari lebih cepat!",
    "Anda tidak bisa MENANGANI kebenaran!",
    "Dahulu kala, di galaksi yang sangat jauh... Seseorang akan peduli tentang itu, Tapi sekarang tidak lagi.",
    "Hei, lihat mereka! Mereka lari dari palu yang tak terelakkan... Manis.",
    "Han menembak lebih dulu, Aku juga.",
    "Apa yang kamu kejar, kelinci putih?",
    "Seperti yang dikatakan The Doctor... LARI!",
]


GAMBAR_LOV = """
╔══╗
╚╗╔╝
╔╝(¯v´¯)
╚══.¸./𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏)
"""

GAMBAR_KISSME = """
*Kiss*…….*Kiss*
*Kiss*…..*Kiss*
*Kiss*…*Kiss*
*Kiss**Kiss*
*Kiss*…*Kiss*
*Kiss*…..*Kiss*
*Kiss*…….*Kiss*
*Kiss*………*Kiss *

……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*
……..*Kiss*

………*Kiss*
…*Kiss*…*Kiss*
.*Kiss*…….*Kiss*
…*Kiss*……*Kiss *
……*Kiss*
………..*Kiss*
*Kiss*……*Kiss*
.*Kiss*…….*Kiss*
…*Kiss*…*Kiss*
…..……*Kiss*

………*Kiss*
…*Kiss*…*Kiss*
.*Kiss*…….*Kiss*
…*Kiss*……*Kiss *
……*Kiss*
………..*Kiss*
*Kiss*……*Kiss*
.*Kiss*…….*Kiss*
…*Kiss*…*Kiss*
……..…*Kiss
"""


GAMBAR_TENGKORAK = """
░░░░░░░░░░░░░▄▐░░░░
░░░░░░░▄▄▄░░▄██▄░░░
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█▄░░░░
░░░░░░░▐▌▀▄▀▄▀▐░░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░
"""

GAMBAR_LOPE = """
…..*..lovelovelo…*
…*..lovelovelove….*
..*.lovelovelovelove…*…………….*….*
.*..lovelovelovelovelo…*………*..lovel….*
...*..lovelovelovelovelove…*….*…lovelovelo.*
*.. lovelovelovelovelove…*….*…lovelovelo.*
.*..lovelovelovelovelove…*..*…lovelovelo…*
..*…lovelovelovelovelove..*…lovelovelo…*
…*….lovelovelolovelovelovelovelovelo…*
…..*….lovelovelovelovelovelovelov…*
……..*….lovelovelovelovelovelo…*
………..*….lovelovelovelove…*
……………*…lovelovelo….*
………………*..lovelo…*
…………………*…..*
………………….*..*
"""

GAMBAR_PAGI = """
 ^_^)
.................^v^
⋱ ⋮ ⋰
⋯ ◯ ⋯¨. ︵ ..............................................^v^
¨︵¸︵( ░░ )︵.︵.︵..............^v^
... (´░░░░░░ ') ░░░' )
´︶´¯︶´︶´︶´︶.....^v^..........^v^
....^v^....▄▀▀──▄▀▀▄─▄▀▀▄─█▀▄....^v^....
....^v^....█─▀█─█──█─█──█─█─█....^v^....
....^v^....─▀▀───▀▀───▀▀──▀▀─....^v^....
....^v^........^v^........^v^........^v^........^v^....
█▄─▄█─▄▀▀▄─█▀▄─█▄─█─█─█▄─█─▄▀▀─
█─▀─█─█──█─██▀─█─▀█─█─█─▀█─█─▀█
▀───▀──▀▀──▀─▀─▀──▀─▀─▀──▀──▀▀─
"""

# Create by @Ultdroid

GAMBAR_MLM = """
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█╔══╗╔══╗╔══╗╔══╗▀█
┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█
┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█
┌▀█╚══╝╚══╝╚══╝╚══╝▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█
┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█
┌▀█░░█░▌█▐█▐░▌░█░░░▀█
┌▀█░░░░░░░░░░░░░░░░▀█
┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
"""


GAMBAR_MALAM = """
       🌙.     *       ☄️
  🌟   .  *       .
                       *   .      🛰     .        ✨      *
  .     *   𝚂𝙻𝙴𝙴𝙿 𝚆𝙴𝙻𝙻         🚀
      .              . . 𝚂𝚆𝙴𝙴𝚃 𝙳𝚁𝙴𝙰𝙼𝚂 🌙
. *       🌏 𝗚𝗢𝗢𝗗 𝗡𝗜𝗚𝗛𝗧 ✨         *
                    🌙.     *       ☄️        .
🌟   .  *       .         ;          .        .
                       *   .      🛰     .        ✨      *
"""

# ===========================================


@register(outgoing=True, pattern=r"^\.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern=r"^\.coinflip (.*)")
async def coin(event):
    r = choice(["Kepala", "Ekor"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "Kepala":
        if input_str == "Kepala":
            await event.edit(
                "Koin Itu Mendarat Di: **Kepala**.\nKamu Benar.")
        elif input_str == "Ekor":
            await event.edit(
                "Koin Itu Mendarat Di: **Kepala**.\nKamu Salah, Coba Lagi..."
            )
        else:
            await event.edit("Koin Itu Mendarat Di: **Kepala**.")
    elif r == "Ekor":
        if input_str == "Ekor":
            await event.edit(
                "Koin Itu Mendarat Di: **Ekor**.\nKamu Benar.")
        elif input_str == "Kepala":
            await event.edit(
                "Koin Itu Mendarat Di: **Ekor**.\nKamu Salah, Coba Lagi..."
            )
        else:
            await event.edit("Koin Itu Mendarat Di: **Ekor**.")


@register(pattern=r"^\.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    """ slaps a user, or get slapped if not a reply. """
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Tidak bisa slap orang ini, perlu mengambil beberapa meteor dan batu!`"
        )


async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    slap_str = event.pattern_match.group(1)
    if slap_str == "en":
        temp = choice(SLAP_TEMPLATES_EN)
        item = choice(ITEMS_EN)
        hit = choice(HIT_EN)
        throw = choice(THROW_EN)
        where = choice(WHERE_EN)
    elif slap_str == "id":
        temp = choice(SLAP_TEMPLATES_ID)
        item = choice(ITEMS_ID)
        hit = choice(HIT_ID)
        throw = choice(THROW_ID)
        where = choice(WHERE_ID)
    elif slap_str == "jutsu":
        temp = choice(SLAP_TEMPLATES_Jutsu)
        item = choice(ITEMS_Jutsu)
        hit = choice(HIT_Jutsu)
        throw = choice(THROW_Jutsu)
        where = choice(WHERE_Jutsu)
    else:
        temp = choice(SLAP_TEMPLATES_EN)
        item = choice(ITEMS_EN)
        hit = choice(HIT_EN)
        throw = choice(THROW_EN)
        where = choice(WHERE_EN)

    caption = "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where)

    return caption


@register(outgoing=True, pattern=r"^\.boobs(?: |$)(.*)")
async def boobs(e):
    await e.edit("`Berdosa, Mendapatkan Gambar Boobs...`")
    await sleep(3)
    await e.edit("`Mengirim Gambar Boobs...`")
    nsfw = requests.get(
        'http://api.oboobs.ru/noise/1').json()[0]["Gambar Boobs"]
    urllib.request.urlretrieve(
        "http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'boobs.jpg')
    await e.client.send_file(e.chat_id, "boobs.jpg")
    os.remove("boobs.jpg")
    await e.delete()


@register(outgoing=True, pattern=r"^\.pantat(?: |$)(.*)")
async def butts(e):
    await e.edit("`Berdosa, Mendapatkan Gambar Pantat Yang Indah...`")
    await sleep(3)
    await e.edit("`Mengirim Gambar Pantat Indah...`")
    nsfw = requests.get(
        'http://api.obutts.ru/noise/1').json()[0]["Gambar Pantat"]
    urllib.request.urlretrieve(
        "http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'butts.jpg')
    await e.client.send_file(e.chat_id, "butts.jpg")
    os.remove("butts.jpg")
    await e.delete()


@register(outgoing=True, pattern=r"^\.(yes|no|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get(f"https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(event.chat_id,
                                    str(r["answer"]).upper(),
                                    reply_to=message_id,
                                    file=r["image"])


@register(outgoing=True, pattern=r"^\.fp$")
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern=r"^\.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    await e.edit(choice(CRI))


@register(outgoing=True, pattern=r"^\.insult$")
async def insult(e):
    """ I make you cry !! """
    await e.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern=r"^\.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await cp_e.edit("`😂🅱️AhHH👐MaNtAp👅Bro👅UnTuk✌️MeMbuAT👌Ku👐TeRliHat👀LuCu💞HaHAhaA!💦`")

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern=r"^\.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await vpr.edit("`B e r i k a n S e b u a h T e k s U n t u k Vａｐｏｒ！`")

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await stret.edit("`Beriiiiiiiiikaaannnn sebuuuuuuuuuah teeeeeeeks!`")

    count = randint(3, 10)
    reply_text = sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])", (r"\1" * count),
                     message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern=r"^\.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await zgfy.edit(
            "`b̜́ͨe͒͜r̠͂ͬi̷̱̋k͖͒ͤa̋ͫ͑n͕͂͗ t̢͘͟e͂̽̈́k͎͂͠s̤͚ͭ m̪͔͑è͜͡n͈ͮḁ͞ͅk̲̮͛u̺͂ͩt̬̗́k͍̙̮á ̺n̨̹ͪ`"
        )

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            rand = randint(0, 2)

            if rand == 0:
                charac = charac.strip() + \
                    choice(ZALG_LIST[0]).strip()
            elif rand == 1:
                charac = charac.strip() + \
                    choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + \
                    choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.hai$")
async def hoi(hello):
    """ Greet everyone! """
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern=r"^\.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await owo.edit("` Mohon Berikan Teks UwU! `")

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern=r"^\.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=r"^\.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(event):
	if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    truth = "@truthordaresbot"
    await event.edit()
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(truth, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Buka blokir @truthordaresbot dan coba lagi```")
            return
        if response.text.startswith(
                "**Maaf saya tidak bisa mendapatkan apa-apa dari **"):
            await event.edit("```Saya pikir ini bukan tautan yang benar```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)
            

@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(event):
	if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    dare = "@truthordaresbot"
    await event.edit()
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(dare, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Buka blokir @truthordaresbot dan coba lagi```")
            return
        if response.text.startswith(
                "**Maaf saya tidak bisa mendapatkan apa-apa dari **"):
            await event.edit("```Saya pikir ini bukan tautan yang benar```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)


@register(outgoing=True, pattern=r"^\.spill$")
async def spill(spill):
    """ Spill Suka-Suka Lu Aja !! """
    await spill.edit(choice(SPILL_STR))


@register(outgoing=True, pattern=r"^\.oem$")
async def oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\.Oem$")
async def Oem(e):
    t = "Oem"
    for j in range(16):
        t = t[:-1] + "em"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\.10iq$")
async def iqless(e):
    await e.edit("♿")


@register(outgoing=True, pattern="^.fuck$")
async def iqless(e):
    await e.edit("🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕")


@register(outgoing=True, pattern=r"^\.moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.bunga$")
async def moon(event):
    deq = deque(list("🌼🌻🌺🌹🌸🌷"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.waktu$")
async def moon(event):
    deq = deque(list("🎑🌄🌅🌇🌆🌃🌌"))
    try:
        for x in range(100):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.buah$")
async def moon(event):
    deq = deque(list("🍉🍓🍇🍎🍍🍐🍌"))
    try:
        for x in range(35):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.rain$")
async def rain(event):
    deq = deque(list("☀️🌤⛅️🌥☁️🌧⛈"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.love$")
async def love(event):
    deq = deque(list("❤️🧡💛💚💙💜🖤💕💞💓💗💖💘💝"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.earth$")
async def earth(event):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.hati$")
async def earth(event):
    deq = deque(list("🖤💜💙💚💛🧡❤️🤍"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.monyet$")
async def earth(event):
    deq = deque(list("🙈🙉🙈🙉🙈🙉🙈🙉"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern="^.emo$")
async def earth(event):
    deq = deque(list("🙂😁😄😃😂🤣😭🐵🙊🙉🙈"))
    try:
        for x in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await mock.edit("`bEriKan PeSan UnTuK MoCk!`")

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.weeb(?: |$)(.*)")
async def weebify(e):
    args = e.pattern_match.group(1)
    if not args:
        get = await e.get_reply_message()
        args = get.text
    if not args:
        await e.edit("`Apa Yang Anda Lakukan`")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await e.edit(string)


@register(outgoing=True, pattern=r"^\.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await memereview.edit("`Mohon Balas Ke Pesan Orang Yang Ingin Anda Puji ツ`")
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=r"^\.teksbiru$")
async def bluetext(bt_e):
    """ Believe me, you will find this useful. """
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/TEKSBIRU /APAKAH /ANDA.\n"
            "/SEDANG /GABUT /KARNA /TERTARIK /MELIHAT /TEKS /BIRU /PASTI /ANDA /BOSAN?")


@register(outgoing=True, pattern=r"^\.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8, paytext * 8, paytext * 2, paytext * 2, paytext * 2,
        paytext * 6, paytext * 6, paytext * 2, paytext * 2, paytext * 2,
        paytext * 2, paytext * 2)
    await event.edit(pay)


@register(outgoing=True, pattern=r"^\.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit("Ini Dia, Bantu Dirimu Sendiri."
                        f"\n[{query}]({r.json()['shorturl']})")


@register(outgoing=True, pattern=r"^\.hy$")
async def sayhi(e):
    await e.edit(
        "\n✨✨✨✨✨✨✨✨✨✨✨✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️❤️❤️❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️❤️❤️❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨✨✨✨✨✨✨✨✨✨✨✨")


@register(pattern=r".scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    """ Just a small command to fake chat actions for fun !! """
    options = [
        'mengetik', 'kontak', 'game', 'lokasi', 'suara', 'bulat', 'video',
        'foto', 'dokumen', 'batal'
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Tidak Valid`")
        return
    try:
        if (scam_time > 300):
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r".type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    """ Just a small command to make your keyboard become a typewriter! """
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await typew.edit("`Berikan Sebuah Teks Untuk Type!`")
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


@register(outgoing=True, pattern=r"^\.leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(f"`❗ {ALIVE_NAME} 𝚃𝚎𝚕𝚊𝚑 𝙼𝚎𝚗𝚒𝚗𝚐𝚐𝚊𝚕𝚔𝚊𝚗 𝙶𝚛𝚘𝚞𝚙...`")


@register(outgoing=True, pattern=r"^\.fail$")
async def fail(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `"
                     "`\n████▌▄▌▄▐▐▌█████ `"
                     "`\n████▌▄▌▄▐▐▌▀████ `"
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")


@register(outgoing=True, pattern=r"^\.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `"
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `"
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `")


@register(outgoing=True, pattern=r"^\.rock$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮┈┈┈┈┈┈┈┈┈┈┈┈ `"
                     "`\n┈┃┃┈╭╮┈┏╮╭╮╭╮┃╭ `"
                     "`\n┈┃┃┈┃┃┈┣┫┃┃┃┈┣┫ `"
                     "`\n┈┃┣┳┫┃┈┃╰╰╯╰╯┃╰ `"
                     "`\n╭┻┻┻┫┃┈┈╭╮┃┃━┳━ `"
                     "`\n┃╱╭━╯┃┈┈┃┃┃┃┈┃┈ `"
                     "`\n╰╮╱╱╱┃┈┈╰╯╰╯┈┃┈ `")


@register(outgoing=True, pattern=r"^\.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")


@register(outgoing=True, pattern=r"^\.stfu$")
async def stfu(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\\████████████████████████████████`"
                     "`\n██▀▀▀▀████▀▀▀▀████▀▀▀▀▀███▀▀██▀▀█`"
                     "`\n█──────██──────██───────██──██──█`"
                     "`\n█──██▄▄████──████──███▄▄██──██──█`"
                     "`\n█▄────▀████──████────█████──██──█`"
                     "`\n█▀▀██──████──████──███████──██──█`"
                     "`\n█──────████──████──███████──────█`"
                     "`\n██▄▄▄▄█████▄▄████▄▄████████▄▄▄▄██`"
                     "`\n█████████████████████████████████`"
                     )


@register(outgoing=True, pattern=r"^\.gtfo$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n███████████████████████████████ `"
                     "`\n█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█ `"
                     "`\n█───────█──────█───────█──────█ `"
                     "`\n█──███──███──███──███▄▄█──██──█ `"
                     "`\n█──███▄▄███──███─────███──██──█ `"
                     "`\n█──██───███──███──██████──██──█ `"
                     "`\n█──▀▀▀──███──███──██████──────█ `"
                     "`\n█▄▄▄▄▄▄▄███▄▄███▄▄██████▄▄▄▄▄▄█ `"
                     "`\n███████████████████████████████ `")


@register(outgoing=True, pattern=r"^\.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`"
                     "\n                    \n"
                     r"`(\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *𝗧𝗔𝗣𝗜 𝗕𝗢𝗢𝗡𝗚`")


@register(outgoing=True, pattern=r"^\.fag$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`"
                     "`\n█▄█████▄█`"
                     "`\n█▼▼▼▼▼`"
                     "`\n█       𝗥𝗔𝗔𝗔𝗔𝗔𝗪𝗥𝗥𝗥`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                     "`\n ██   ██`")


@register(outgoing=True, pattern=r"^\.tai$")
async def taco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\\__/}"
                     "\n(●_●)"
                     "\n( >💩 Mau PUP Ku?")


@register(outgoing=True, pattern=r"^\.paw$")
async def paw(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern=r"^\.tf$")
async def tf(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@register(outgoing=True, pattern=r"^\.gey$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈Lu Bau Hehe`"
                     "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


@register(outgoing=True, pattern=r"^\.gay$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈ANDA GAY`"
                     "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")


@register(outgoing=True, pattern=r"^\.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@register(outgoing=True, pattern=r"^\.hey$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@register(outgoing=True, pattern=r"^\.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
                     "`\n┗━━┻━┛`")


@register(outgoing=True, pattern=r"^\.iwi(?: |$)(.*)")
async def faces(siwis):
    """ IwI """
    textx = await siwis.get_reply_message()
    message = siwis.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await siwis.edit("` Anda Harus Memberikan Teks Ke IwI  `")
        return

    reply_text = sub(r"(a|i|u|e|o)", "i", message)
    reply_text = sub(r"(A|I|U|E|O)", "I", reply_text)
    reply_text = sub(r"\!+", " " + choice(IWIS), reply_text)
    reply_text += " " + choice(IWIS)
    await siwis.edit(reply_text)


@register(outgoing=True, pattern="^.koc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8===✊D💦")
        await e.edit("8==✊=D💦💦")
        await e.edit("8=✊==D💦💦💦")
        await e.edit("8✊===D💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦")
        await e.edit("8=✊==D💦💦💦💦💦💦💦")
        await e.edit("8✊===D💦💦💦💦💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
        await e.edit("8=✊==D Lah Kok Habis?")
        await e.edit("𝗧𝗢𝗕𝗔𝗧 𝗞𝗔 𝗧𝗢𝗕𝗔𝗧 😭😭😭😭")


@register(outgoing=True, pattern="^.gas$")
async def gas(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("___________________🚑")
        await e.edit("________________🚑___")
        await e.edit("______________🚑_____")
        await e.edit("___________🚑________")
        await e.edit("________🚑___________")
        await e.edit("_____🚑______________")
        await e.edit("__🚑_________________")
        await e.edit("🚑___________________")
        await e.edit("_____________________")
        await e.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=r"^\.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern=r"^\.(?:lov|lov)\s?(.)?")
async def emoji_lov(e):
    emoji = e.pattern_match.group(1)
    lov = GAMBAR_LOV
    if emoji:
        lov = lov.replace('🌟', emoji)
    await e.edit(lov)


@register(outgoing=True, pattern=r"^\.(?:lope|lope)\s?(.)?")
async def emoji_lope(e):
    emoji = e.pattern_match.group(1)
    lope = GAMBAR_LOPE
    if emoji:
        lope = lope.replace('😂', emoji)
    await e.edit(lope)


@register(outgoing=True, pattern=r"^\.(?:mlm|mlm)\s?(.)?")
async def emoji_mlm(e):
    emoji = e.pattern_match.group(1)
    mlm = GAMBAR_MLM
    if emoji:
        mlm = mlm.replace('🌟', emoji)
    await e.edit(mlm)


@register(outgoing=True, pattern=r"^\.(?:night|night)\s?(.)?")
async def emoji_night(e):
    emoji = e.pattern_match.group(1)
    night = GAMBAR_MALAM
    if emoji:
        night = night.replace('🌟', emoji)
    await e.edit(night)


@register(outgoing=True, pattern=r"^\.(?:pagi|pagi)\s?(.)?")
async def emoji_pagi(e):
    emoji = e.pattern_match.group(1)
    pagi = GAMBAR_PAGI
    if emoji:
        pagi = pagi.replace('😂', emoji)
    await e.edit(pagi)


@register(outgoing=True, pattern=r"^\.(?:kissme|kissme)\s?(.)?")
async def emoji_kissme(e):
    emoji = e.pattern_match.group(1)
    kissme = GAMBAR_KISSME
    if emoji:
        kissme = oke.replace('😂', emoji)
    await e.edit(kissme)


@register(outgoing=True, pattern=r"^\.(?:skull|skull)\s?(.)?")
async def emoji_skull(e):
    emoji = e.pattern_match.group(1)
    skull = GAMBAR_TENGKORAK
    if emoji:
        skull = skull.replace('😂', emoji)
    await e.edit(skull)


CMD_HELP.update({
    "animasi3":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cowsay`"
    "\nPenggunaan: sapi yang mengatakan sesuatu."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `cp`"
    "\nPenggunaan: Copy paste meme terkenal"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vapor`"
    "\nPenggunaan: Menguapkan semuanya!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.str`"
    "\nPenggunaan: Regangkan."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.10iq`"
    "\nPenggunaan: Kamu mundur !!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.zal`"
    "\nPenggunaan: Munculkan perasaan kacau."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.Oem`"
    "\nPenggunaan: Oeeeem"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fp`"
    "\nPenggunaan: Telapak Tangan:P"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.moon`"
    "\nPenggunaan: animasi bulan."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.clock`"
    "\nPenggunaan: animasi jam."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.hi`"
    "\nPenggunaan: Sapa semuanya!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.coinflip` <Kepala/Ekor>"
    "\nPenggunaan: Melempar koin !!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.owo`"
    "\nPenggunaan: UwU"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.react`"
    "\nPenggunaan: Buat Userbot Anda bereaksi terhadap semuanya."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.slap`"
    "\nPenggunaan: balas tampar mereka dengan benda acak !!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cry`"
    "\nPenggunaan: jika kamu melakukan ini, aku akan menangis."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shg`"
    "\nPenggunaan: Angkat bahu!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.run`"
    "\nPenggunaan: Biarkan Aku Lari, Lari, LARI!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.chase`"
    "\nPenggunaan: Sebaiknya Anda mulai berlari"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.metoo`"
    "\nPenggunaan: Haha ya"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mock`"
    "\nPenggunaan: Lakukan dan temukan kesenangan yang sesungguhnya."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.clap`"
    "\nPenggunaan: Puji orang!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.f` <emoji/karakter>"
    "\nPenggunaan: FU"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bt`"
    "\nPenggunaan: Percayalah, Anda akan menemukan ini berguna."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.weeb`"
    "\nPenggunaan: Untuk Mengubah Teks Menjadi Weeb-ify."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.type` <teks>"
    "\nPenggunaan: Hanya perintah kecil untuk membuat keyboard Anda menjadi mesin tik!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lfy` <query>"
    "\nPenggunaan: Biar saya Google itu untuk Anda dengan cepat!"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.decide` [Alternatif: (.yes, .no, .maybe)]"
    "\nPenggunaan: Buat keputusan cepat."
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙:  `.nou` `.bot` `.rock` `.gey` `.tf` `.paw` `.tai` `.nih`"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fag` `.gtfo`; `.stfu` `.lol` `.lool` `.fail` `.leave`"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.iwi` `.hy` `.koc` `.kissme` `.gas` `.earth` `.love` `.rain`"
    "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lope` `.lov` `.emo` `.fuck` `.skull`  `.monyet`\nPenggunaan: Explore sendiri weh"
})
