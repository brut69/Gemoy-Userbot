from time import sleep
from userbot import CMD_HELP
from userbot.events import register
from userbot import ALIVE_NAME, WEATHER_DEFCITY


@register(outgoing=True, pattern='^.saya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit("`Umurku 17 y.o`")
    sleep(2)
    await typew.edit("`Saya pengguna  `")
    sleep(1)
    await typew.edit("`Tinggal Di {WEATHER_DEFCITY}, Salam Kenal Semua :)`")
    
# Create by myself @localheart


@register(outgoing=True, pattern='^.kamu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
    sleep(1)
    await typew.edit("`I LOVE YOU SO MUCH 🥰`")
    
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
    sleep(1)
    await typew.edit("`Alhamdulillah..`")
    
# Create by myself @localheart


@register(outgoing=True, pattern='^.aku(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Aku  `")
    sleep(3)
    await typew.edit("`Jangan Main Main`")
    sleep(2)
    await typew.edit("`Aku Gban Nangesss Ntar Lu. Bhaks`")
    
# Create by myself @localheart



CMD_HELP.update({
    "intro":
    ": `.saya`\
\n : Intro saja.\
\n\n: `.kamu`\
\n : Kamu iya kamu.\
\n\n: `.semangat`\
\n : Neber stop to learn.\
\n\n: `.aku`\
\n : Lmao."
})
