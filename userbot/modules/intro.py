from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.saya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hai Perkenalkan Namaku {ALIVE_NAME}`")
    sleep(3)
    await typew.edit("`Umurku 17 y.o`")
    sleep(3)
    await typew.edit("`Saya pengguna 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏`")
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
    await typew.edit("`Aku 𝙂𝙀𝙈𝙊𝙔 𝙐𝙎𝙀𝙍𝘽𝙊𝙏`")
    sleep(3)
    await typew.edit("`Jangan Main Main`")
    sleep(2)
    await typew.edit("`Aku Gban Nangesss Ntar Lu. Bhaks`")
    
# Create by myself @localheart



CMD_HELP.update({
    "intro":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.saya`\
\n↳ : Intro saja.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.kamu`\
\n↳ : Kamu iya kamu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
\n↳ : Neber stop to learn.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.aku`\
\n : Lmao."
})
