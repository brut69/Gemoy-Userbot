#credits: mrconfused
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


from geopy.geocoders import Nominatim
from telethon.tl import types
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern="^.gps(?: |$)(.*)")
async def gps(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    input_str = event.pattern_match.group(1)

    if not input_str:
        return await event.edit("`Mohon Berikan Tempat Yang Dicari`")

    await event.edit("`Menemukan Lokasi Ini Di Server Map....`")

    geolocator = Nominatim(user_agent="Geez")
    geoloc = geolocator.geocode(input_str)

    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(
                    lat, lon
                )
            )
        )
        await event.delete()
    else:
        await event.edit("`Saya Tidak Dapat Menemukannya`")

CMD_HELP.update({
    "gps":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gps`"
    "\nPenggunaan: Untuk Mendapatkan Lokasi Map"
})
