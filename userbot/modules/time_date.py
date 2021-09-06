# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting the date
    and time of any country or the userbot server.  """

from datetime import datetime as dt

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from userbot import CMD_HELP, COUNTRY, TZ_NUMBER
from userbot.events import register


async def get_tz(con):
    """ Dapatkan zona waktu negara tertentu. """
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace(
            "Kepulauan Terluar Kecil",
            "pulau-pulau kecil terluar")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@register(outgoing=True, pattern="^.time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def time_func(tdata):
    """ Untuk perintah .time, kembalikan waktu
        1. Negara disahkan sebagai argumen,
        2. Negara userbot default (atur dengan menggunakan .settime),
        3. Server tempat userbot berjalan.
    """
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)

    t_form = "%H:%M"
    c_name = None

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await tdata.edit(f"`Ini` **{dt.now().strftime(t_form)}** `di sini.`")
        return

    if not timezones:
        await tdata.edit("`Negara tidak valid.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} memiliki beberapa zona waktu:`\n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Pilih salah satu dengan mengetikkan angka "
            return_str += "dalam perintah.`\n"
            return_str += f"`Contoh: .time {c_name} 2`"

            await tdata.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(t_form)

    if c_name != COUNTRY:
        await tdata.edit(
            f"`Dia`  **{dtnow}**  `di dalam {c_name}({time_zone} timezone).`")
        return

    elif COUNTRY:
        await tdata.edit(f"`Dia`  **{dtnow}**  `disini {COUNTRY}"
                         f"({time_zone} timezone).`")
        return


@register(outgoing=True, pattern="^.date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def date_func(dat):
    """ Untuk perintah .date, kembalikan tanggal
        1. Negara disahkan sebagai argumen,
        2. Negara userbot default (atur dengan menggunakan .settime),
        3. Server tempat userbot berjalan.
    """
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)

    d_form = "%d/%m/%y - %A"
    c_name = ''

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await dat.edit(f"`Dia`  **{dt.now().strftime(d_form)}**  `di sini.`")
        return

    if not timezones:
        await dat.edit("`Negara tidak valid.`")
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"`{c_name} memiliki beberapa zona waktu:`\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Pilih salah satu dengan mengetikkan angka "
            return_str += "dalam perintah.`\n"
            return_str += f"Contoh: .date {c_name} 2"

            await dat.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(d_form)

    if c_name != COUNTRY:
        await dat.edit(
            f"`Dia`  **{dtnow}**  `di dalam {c_name}({time_zone} timezone).`")
        return

    elif COUNTRY:
        await dat.edit(f"`Dia`  **{dtnow}**  `disini {COUNTRY}"
                       f"({time_zone} timezone).`")
        return


CMD_HELP.update({
    "timedate":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.time` <nama/kode negara> <nomor zona waktu>\
\nPenggunaan: Dapatkan waktu suatu negara.\nJika suatu negara memiliki beberapa zona waktu\nsemua zona waktu akan dicantumkan dan Anda dapat memilih salah satu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.date` <nama/kode negara> <nomor zona waktu>\
\nPenggunaan: Dapatkan tanggal suatu negara. Jika suatu negara memiliki beberapa zona waktu\nitu akan mencantumkan semuanya dan membiarkan Anda memilih satu."
})
