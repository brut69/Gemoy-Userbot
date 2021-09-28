# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
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


import os
import lyricsgenius

from userbot.events import register
from userbot import CMD_HELP, GENIUS, lastfm, LASTFM_USERNAME
from pylast import User

if GENIUS is not None:
    genius = lyricsgenius.Genius(GENIUS)


@register(outgoing=True, pattern="^.lyrics (?:(now)|(.*) - (.*))")
async def lyrics(lyric):
    await lyric.edit("`Mendapatkan informasi...`")
    if GENIUS is None:
        await lyric.edit(
            "`Berikan token akses jenius ke Heroku ConfigVars...`")
        return False
    if lyric.pattern_match.group(1) == "now":
        playing = User(LASTFM_USERNAME, lastfm).get_now_playing()
        if playing is None:
            await lyric.edit(
                "`Tidak ada informasi scrobbling lastfm saat ini...`"
            )
            return False
        artist = playing.get_artist()
        song = playing.get_title()
    else:
        artist = lyric.pattern_match.group(2)
        song = lyric.pattern_match.group(3)
    await lyric.edit(f"`Mencari lirik untuk {artist} - {song}...`")
    songs = genius.search_song(song, artist)
    if songs is None:
        await lyric.edit(f"`Lagu` **{artis} - {lagu}** `tidak ditemukan...`")
        return False
    if len(songs.lyrics) > 4096:
        await lyric.edit("`Lirik terlalu besar, lihat file untuk melihatnya.`")
        with open("lyrics.txt", "w+") as f:
            f.write(f"Kueri penelusuran: \n{artis} - {song}\n\n{songs.lyrics}")
        await lyric.client.send_file(
            lyric.chat_id,
            "lyrics.txt",
            reply_to=lyric.id,
        )
        os.remove("lyrics.txt")
        return True
    else:
        await lyric.edit(
            f"**Permintaan pencarian**:\n`{artist}` - `{song}`"
            f"\n\n```{songs.lyrics}```"
        )
        return True


CMD_HELP.update({
    "lyrics":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lyrics` <nama artis> <nama lagu>"
    "\nPenggunaan: Dapatkan lirik yang cocok dengan artis dan lagu."
    "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lyrics now`"
    "\nPenggunaan: Dapatkan artis lirik dan lagu dari scrobbling lastfm saat ini."
})
