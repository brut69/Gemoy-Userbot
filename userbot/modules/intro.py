from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.saya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hemblo 👋 Perkenalkan Namaku 𝙂𝙀𝙈𝙊𝙔-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 `")
    sleep(3)
    await typew.edit("`Tinggal Di Mars`")
    sleep(1)
    await typew.edit("`Aku anak Kedua dari 11 bersaudara`")
    sleep(1)
    await typew.edit("`Hobiku Nyemil, Tidur, Nyemil, Tidur`")
    sleep(1)
    await typew.edit("`Kegiatanku sekarang tidak ada😂`")
    sleep(1)
    await typew.edit("`Karena itu Aku gabut gatau stress keknya juga🤪`")
    sleep(1)
    await typew.edit("`Ya beginilah aku Apa Adanya. Bhaak🤣`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.kamu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(1)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 🥰`")
    sleep(1)
    await typew.edit("`I MISS YOU 🤧`")
    sleep(1)
    await typew.edit("`INTINYA KALO KETEMU JAN SAMPE ANU 👉👈`")
    sleep(1)
    await typew.edit("`🥲🥲🥲`")
    sleep(1)
    await typew.edit("`😭😭😭`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Bernapas itu Gratis`")
    sleep(1)
    await typew.edit("`Sama halnya kek Ibadah`")
    sleep(1)
    await typew.edit("`Jaga diri, Jaga kesehatan`")
    sleep(1)
    await typew.edit("`Dalam semangat, syukur dan keceriaan 🥰`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.aku(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Aku 𝙂𝙀𝙈𝙊𝙔-𝙐𝙎𝙀𝙍𝘽𝙊𝙏`")
    sleep(3)
    await typew.edit("`Jangan Nakal kamu yah`")
    sleep(1)
    await typew.edit("`Cepet tobat ape perlu Aku Rukyah ntar nih GC`")
    sleep(1)
    await typew.edit("`Kalo perlu Aku Rukyah Ownernya sklian`")
    sleep(1)
    await typew.edit("`Ebujet.. 😭😭`")

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
