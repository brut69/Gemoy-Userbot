# Port By @VckyouuBitch From Geez-Projects
# # Copyright (C) 2021 Geez-Project
from userbot.events import register
from userbot import CMD_HELP
import asyncio


@register(outgoing=True, pattern="^.ftyping(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Format Salah`")
    await event.edit(f"`Memulai Pengetikan Palsu Selama {t} detik.`")
    async with event.client.action(event.chat_id, "mengetik"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Format Salah`")
    await event.edit(f"`Memulai perekaman audio palsu Selama {t} detik.`")
    async with event.client.action(event.chat_id, "suara rekaman"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fvideo(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Format Salah`")
    await event.edit(f"`Memulai perekaman video palsu Selama {t} detik.`")
    async with event.client.action(event.chat_id, "merekam video"):
        await asyncio.sleep(t)


@register(outgoing=True, pattern="^.fgame(?: |$)(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("`Format Salah`")
    await event.edit(f"`Memulai Bermain Game Palsu Selama {t} detik.`")
    async with event.client.action(event.chat_id, "permainan"):
        await asyncio.sleep(t)

CMD_HELP.update({
    "fakeaction":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ftyping` <jumlah teks>\
   \nPenggunaan: Seakan akan sedang mengetik padahal tidak\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.faudio` <jumlah teks>\
   \nPenggunaan: Berfungsi sama seperti ftyping tapi ini dalam bentuk fake audio\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fgame` <jumlah teks>\
   \nPenggunaan: Berfungsi sama seperti ftyping tapi ini dalam bentuk fake game\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fvideo` <jumlah teks>\
   \nPenggunaan: Berfungsi sama seperti ftyping tapi ini dalam bentuk fake video"
})
