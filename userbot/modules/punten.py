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

from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sadboy(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Sebenarnya....`")
    sleep(2)
    await typew.edit("`Aku pengen jujur ke kamu`")
    sleep(1)
    await typew.edit("`Soal hubungan kita 🥺`")
    sleep(2)
    await typew.edit("`Kamu sebenarnya sayang aku ndak sih?`")
    sleep(1)
    await typew.edit("`Terus kenapa kamu selalu jauhin aku`")
    sleep(1)
    await typew.edit("`Kadang aku cuma mikir`")
    sleep(1)
    await typew.edit("`Kurangku apa di Kamu`")
    sleep(1)
    await typew.edit("`Sampe Kamu tega lakuin ini ke Aku`")
    sleep(1)
    await typew.edit("`Aku tuh sayang kamu`")
    sleep(1)
    await typew.edit("`Kapan Kamu bisa ngertiin Aku`")
    sleep(1)
    await typew.edit("`Sampe sekarang pun`")
    sleep(1)
    await typew.edit("`Aku masi mengharap Kamu`")
    sleep(1)
    await typew.edit("`Kembali disini`")
    sleep(1)
    await typew.edit("`Di Hatiku...🥺😭`")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.punten(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n𝗠𝗜𝗦𝗜𝗠𝗜𝗦𝗜"
        "\n𝗡𝗚𝗜𝗡𝗧𝗜𝗣 𝗗𝗨𝗟𝗨 𝗔𝗛"
    )


@register(outgoing=True, pattern=r"^\.pantau(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n𝙝𝙢𝙢"
        "\n𝘼𝘿𝙀 𝘼𝙋𝙀 𝙎𝙄𝙄𝙃"
    )


# Create by myself @localheart


CMD_HELP.update(
    {
        "punten": "𝙋𝙡𝙪𝙜𝙞𝙣: `Animasi Punten`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.punten` | `.pantau`\
        \nPenggunaan: Arts Beruang mantau.\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sadboy`\
        \nPenggunaan: coba aja.\
    "
    }
)
