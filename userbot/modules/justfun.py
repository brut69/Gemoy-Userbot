# Based Plugins
# Ported For Lord-Userbot By liualvinas/Alvin
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini!!!
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


# Alvin Gans


@register(outgoing=True, pattern=r"^\.wp(?: |$)(.*)")
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


# Alvin Gans


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


# Ported For Lord-Userbot By liualvinas/Alvin


CMD_HELP.update(
    {
        "justfun": "𝙋𝙡𝙪𝙜𝙞𝙣: `justfun`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.xogame`\
        \nPenggunaan: Game xo-game bot\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mod` <nama app>\
        \nPenggunaan: Dapatkan applikasi mod\
    "
    }
)


CMD_HELP.update(
    {
        "secretchat": "𝙋𝙡𝙪𝙜𝙞𝙣: `secretchat`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.wp` <teks> <username/id>\
        \nPenggunaan: Memberikan pesan rahasia haya orang yang di tag yang bisa melihat\
        \n**Contoh**: `.wp` aku sayang kamu\
    "
    }
)
