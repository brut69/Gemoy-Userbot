from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.pap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@fybpap_bot"
    await event.edit("```Pencarian Pap```")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(chat, link)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Buka blokir @fybpap_bot dan coba lagi, atau join dahulu ke Channel @ratefyb```")
            return
        if response.text.startswith(
                "**Maaf saya tidak bisa mendapatkan pap dari**"):
            await event.edit("```Saya pikir ini Anda harus join Channel dahulu ke @ratefyb```")
        else:
            await event.delete()
            await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "paprate":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pap` <link/code> \
\nPenggunaan: lihat adult pap. Kek"})
