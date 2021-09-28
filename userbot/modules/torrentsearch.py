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

import codecs
import json
import os

import requests
from bs4 import BeautifulSoup as bs

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register


@register(outgoing=True, pattern=r"^\.ts (.*)")
async def gengkapak(e):
    await e.edit("`Harap tunggu, mengambil hasil...`")
    query = e.pattern_match.group(1)
    response = requests.get(
        f"https://sjprojectsapi.herokuapp.com/torrent/?query={query}"
    )
    ts = json.loads(response.text)
    if ts != response.json():
        await e.edit("**Terjadi beberapa kesalahan**\n`Coba Lagi Nanti`")
        return
    listdata = ""
    run = 0
    while True:
        try:
            run += 1
            r1 = ts[run]
            list1 = "<-----{}----->\nName: {}\nSeeders: {}\nSize: {}\nAge: {}\n<--Magnet Below-->\n{}\n\n\n".format(
                run, r1["name"], r1["seeder"], r1["size"], r1["age"], r1["magnet"])
            listdata += list1
        except BaseException:
            break

    if not listdata:
        return await e.edit("`Kesalahan: Tidak ada hasil yang ditemukan`")

    tsfileloc = f"{TEMP_DOWNLOAD_DIRECTORY}/{query}.txt"
    with open(tsfileloc, "w+", encoding="utf8") as out_file:
        out_file.write(str(listdata))
    fd = codecs.open(tsfileloc, "r", encoding="utf-8")
    data = fd.read()
    key = (requests.post("https://nekobin.com/api/documents",
                         json={"content": data}) .json() .get("result") .get("key"))
    url = f"https://nekobin.com/raw/{key}"
    caption = (
        f"`Berikut hasil kueri: {query}`\n\nDitempel to: [Nekobin]({url})"
    )
    os.remove(tsfileloc)
    await e.edit(caption, link_preview=False)


def dogbin(magnets):
    counter = 0
    urls = []
    while counter != len(magnets):
        message = magnets[counter]
        url = "https://del.dog/documents"
        r = requests.post(url, data=message.encode("UTF-8")).json()
        url = f"https://del.dog/raw/{r['key']}"
        urls.append(url)
        counter += 1
    return urls


@register(outgoing=True, pattern=r"^\.tos(?: |$)(.*)")
async def tor_search(event):
    if event.fwd_from:
        return
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    search_str = event.pattern_match.group(1)

    print(search_str)
    await event.edit("Mencari " + search_str + ".....")
    if " " in search_str:
        search_str = search_str.replace(" ", "+")
        print(search_str)
        res = requests.get(
            "https://www.torrentdownloads.me/search/?new=1&s_cat=0&search="
            + search_str,
            headers,
        )

    else:
        res = requests.get(
            "https://www.torrentdownloads.me/search/?search=" +
            search_str,
            headers)

    source = bs(res.text, "lxml")
    urls = []
    magnets = []
    titles = []
    counter = 0
    for div in source.find_all("div", {"class": "grey_bar3 back_none"}):
        # print("https://www.torrentdownloads.me"+a['href'])
        try:
            title = div.p.a["title"]
            title = title[20:]
            titles.append(title)
            urls.append("https://www.torrentdownloads.me" + div.p.a["href"])
        except KeyError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
        if counter == 11:
            break
        counter += 1
    if not urls:
        await event.edit("Entah Kata Kunci dibatasi atau tidak ditemukan..")
        return

    print("Found URLS...")
    for url in urls:
        res = requests.get(url, headers)
        # print("URl: "+url)
        source = bs(res.text, "lxml")
        for div in source.find_all("div", {"class": "grey_bar1 back_none"}):
            try:
                mg = div.p.a["href"]
                magnets.append(mg)
            except Exception:
                pass
    print("Menemukan Magnet...")
    shorted_links = dogbin(magnets)
    print("Magnet mantap ke del.dog...")
    msg = ""
    try:
        search_str = search_str.replace("+", " ")
    except BaseException:
        pass
    msg = "**Torrent Search Query**\n`{}`".format(
        search_str) + "\n**Results**\n"
    counter = 0
    while counter != len(titles):
        msg = (
            msg
            + "⁍ [{}]".format(titles[counter])
            + "({})".format(shorted_links[counter])
            + "\n\n"
        )
        counter += 1
    await event.edit(msg, link_preview=False)


CMD_HELP.update(
    {
        "torrent": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ts` <permintaan pencarian>"
        "\nPenggunaan: Telusuri kueri torrent dan poskan ke dogbin."
        "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.tos` <permintaan pencarian>"
        "\nPenggunaan: Cari magnet torrent dari kueri."
    }
)
