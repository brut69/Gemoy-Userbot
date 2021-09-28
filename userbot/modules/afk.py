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


""" Userbot module which contains afk-related commands """

from datetime import datetime
import time
from random import choice, randint

from telethon.events import StopPropagation
from telethon.tl.functions.account import UpdateProfileRequest

from userbot import (  # noqa pylint: disable=unused-import isort:skip
    AFKREASON,
    BOTLOG,
    BOTLOG_CHATID,
    CMD_HELP,
    ALIVE_NAME,
    COUNT_MSG,
    ISAFK,
    PM_AUTO_BAN,
    USERS,
    PM_AUTO_BAN,
    bot,
)
from userbot.events import register

# ========================= CONSTANTS ============================
AFKSTR = [
    f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞",
    f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞",
    f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞",
    f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞",
]


global USER_AFK  # pylint:disable=E0602
global afk_time  # pylint:disable=E0602
global afk_start
global afk_end
USER_AFK = {}
afk_time = None
afk_start = {}

# =================================================================


@register(outgoing=True, pattern="^.afk(?: |$)(.*)", disable_errors=True)
async def set_afk(afk_e):
    """ For .afk command, allows you to inform people that you are afk when they message you """
    message = afk_e.text  # pylint:disable=E0602
    string = afk_e.pattern_match.group(1)
    global ISAFK
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    global reason
    USER_AFK = {}
    afk_time = None
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if string:
        AFKREASON = string
        await afk_e.edit(f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞\n📢 𝘿𝙄𝙆𝘼𝙍𝙀𝙉𝘼𝙆𝘼𝙉 : {AFKREASON}")
    else:
        await afk_e.edit("🔴 𝘼 𝙁 𝙆\n📢 𝙅𝘼𝙉𝙂 𝘿𝙄𝘾𝘼𝙍𝙄\n")
    if user.last_name:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name=user.last_name))
    else:
        await afk_e.client(UpdateProfileRequest(first_name=user.first_name, last_name=user.last_name))
    if BOTLOG:
        await afk_e.client.send_message(BOTLOG_CHATID, "💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n**🔴 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞 🔴**")
    ISAFK = True
    afk_time = datetime.now()  # pylint:disable=E0602
    raise StopPropagation


@register(outgoing=True)
async def type_afk_is_not_true(notafk):
    """ This sets your status as not afk automatically when you write something while being afk """
    global ISAFK
    global COUNT_MSG
    global USERS
    global AFKREASON
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    last = user.last_name
    if last and last.endswith("🔴 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞 🔴"):
        last1 = last[:-12]
    else:
        last1 = ""
    back_alive = datetime.now()
    afk_end = back_alive.replace(microsecond=0)
    if ISAFK:
        ISAFK = False
        msg = await notafk.respond("𝙃𝙀𝙈𝘽𝙇𝙊...👋\n𝙄𝙈 𝘽𝘼𝘾𝙆 🟢 𝙊𝙉𝙇𝙄𝙉𝙀 🟢")
        time.sleep(3)
        await msg.delete()
        await notafk.client(UpdateProfileRequest(first_name=user.first_name, last_name=last1))
        if BOTLOG:
            await notafk.client.send_message(
                BOTLOG_CHATID,
                "`Anda Mendapatkan`" + str(COUNT_MSG) + "`Pesan Dari`" +
                str(len(USERS)) + "`Obrolan Saat Anda 🔴 𝗔𝗙𝗞`",
            )
            for i in USERS:
                name = await notafk.client.get_entity(i)
                name0 = str(name.first_name)
                await notafk.client.send_message(
                    BOTLOG_CHATID,
                    "[" + name0 + "](tg://user?id=" + str(i) + ")" +
                    " Mengirim Mu " + "`" + str(USERS[i]) + " Pesan`",
                )
        COUNT_MSG = 0
        USERS = {}
        AFKREASON = None


@register(incoming=True, disable_edited=True)
async def mention_afk(mention):
    """ This function takes care of notifying the people who mention you that you are AFK."""
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Terakhir Aktif**"
    if mention.message.mentioned and not (await mention.get_sender()).bot:
        if ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if mention.sender_id not in USERS:
                if AFKREASON:
                    await mention.reply(f"🔴 𝘼 𝙁 𝙆\n⏰ {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞\n⏰ 𝗦𝗘𝗝𝗔𝗞: {afk_since}\n📢 𝘿𝙄𝙆𝘼𝙍𝙀𝙉𝘼𝙆𝘼𝙉: {AFKREASON}")
                else:
                    await mention.reply(str(choice(AFKSTR)))
                USERS.update({mention.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif mention.sender_id in USERS:
                if USERS[mention.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await mention.reply(f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞\n⏰ 𝗦𝗘𝗝𝗔𝗞: {afk_since}\n📢 𝘿𝙄𝙆𝘼𝙍𝙀𝙉𝘼𝙆𝘼𝙉: {AFKREASON}")
                    else:
                        await mention.reply(str(choice(AFKSTR)))
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[mention.sender_id] = USERS[mention.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


@register(incoming=True, disable_errors=True)
async def afk_on_pm(sender):
    """ Function which informs people that you are AFK in PM """
    global ISAFK
    global USERS
    global COUNT_MSG
    global COUNT_MSG
    global USERS
    global ISAFK
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global afk_start
    global afk_end
    user = await bot.get_me()  # pylint:disable=E0602
    back_alivee = datetime.now()
    afk_end = back_alivee.replace(microsecond=0)
    afk_since = "**Belum Lama**"
    if sender.is_private and sender.sender_id != 777000 and not (
            await sender.get_sender()).bot:
        if PM_AUTO_BAN:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
                apprv = is_approved(sender.sender_id)
            except AttributeError:
                apprv = True
        else:
            apprv = True
        if apprv and ISAFK:
            now = datetime.now()
            datime_since_afk = now - afk_time  # pylint:disable=E0602
            time = float(datime_since_afk.seconds)
            days = time // (24 * 3600)
            time = time % (24 * 3600)
            hours = time // 3600
            time %= 3600
            minutes = time // 60
            time %= 60
            seconds = time
            if days == 1:
                afk_since = "**Kemarin**"
            elif days > 1:
                if days > 6:
                    date = now + \
                        datetime.timedelta(
                            days=-days, hours=-hours, minutes=-minutes)
                    afk_since = date.strftime("%A, %Y %B %m, %H:%I")
                else:
                    wday = now + datetime.timedelta(days=-days)
                    afk_since = wday.strftime('%A')
            elif hours > 1:
                afk_since = f"`{int(hours)} Jam {int(minutes)} Menit`"
            elif minutes > 0:
                afk_since = f"`{int(minutes)} Menit {int(seconds)} Detik`"
            else:
                afk_since = f"`{int(seconds)} Detik`"
            if sender.sender_id not in USERS:
                if AFKREASON:
                    await sender.reply(f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞\n⏰ 𝗦𝗘𝗝𝗔𝗞: {afk_since}\n📢 𝘿𝙄𝙆𝘼𝙍𝙀𝙉𝘼𝙆𝘼𝙉: {AFKREASON}")
                else:
                    await sender.reply(str(choice(AFKSTR)))
                USERS.update({sender.sender_id: 1})
                COUNT_MSG = COUNT_MSG + 1
            elif apprv and sender.sender_id in USERS:
                if USERS[sender.sender_id] % randint(2, 4) == 0:
                    if AFKREASON:
                        await sender.reply(f"💌 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏\n👤 {ALIVE_NAME} 𝗦𝗘𝗗𝗔𝗡𝗚 𝗔𝗙𝗞\n⏰ 𝗦𝗘𝗝𝗔𝗞: {afk_since}\n📢 𝘿𝙄𝙆𝘼𝙍𝙀𝙉𝘼𝙆𝘼𝙉: {AFKREASON}")
                    else:
                        await sender.reply(str(choice(AFKSTR)))
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1
                else:
                    USERS[sender.sender_id] = USERS[sender.sender_id] + 1
                    COUNT_MSG = COUNT_MSG + 1


CMD_HELP.update({
    "afk":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.afk` <reason>\
\nPenggunaan: Lakukan ketika ingin OFF.\nSiapapun Yang Balas, Tag, Atau Chat Kamu \
Mereka Akan Tau Alasan Kamu OFF.\n\nAFK Bisa Dilakukan Dan Dibatalkan Dimanapun.\
"
})
