# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# The entire source code is OSSRPL except 'sed' which is GPLv3
# License: GPLv3 and OSSRPLOSSRPL
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


""" Userbot command for sed. """

import re
from sre_constants import error as sre_err
from userbot import CMD_HELP
from userbot.events import register

DELIMITERS = ("/", ":", "|", "_")


async def separate_sed(sed_string):
    """ Separate sed arguments. """

    if len(sed_string) < 2:
        return

    if (len(sed_string) >= 2 and sed_string[2] in DELIMITERS
            and sed_string.count(sed_string[2]) >= 2):
        delim = sed_string[2]
        start = counter = 3
        while counter < len(sed_string):
            if sed_string[counter] == "\\":
                counter += 1

            elif sed_string[counter] == delim:
                replace = sed_string[start:counter]
                counter += 1
                start = counter
                break

            counter += 1

        else:
            return None

        while counter < len(sed_string):
            if (sed_string[counter] == "\\" and counter + 1 < len(sed_string)
                    and sed_string[counter + 1] == delim):
                sed_string = sed_string[:counter] + sed_string[counter + 1:]

            elif sed_string[counter] == delim:
                replace_with = sed_string[start:counter]
                counter += 1
                break

            counter += 1
        else:
            return replace, sed_string[start:], ""

        flags = ""
        if counter < len(sed_string):
            flags = sed_string[counter:]
        return replace, replace_with, flags.lower()
    return None


@register(outgoing=True, pattern=r"^\.s")
async def sed(command):
    """ Untuk perintah sed, gunakan sed di Telegram. """
    sed_result = await separate_sed(command.text)
    textx = await command.get_reply_message()
    if sed_result:
        if textx:
            to_fix = textx.text
        else:
            return await command.edit(
                "`Mastah, saya tidak punya otak. Anda juga tidak, saya kira.`")

        repl, repl_with, flags = sed_result

        if not repl:
            return await command.edit(
                "`Mastah, saya tidak punya otak. Anda juga tidak, saya kira.`")

        try:
            check = re.match(repl, to_fix, flags=re.IGNORECASE)
            if check and check.group(0).lower() == to_fix.lower():
                return await command.edit("`Boi!, itu balasan. Jangan gunakan sed`")

            if "i" in flags and "g" in flags:
                text = re.sub(repl, repl_with, to_fix, flags=re.I).strip()
            elif "i" in flags:
                text = re.sub(repl, repl_with, to_fix, count=1,
                              flags=re.I).strip()
            elif "g" in flags:
                text = re.sub(repl, repl_with, to_fix).strip()
            else:
                text = re.sub(repl, repl_with, to_fix, count=1).strip()
        except sre_err:
            return await command.edit("B O I! [Learn Regex](https://regexone.com)")
        if text:
            await command.edit(f"Apakah yang kamu maksud? \n\n{teks}")


CMD_HELP.update({
    "sed": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.s` <pembatas><kata lama><pembatas><kata baru>"
    "\nPenggunaan: Mengganti kata atau kata menggunakan sed."
    "\nDelimiters: `/, :, |, _`"
})
