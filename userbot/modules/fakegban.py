# This is a troll indeed ffs *facepalm*
# Ported from xtra-telegram by @heyworld
import asyncio
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
# from userbot.utils import admin_cmd
from userbot.events import register
from userbot import ALIVE_NAME, CMD_HELP, bot

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.fgban(?: |$)(.*)")
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = f"`Peringatan!! Pengguna 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n"
    no_reason = "Tidak ada alasan yang diberikan"
    await event.edit("**Memanggil palu Gban yang perkasa 🔨**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 1036951071:
            await reply_message.reply("`Tunggu sebentar, Ini tuanku!`\n**Beraninya kau mengancam akan melarang tuan negroku!**\n\n__Akunmu telah diretas! Bayar $6969 ke tuanku__[Heyworld](tg: // user?id=1036951071) __untuk melepaskan
        else:
            jnl=("`Warning!!`"
                   "[{}](tg://user?id={})"
                   f"` 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By` {DEFAULTUSER}\n\n"
                   "**Nama: ** __{}__\n"
                   "**ID : ** `{}`\n"
                   ).format(firstname, idd, firstname, idd)
            if usname is None:
                jnl += "**Username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm="`{}`".format(gbunVar)
                gbunr="**Alasan: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention=(
            f"Peringatan!! Pengguna 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 By {DEFAULTUSER} \nReason: Tidak ada alasan yang diberikan.")
        await event.reply(mention)
    await event.delete()

CMD_HELP.update({
    "fakegban": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fgban`\
    \nPenggunaan: `.fgban` or Reply `.fgban` alasan dan lihat sendiri. "
})
