# Credits By @VckyouuBitch From Geez - Project
# BUATLO NI ANAK ANAK ANJING YANG KALO NGAMBIL MODUL DENGAN HAPUS CREDITS.
# INTINYA LO ANJING!!!!!!

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Memeriksa Apakah Anda Terbatas...`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Bos! Silakan Buka Blokir @SpamBot`")
            return
        await event.edit(f"~ {response.message.message}")


CMD_HELP.update({"limit": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.limit`"
                 "\nPenggunaan: ngecek akun limit"})
