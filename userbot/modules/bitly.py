# Copyright (C) 2020 azrim.
# All rights reserved.
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


from bitlyshortener import Shortener
from re import match
from userbot import BITLY_TOKEN, BOTLOG, BOTLOG_CHATID
from userbot.events import register


@register(outgoing=True, pattern=r"^\.bitly(?: |$)(.*)")
async def shortener(short):
    """
        Shorten link using bit.ly API
    """
    if BITLY_TOKEN is not None:
        token = [f'{BITLY_TOKEN}']
        reply = await short.get_reply_message()
        message = short.pattern_match.group(1)
        if message:
            pass
        elif reply:
            message = reply.text
        else:
            await short.edit("`Error! No URL given!`")
            return
        link_match = match(r'\bhttps?://.*\.\S+', message)
        if not link_match:
            await short.edit("`Error! Please provide valid url!`\nexample: https://google.com")
            return
        urls = [f'{message}']
        bitly = Shortener(tokens=token, max_cache_size=8192)
        raw_output = bitly.shorten_urls(urls)
        string_output = f"{raw_output}"
        output = string_output.replace("['", "").replace("']", "")
        await short.edit(f"`Your link shortened successfully!`\nHere is your link {output}")
        if BOTLOG:
            await short.client.send_message(BOTLOG_CHATID, f"`#SHORTLINK \nThis Your Link!`\n {output}")
    else:
        await short.edit("Set bit.ly API token first\nGet from [here](https://bitly.com/a/sign_up)")
