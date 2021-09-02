# Copyright (C) 2020 Catuserbot <https://github.com/sandy1709/catuserbot>
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#

"""Count the Number of Dialogs you have in your Telegram Account
Syntax: .stats & .ustat"""

import time

from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from userbot import CMD_HELP
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply

# STRINGS
STAT_INDICATION = "`Collecting stats, Please wait....`"


# Functions
def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


async def get_entity(msg):
    bold = {0: 0}
    italic = {0: 0}
    mono = {0: 0}
    link = {0: 0}
    if not msg.entities:
        return bold, mono, italic, link
    for entity in msg.entities:
        if isinstance(entity, types.MessageEntityBold):
            bold[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityItalic):
            italic[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityCode):
            mono[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityUrl):
            link[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityTextUrl):
            link[entity.offset] = entity.offset + entity.length
        elif isinstance(entity, types.MessageEntityMention):
            link[entity.offset] = entity.offset + entity.length
    return bold, mono, italic, link


@register(outgoing=True, pattern=r"^\.stats$")
async def stats(event):
    stat = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"📊 **Stats for {full_name}** \n\n"
    response += f"**Private Chats:** {private_chats} \n"
    response += f"   • `Users: {private_chats - bots}` \n"
    response += f"   • `Bots: {bots}` \n"
    response += f"**Groups:** {groups} \n"
    response += f"**Channels:** {broadcast_channels} \n"
    response += f"**Admin in Groups:** {admin_in_groups} \n"
    response += f"   • `Creator: {creator_in_groups}` \n"
    response += f"   • `Admin Rights: {admin_in_groups - creator_in_groups}` \n"
    response += f"**Admin in Channels:** {admin_in_broadcast_channels} \n"
    response += f"   • `Creator: {creator_in_channels}` \n"
    response += (
        f"   • `Admin Rights: {admin_in_broadcast_channels - creator_in_channels}` \n"
    )
    response += f"**Unread:** {unread} \n"
    response += f"**Unread Mentions:** {unread_mentions} \n\n"
    response += f"⏱ __It Took:__ {stop_time:.02f}s \n"
    await stat.edit(response)


@register(outgoing=True, pattern=r"^\.(ustat|deteksi|ustats)(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "`Balas pesan pengguna atau berikan userid/username`",
        )
    if input_str:
        try:
            uid = int(input_str)
        except ValueError:
            try:
                u = await event.client.get_entity(input_str)
            except ValueError:
                await edit_delete(
                    event, "`Berikan userid atau username untuk melihat riwayat group`"
                )
            uid = u.id
    else:
        uid = reply_message.sender_id
    chat = "@tgscanrobot"
    sevent = await edit_or_reply(event, "`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"{uid}")
        except Exception:
            await edit_delete(sevent, "**Unblock @tgscanrobot dan coba lagi**")
        response = await conv.get_response()
        await event.client.send_read_acknowledge(conv.chat_id)
        await sevent.edit(response.text)
        """Cleanup after completed"""
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id])


CMD_HELP.update(
    {
        "stats": "**Plugin : **`stats`\
        \n\n  •  **Syntax :** `.stats`\
        \n  •  **Function : **Untuk memeriksa statistik pengguna\
        \n\n  •  **Syntax :** `.ustat` atau `.ustats`\
        \n  •  **Function : **Untuk memeriksa orang tersebut bergabung ke grup mana aja\
    "
    }
)


CMD_HELP.update(
    {
        "deteksi": "**Plugin : **`deteksi`\
        \n\n  •  **Syntax :** `.deteksi`\
        \n  •  **Function : **Untuk memeriksa orang tersebut bergabung ke grup mana aja\
    "
    }
)
