# Thanks Full To Team Ultroid
# Ported By Vcky @VckyouuBitch
# Copyright (c) 2021 Geez - Projects
# Geez - Projects https://github.com/Vckyou/Geez-UserBot
# Ini Belum Ke Fix Ya Bg :')

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from telethon.tl.types import ChatAdminRights
from userbot import CMD_HELP
from userbot.events import register

NO_ADMIN = "`Maaf anda bukan admin :)`"


async def get_call(event):
    geez = await event.client(getchat(event.chat_id))
    vcky = await event.client(getvc(geez.full_chat.call))
    return vcky.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.vcsr$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(startvc(e.chat_id))
        await e.edit("`Obrolan Suara Dimulai...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcst$", groups_only=True)
async def _(e):
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        return await e.edit(NO_ADMIN)
    new_rights = ChatAdminRights(invite_users=True)
    try:
        await e.client(stopvc(await get_call(e)))
        await e.edit("`Obrolan Suara Dihentikan...`")
    except Exception as ex:
        await e.edit(f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.vcin", groups_only=True)
async def _(e):
    await e.edit("`Mengundang Anggota ke Obrolan Suara...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await e.edit(f"`Mengundang {z} anggota`")


CMD_HELP.update(
    {
        "vcs": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcsr`\
         \nPenggunaan: Mulai Panggilan Grup dalam grup.\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcst`\
         \nPenggunaan: `Hentikan Panggilan Grup dalam grup.`\
         \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcin`\
         \nPenggunaan: Undang semua anggota grup dalam Panggilan Grup (Anda harus bergabung)."
    }
)
