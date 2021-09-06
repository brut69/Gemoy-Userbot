# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# Kalo mau ngecopas, jangan hapus credit ya goblok

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, groups_only=True, pattern=r"^\.startos$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await c.edit("`Obrolan Suara Dimulai...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.stopos$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await c.edit(f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await c.edit("`Obrolan Suara Dihentikan...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")


@register(outgoing=True, groups_only=True, pattern=r"^\.inviteos")
async def _(c):
    await c.edit("`Mengundang Anggota ke Obrolan Suara...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botman = list(user_list(users, 6))
    for p in botman:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await c.edit(f"`{z}` **Orang Berhasil diundang ke Obrolan Suara**")


CMD_HELP.update(
    {
        "os": "𝙋𝙡𝙪𝙜𝙞𝙣: `os`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.startos`\
        \nPenggunaan: Untuk Memulai voice chat group\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.stopos`\
        \nPenggunaan: Untuk Memberhentikan voice chat group\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.inviteos`\
        \nPenggunaan: Mengundang Member group ke voice chat group\
    "
    }
)
