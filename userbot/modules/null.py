# Gemoy-Userbot ©2021
# @brut69
from userbot.events import register
from time import sleep


@register(outgoing=True, pattern='^.gemoybot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Hai Perkenalkan Namaku 𝙂𝙀𝙈𝙊𝙔-𝙐𝙎𝙀𝙍𝘽𝙊𝙏`")
    sleep(2)
    await typew.edit("`Aku lahir karena emang mau lahir`")
    sleep(1)
    await typew.edit("`Usiaku sekarang masih beberapa bulan`")
    sleep(1)
    await typew.edit("`Aku cuma ingin banyak yang mengenalku disini`")
    sleep(1)
    await typew.edit("`Jika kalian ingin tahu banyak tentangku`")
    sleep(1)
    await typew.edit("`Atau kalian punya masukan`")
    sleep(1)
    await typew.edit("`Agar Userbot ini lebih mengerti kalian`")
    sleep(1)
    await typew.edit("`Kalian bisa menghubungi Pembuatku`")
    sleep(1)
    await typew.edit("`Salam Hangat semua`")
    sleep(1)
    await typew.edit("`#tag @dunottagme`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({"gemoybot": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gemoybot`"
                 "\nPenggunaan: Just Intro."})