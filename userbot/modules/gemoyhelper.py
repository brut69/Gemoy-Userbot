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


""" Userbot module for other small commands. """

from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/dunottagme)"
        "\n[Repo](https://github.com/brut69/Gemoy-Userbot)"
        "\n[Instagram](instagram.com/intan_hepy)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/brut69/Gemoy-Userbot/Gemoy-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lhelp`\
\nPenggunaan: Bantuan Untuk QueenGemoy-Userbot.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vars`\
\nPenggunaan: Melihat Daftar Vars."
})
