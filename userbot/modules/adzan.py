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


import json
import requests
from userbot import CMD_HELP
from userbot.events import register

PLACE = ""


@register(pattern=r"^\.adzan(?: |$)(.*)")
async def get_adzan(adzan):
    if not adzan.pattern_match.group(1):
        LOCATION = PLACE
        if not LOCATION:
            await adzan.edit("`Harap Menentukan Kota Atau Negara.`")
            return
    else:
        LOCATION = adzan.pattern_match.group(1)

    # url = f'http://muslimsalat.com/{LOCATION}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    url = f"https://api.pray.zone/v2/times/today.json?city={LOCATION}"
    request = requests.get(url)
    if request.status_code == 500:
        return await adzan.edit(f"**Tidak Dapat Menemukan Kota** `{LOCATION}`")

    parsed = json.loads(request.text)

    city = parsed["results"]["location"]["city"]
    country = parsed["results"]["location"]["country"]
    timezone = parsed["results"]["location"]["timezone"]
    date = parsed["results"]["datetime"][0]["date"]["gregorian"]

    imsak = parsed["results"]["datetime"][0]["times"]["Imsak"]
    subuh = parsed["results"]["datetime"][0]["times"]["Fajr"]
    zuhur = parsed["results"]["datetime"][0]["times"]["Dhuhr"]
    ashar = parsed["results"]["datetime"][0]["times"]["Asr"]
    maghrib = parsed["results"]["datetime"][0]["times"]["Maghrib"]
    isya = parsed["results"]["datetime"][0]["times"]["Isha"]

    result = (
        f"**Jadwal Sholat**:\n"
        f"📅 `{date} | {timezone}`\n"
        f"🌏 `{city} | {country}`\n\n"
        f"**Imsak :** `{imsak}`\n"
        f"**Subuh :** `{subuh}`\n"
        f"**Zuhur :** `{zuhur}`\n"
        f"**Ashar :** `{ashar}`\n"
        f"**Maghrib :** `{maghrib}`\n"
        f"**Isya :** `{isya}`\n"
    )

    await adzan.edit(result)


CMD_HELP.update({"adzan": "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.adzan` <kota>"
                 "\nPenggunaan: Memberikan Informasi Waktu Sholat."})
