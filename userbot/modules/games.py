from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.xogame(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.whisp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.mod(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.truth(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@truthordaresbot"
    honest = "truth"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, honest)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.dare(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@truthordaresbot"
    dare = "dare"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, dare)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.spill(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@Spillgame_bot"
    spill = "spill"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, spill)
    await tap[0].click(event.chat_id)
    await event.delete()


@register(outgoing=True, pattern=r"^\.f100(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    botusername = "@Familys100_bot"
    family = "next"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, family)
    await tap[0].click(event.chat_id)
    await event.delete()


CMD_HELP.update({
    "games": "\
𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.xogame`\
\nPenggunaan: Mainkan game XO bersama temanmu.\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mod <nama app>`\
\nPenggunaan: Dapatkan applikasi mod\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.whisp <teks> <username/ID>`\
\nPenggunaan: Berikan pesan rahasia\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.truth`\
\nPenggunaan: Tantangan kejujuran.\
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.dare`\
\nPenggunaan: Tantangan lain.
\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.spill`
    \nPenggunaan: Spill pertanyaan.
    \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.f100`
    \nPenggunaan: Kuis Family 100."})
