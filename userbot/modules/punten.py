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
