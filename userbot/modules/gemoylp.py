# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# Fixes by Github/ArnabXD | Telegram/Arnab431
# Ported to Gemoy-Userbot
# @dunottagme
# © 2021


from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================

EMOJIS = [
    "🥱",
    "🥱",
]

PICTURE_BERUANGLOVE = """
█▀███▀▀███▀▀███▀▀███▀▀███▀█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒█▒▒▒▒▒███▒▒█▒▒▒█▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒█▒▒▒▒▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█████▒█
█▒▒█▒▒▒▒█▒▒▒█▒▒█▒█▒▒█▒▒▒▒▒█
█▒▒████▒▒███▒▒▒▒█▒▒▒█████▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒█
█▒▒▒▒▒▒▒█──█▒████▒█──█▒▒▒▒█
█▒▒▒▒▒▒█──█─█────█─█──█▒▒▒█
█▒▒▒▒▒▒█─██───────███─█▒▒▒█
█▒▒▒▒▒▒█──────────────█▒▒▒█
█▒▒▒▒▒▒▒█────────────█▒▒▒▒█
█▒▒▒▒██▒▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█──██───██──█▒▒▒▒█
█▒▒▒█──█▒█────███────█▒▒▒▒█
█▒▒▒█──█▒█───█───█──█▒▒▒▒▒█
█▒▒▒▒█──█─█───███──█▒▒▒▒▒▒█
█▒▒▒▒▒█────██────██▒▒▒▒▒▒▒█
█▒▒▒▒▒█──────████─██▒▒▒▒▒▒█
█▒▒▒▒▒▒█───────────█▒▒▒▒▒▒█
█▒▒▒▒▒▒▒███─────────█▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒█──────█───█▒▒▒▒█
█▒▒▒▒███▒▒█───────█───█▒▒▒█
█▒▒▒█──████─────████───█▒▒█
█▒▒▒█────█─────█────█─█▒▒▒█
█▒▒▒█─────█────█────██▒▒▒▒█
█▒▒▒█──────█───█──────█▒▒▒█
█▒▒▒▒█─────██████─────█▒▒▒█
█▒▒▒▒▒█──███▒▒▒▒█─────█▒▒▒█
█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█───█▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒█
█▒▒▒▒█▒▒▒▒█▒▒███▒▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒█▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒██▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒▒█▒▒▒▒█▒▒▒█▒█▒▒▒█▒▒▒█
█▒▒▒▒▒█▒▒▒▒▒▒███▒▒▒███▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▄▄█▄▄██▄▄█▄▄█▄▄█▄▄██▄▄█▄▄█
"""

PICTURE_ILU = """
╔══╗
╚╗╔╝
╔╝(¯`v´¯)
╚══`.¸.YOU
"""

PICTURE_BIGLOVE = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄░░░░▄▄▄░░░░▄▄▄░░░░░░
░░░▀████▀░░▄█████▄▄█████▄░░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░▀██████████████▀░░░
░░░░▄██▄░░░░▀██████████▀░░░░░
░░░██████░░░░░▀██████▀░░░░░░░
░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░
░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░▀███░███▀▄█▀▀█▄░▀██▀░▀██▀░░
░░░░▀█▄█▀░▄█░░░░█▄░██░░░██░░░
░░░░░░█░░░██░░░░██░██░░░██░░░
░░░░░░█░░░░█▄░░▄█░░██░░░██░░░
░░░░▄███▄░░░▀██▀░░░░▀███▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""


PICTURE_ANAK = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄░░░░▄███▄▄███▄░░░░░░▄░░▄░░░░░░░░
░░░░█░░░░░██████████░░░░░░█░░█░░░░░░░░
░░░░█░░░░░░▀██████▀░░░░░░░█░░█░░░░░░░░
░░░▀▀▀░░░░░░░▀██▀░░░░░░░░░░▀▀░░░░░░░░░
░░░░░░░░░░░░▄░░░░░█░▄▀░░▄░░░░░░░░░░░░░
░░░░░░░░▄░░░▀▄▄▄▀█▀▀█▀▀▄█▄░█░░░░░░░░░░
░░░░░░░░░▀▄▄▀█░░░▀░░░░░░░░█▄░▄▀▀░░░░░░
░░░░░▀▀▄░█▀░░░░░░░░░▄▄▄▄▄▄░▀█░░░░░░░░░
░░░░░░▄▀▀░▄▄▀▀▀▄░░▄█▀░░░░▀▄░▄█▀▀▀▄░░░░
░░░▄▄██░░█░░░░░░█░█░░███░▄▀░░░██░█░░░░
░░█░▄█░░░█░███░▄▀░▀▀▄███▀░░░░░██░█░░░░
░░█░▀█▄░░▀▄███▄▀░░░░░░░░░░░░░▄█▄▀░░░░░
░░░▀▀▀▀█░░░░░░░░░░░░░░░▄█▀░░▄▀░░░░▄░░░
░░░░▄░░░▀▄░▀▀▄▄░░░░░▄▄▀▀░░▄▀░░░░▄█▀░░░
░░▄▄█▄░░░░▀▀▄▄░▀▀▀▀▀░▄▄▄▀▀░░▄▄▀▀▀█▀▀░░
░░▄█▀▀▀▀▄▄▄▄░░▀▀▀▀▀█▀░░░▄▄▀▀░░░░░░▀░░░
░░░░░░░░░░░░▀▀▀▀▀▄▄█▄▄▀▀░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░▀░░░░░░░░░░░░░░░░░░
"""


PICTURE_YUHU = """
────╪███████╪────╪███████
──╪███████████╪╪███████████
──██████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
─████████████████████████████
──██████████████████████████
──╪████████████████████████
───╪██████████████████████
─────████████████████████
──────╪████████████████
────────╪████████████
──────────╪████████
─────────────╪██
████─╪███╪╪████████──████─████
╪███─╪███─████╪████──████─████
─███─╪███─████─╪███╪─████─████
─███╪╪██╪─████─╪███╪─████─████
─╪██████──████─╪███╪─████─████
──██████──████─╪███╪─████─████
──█████╪──████─╪███╪─████─████
──╪████───████─╪███╪─████─████
───████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───████─╪███╪─████─████
──╪████───█████████──█████████
───████────███████╪──╪███████
"""


PICTURE_INLOVE = """
───▄▄▄▄▄▄─────▄▄▄▄▄▄
─▄█▓▓▓▓▓▓█▄─▄█▓▓▓▓▓▓█▄
▐█▓▓▒▒▒▒▒▓▓█▓▓▒▒▒▒▒▓▓█▌
█▓▓▒▒░╔╗╔═╦═╦═╦═╗░▒▒▓▓█
█▓▓▒▒░║╠╣╬╠╗║╔╣╩╣░▒▒▓▓█
▐█▓▓▒▒╚═╩═╝╚═╝╚═╝▒▒▓▓█▌
─▀█▓▓▒▒░░░░░░░░░▒▒▓▓█▀
───▀█▓▓▒▒░░░░░▒▒▓▓█▀
─────▀█▓▓▒▒░▒▒▓▓█▀
──────▀█▓▓▒▓▓█▀
────────▀█▓█▀
──────────▀
"""


PICTURE_LONG = """
░███████░
░█╬╬╬╬╬█░
░██╬╬███░
░██╬╬███░
░██╬╬███░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬╬████░
░█╬╬╬╬██░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░██╬╬╬██░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
"""


PICTURE_DATAR = """
  ::::          ::::::      ::::      ::::    :::::::::
  ::::        ::::  ::::    ::::      ::::    :::::::::
  ::::       ::::    ::::   ::::      ::::    ::::
  ::::       ::::    ::::    ::::    ::::     ::::::::
  ::::       ::::    ::::     ::::  ::::      ::::
  ::::       ::::    ::::      ::::::::       ::::
  ::::::::::  ::::  ::::        ::::::        :::::::::
  ::::::::::    ::::::           ::::         :::::::::
"""


PICTURE_ALAY = """
██─▄███▄███▄─██▄──▄██──▄███▄──██──██
██─█████████──▀████▀──██▀─▀██─██──██
██──▀█████▀─────██────██▄─▄██─██──██
██────▀█▀───────██─────▀███▀──▀█████
"""


PICTURE_APESI = """
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒░░░░░░═░░▒▒▒▒░░░░░░▒▒▒░░░░═░▒▒▒▒▒▒
▒▒▒▒▒▒░████████▓░▒▒░░█████░══█████▓═░▒▒▒▒
▒▒▒▒▒░▓█████████░▒░█████████████████░▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒░▒██████████████████═▒▒▒
▒▒▒▒▒▒▒░░═███═░▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒░███████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███═▒▒▒░▒██████████████████░▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒═█████████████████═▒▒▒▒
▒▒▒▒▒▒▒▒▒░███░▒▒▒▒▒─███████████████░░▒▒▒▒
▒▒▒▒▒▒▒▒░═███═░▒▒▒▒▒─█████████████═░▒▒▒▒▒
▒▒▒▒▒▒░░░▒███░▒░▒▒▒▒▒░░█████████▒═▒▒▒▒▒▒▒
▒▒▒▒▒░▒█████████═▒▒▒▒▒░═░█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░████████▒░▒▒░░░▒▒░═░▓▒═░▒▒▒▒░▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░▒▒░░░░░░░▒░░═░░░░░░░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████─██████████░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████═▒████████░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░─███▒─▒░─███░═░░░▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███▒░─███░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─███═███▒░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████▒░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─████═▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░─███═══░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▒░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░█████████▓░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░──────═░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░═▓█████▒═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████████░░▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═█████░░░████▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░░▒░═░███═▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═███░░▒▒▒▒▒░▓███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███═▒▒▒▒▒▒░░███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███░░▒▒▒▒▒░▒███░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒▒░░═███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████▒══░▓████░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─██████████▓═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███████═░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░═───░───═░░░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▓██████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░███████─███████░▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒███░░▒░░████─▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░███═░▒▒░▒██▒░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▓██▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███░▒▒▒░▒███░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒███─░▒░═███▓░▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═████░░░████═▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒─█████████═▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒═▒█████▓─▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░═░░▒▒▒▒▒▒▒▒▒▒
"""


PICTURE_SERAHLAH = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░▄▄▄▄▄▄░░░░░░░░░▄▄▄▄▄▄░░░░░░░░
░░░░▄▄▄▄░░░░▄▄▄▄░░░▄▄▄▄░░░░▄▄▄▄░░░░░
░▄▄▄▄░░░░░░░░░░░▄░▄░░░░░░░░░░░▄▄▄▄░░
▄▄░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░▄▄░
▄▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄░
▄▄░▐█▀▀██▀▀▀█▀█▀█▀▀█▄▄▄▄▄▄▄▄▄▄▄▄░▄▄░
▄▄░▐█──██─█─█─█─█─▀█─█─█─█▀█─█─█░▄▄░
▄▄░▐█──██─▀─█▄─▄█─▀█──█──█▄█─█▄█░▄▄░
▄▄░▐█▄▄▄█▀▀▀▀▀▀▀▀▀▀▀████████████░▄▄░
░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░
░░░▄▄▄▄░░░░░░░░░░░░░░░░░░░░░▄▄▄▄░░░░
░░░░░░▄▄▄▄░░░░░░░░░░░░░░░▄▄▄▄░░░░░░░
░░░░░░░░░▄▄▄▄░░░░░░░░░▄▄▄▄░░░░░░░░░░
░░░░░░░░░░░░▄▄▄▄░░░▄▄▄▄░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▄▄▄▄▄░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░▄▄▄░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░▄░░░░░░░░░░░░░░░░░░
"""


@register(outgoing=True, pattern=r"^\.(?:glop1|glop1)\s?(.)?")
async def emoji_glop1(e):
    emoji = e.pattern_match.group(1)
    glop1 = PICTURE_BERUANGLOVE
    if emoji:
        glop1 = glop1.replace('🥱', emoji)
    await e.edit(glop1)


@register(outgoing=True, pattern=r"^\.(?:glop2|glop2)\s?(.)?")
async def emoji_glop2(e):
    emoji = e.pattern_match.group(1)
    glop2 = PICTURE_ILU
    if emoji:
        glop2 = glop2.replace('🥱', emoji)
    await e.edit(glop2)


@register(outgoing=True, pattern=r"^\.(?:glop3|glop3)\s?(.)?")
async def emoji_glop3(e):
    emoji = e.pattern_match.group(1)
    glop3 = PICTURE_BIGLOVE
    if emoji:
        glop3 = glop3.replace('🥱', emoji)
    await e.edit(glop3)


@register(outgoing=True, pattern=r"^\.(?:glop4|glop4)\s?(.)?")
async def emoji_glop4(e):
    emoji = e.pattern_match.group(1)
    glop4 = PICTURE_ANAK
    if emoji:
        glop4 = glop4.replace('🥱', emoji)
    await e.edit(glop4)


@register(outgoing=True, pattern=r"^\.(?:glop5|glop5)\s?(.)?")
async def emoji_glop5(e):
    emoji = e.pattern_match.group(1)
    glop5 = PICTURE_YUHU
    if emoji:
        glop5 = glop5.replace('🥱', emoji)
    await e.edit(glop5)


@register(outgoing=True, pattern=r"^\.(?:glop6|glop6)\s?(.)?")
async def emoji_glop6(e):
    emoji = e.pattern_match.group(1)
    glop6 = PICTURE_INLOVE
    if emoji:
        glop6 = glop6.replace('🥱', emoji)
    await e.edit(glop6)


@register(outgoing=True, pattern=r"^\.(?:glop7|glop7)\s?(.)?")
async def emoji_glop7(e):
    emoji = e.pattern_match.group(1)
    glop7 = PICTURE_LONG
    if emoji:
        glop7 = glop7.replace('🥱', emoji)
    await e.edit(glop7)


@register(outgoing=True, pattern=r"^\.(?:glop8|glop8)\s?(.)?")
async def emoji_glop8(e):
    emoji = e.pattern_match.group(1)
    glop8 = PICTURE_DATAR
    if emoji:
        glop8 = glop8.replace('🥱', emoji)
    await e.edit(glop8)


@register(outgoing=True, pattern=r"^\.(?:glop9|glop9)\s?(.)?")
async def emoji_glop9(e):
    emoji = e.pattern_match.group(1)
    glop9 = PICTURE_ALAY
    if emoji:
        glop9 = glop9.replace('🥱', emoji)
    await e.edit(glop9)


@register(outgoing=True, pattern=r"^\.(?:glop10|glop10)\s?(.)?")
async def emoji_glop10(e):
    emoji = e.pattern_match.group(1)
    glop10 = PICTURE_APESI
    if emoji:
        glop10 = glop10.replace('🥱', emoji)
    await e.edit(glop10)


@register(outgoing=True, pattern=r"^\.(?:glop11|glop11)\s?(.)?")
async def emoji_glop11(e):
    emoji = e.pattern_match.group(1)
    glop11 = PICTURE_SERAHLAH
    if emoji:
        glop11 = glop11.replace('🥱', emoji)
    await e.edit(glop11)


CMD_HELP.update({
    "gemoylop":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.glop` `.glop1` `.glop2` `.glop3` `.glop4`\n`.glop5` `.glop6` `.glop7` `.glop8` `.glop9` `.glop10` `.glop11`\n`.pagi` `.mlm` `.night` `.lov`\nPenggunaan: Gemoy Userbot lope yu bhaaks."
}
)
