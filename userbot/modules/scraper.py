# Coded By Abdul <https://github.com/DoellBarr>
# Ported By VckyAuliaZulfikar @VckyouuBitch
#
# gemoy Projects UserBot
# Copyright (C) 2021 gemoyProjects
#
# This file is a part of <https://github.com/vckyou/gemoyProjects/>
# PLease read the GNU Affero General Public License in
# <https://github.com/vckyou/gemoyProjects/blob/master/LICENSE>.

import asyncio
import csv
import random
from asyncio import sleep
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserPrivacyRestrictedError,
    UserNotMutualContactError
)
from telethon.tl.functions.channels import (
    InviteToChannelRequest,
    EditBannedRequest,
    GetFullChannelRequest)
from telethon.tl.types import InputPeerUser, ChatBannedRights
from telethon.tl import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError)

from userbot.events import register
from userbot import CMD_HELP


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Saluran/grup tidak valid`")
            return None
        except ChannelPrivateError:
            await event.reply("`Ini adalah saluran/grup pribadi atau saya dilarang dari sana`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Saluran atau supergrup tidak ada`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Saluran/grup tidak valid`")
            return None
    return chat_info


@register(outgoing=True, pattern=r"^\.inviteall(?: |$)(.*)")
async def get_users(event):
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        gemoy = await event.reply("`pengolahan...`")
    else:
        gemoy = await event.edit("`pengolahan...`")
    gemoyteam = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await gemoy.edit("`Maaf, Dapat menambahkan pengguna di sini`")
    s = 0
    f = 0
    error = 'None'

    await gemoy.edit("**Status Terminal**\n\n`Mengumpulkan Pengguna.......`")
    async for user in event.client.iter_participants(gemoyteam.full_chat.id):
        try:
            if error.startswith("Too"):
                return await gemoy.edit(f"**Terminal Selesai Dengan Kesalahan**\n(`Mungkin Mendapat Batas Kesalahan dari telethon Silakan coba lagi Nanti`)\n**Kesalahan** : \n`{error}`\n\n• `{s}` orang yang diundang \\ n• Gagal Mengundang `{f}` orang")
            await event.client(functions.channels.InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await gemoy.edit(f"**Terminal Berjalan...**\n\n• Mengundang `{s}` orang \n• Gagal Mengundang `{f}` orang\n\n**× LastError:** `{error}`")
        except Exception as e:
            error = str(e)
            f = f + 1
    return await gemoy.edit(f"**Terminal Selesai** \n\n• Berhasil Mengundang `{s}` orang \n• gagal mengundang `{f}` orang")


@register(outgoing=True, pattern=r"^\.getmemb$")
async def scrapmem(event):
    chat = event.chat_id
    await event.edit("`Mohon tunggu...`")
    event.client
    members = await event.client.get_participants(chat, aggressive=True)

    with open("members.csv", "w", encoding="UTF-8") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(["user_id", "hash"])
        for member in members:
            writer.writerow([member.id, member.access_hash])
    await event.edit("`Berhasil Mengumpulkan Member..`")


@register(outgoing=True, pattern=r"^\.addmemb$")
async def admem(event):
    await event.edit("`Proses Menambahkan 0 Member...`")
    chat = await event.get_chat()
    event.client
    users = []
    with open("members.csv", encoding="UTF-8") as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {'id': int(row[0]), 'hash': int(row[1])}
            users.append(user)
    n = 0
    for user in users:
        n += 1
        if n % 30 == 0:
            await event.edit(f"`Mencapai 30 anggota, tunggu selama {900/60} menit`")
            await asyncio.sleep(900)
        try:
            userin = InputPeerUser(user['id'], user['hash'])
            await event.client(InviteToChannelRequest(chat, [userin]))
            await asyncio.sleep(random.randrange(5, 7))
            await event.edit(f"`Prosess Menambahkan {n} Member...`")
        except TypeError:
            n -= 1
            continue
        except UserAlreadyParticipantError:
            n -= 1
            continue
        except UserPrivacyRestrictedError:
            n -= 1
            continue
        except UserNotMutualContactError:
            n -= 1
            continue


# Port By @VckyouuBitch From gemoyProject
# Perkontolan Dengan Hapus Credits
@register(outgoing=True, pattern="^.allban(?: |$)(.*)")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("Anda Tidak Mempunyai Hak")
        return
    await event.edit("Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Tidak Ada yang Terjadi di sini 🙃")


CMD_HELP.update({
    "inviteall":
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.inviteall groups username`\
          \n📌 : __Scrapes users from the given chat to your group__."
})

CMD_HELP.update(
    {
        "allban": "**Plugin : **`allban`\
    \n\n**Syntax : **`.allban`\
    \n**Function : **ban all members in 1 cmnd"
    }
)

CMD_HELP.update({
    "scraper":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getmemb`\
   \nUsage : Mengumpulkan Anggota dari Obrolan\
   \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.addmemb`\
   \nUsage : Menambahkan Anggota ke Obrolan\
   \nTata Cara Menggunakannya:  Pertama, Anda harus melakukan .getmemb terlebih dahulu dari Obrolan. Lalu buka grup Anda dan ketik .addmemb untuk menambahkan mereka ke grup Anda."
})
