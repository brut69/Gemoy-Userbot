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


from userbot.events import register
from time import sleep


@register(outgoing=True, pattern='^.gemoy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Hai Perkenalkan Namaku 𝙂𝘼𝙈𝙊𝙉 𝙐𝙎𝙀𝙍𝘽𝙊𝙏")
    sleep(2)
    await typew.edit("`Aku lahir karena emang mau lahir`")
    sleep(1)
    await typew.edit("`Usiaku sekarang masih beberapa bulan`")
    sleep(1)
    await typew.edit("`Aku cuma ingin banyak yang mengenalku disini`")
    sleep(1)
    await typew.edit("`Jika kalian ingin tahu banyak tentangku`")
    sleep(1)
    await typew.edit("`Atau kalian punya masukan`")
    sleep(1)
    await typew.edit("`Agar Userbot ini lebih mengerti kalian`")
    sleep(1)
    await typew.edit("`Kalian bisa menghubungi Pembuatku`")
    sleep(1)
    await typew.edit("`Salam Hangat semua`")
    sleep(1)
    await typew.edit("`#tag @dunottagme`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💟`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
