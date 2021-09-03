from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.sadboy(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


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
        "\n**Punten**"
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
        "\n**Masih Ku Pantau**"
    )
    
    
@register(outgoing=True, pattern='^.aku(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit(f"`Aku pengguna 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏`")
    sleep(2)
    await typew.edit(f"`Umurku 17 y.o`")
    sleep(1)
    await typew.edit(f"`Tinggal Di {WEATHER_DEFCITY}, Salam Kenal Semua:)`")


# Create by myself @localheart


CMD_HELP.update(
    {
        "punten": "**Plugin : **`Animasi Punten`\
        \n\n  •  **Syntax :** `.punten` ; `.pantau`\
        \n  •  **Function : **Arts Beruang kek lagi mantau.\
        \n\n  •  **Syntax :** `.sadboy`\
        \n  •  **Function : **ya sadboy coba aja.\
        \n\n  •  **Syntax :** `.aku`\
        \n  •  **Function : **Perkenalan Diri.\
    "
    }
)
