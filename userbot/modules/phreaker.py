#
# Gemoy-Userbot (Telegram Userbot Project )
# Copyright (C) 2021 @dunottagme

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.nmap(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    nmap = f"nmap"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{nmap} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.subd(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    subdomain = f"subdomain"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{subdomain} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.cek(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@scriptkiddies_bot"  # pylint:disable=E0602
    httpheader = f"httpheader"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@scriptkiddies_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=510263282))
            await conv.send_message(f'/{httpheader} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @ scriptkiddies_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(httpheader, response.message.message)


@register(outgoing=True, pattern=r"^\.bin(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"  # pylint:disable=E0602
    bin = f"bin"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await conv.send_message(f'/{bin} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @Carol5_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


@register(outgoing=True, pattern=r"^\.cc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@Carol5_bot"  # pylint:disable=E0602
    ss = f"ss"  # pylint:disable=E0602
    await event.edit("Processing....")
    async with bot.conversation("@Carol5_bot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1247032902))
            await conv.send_message(f'/{ss} {link}')
            response = await response
        except YouBlockedUserError:
            await event.reply("Unblock @Carol5_bot dulu Goblok!!")
            return
        else:
            await event.edit(f"{response.message.message}")
            await event.client.delete_messages(response.message.message)


CMD_HELP.update({
    "bughost": "????????????????????????????: `.nmap <bug hosts>`\
\nPenggunaan: to get info bug/host.\
\n\n????????????????????????????: `.subd <bug hosts>`\
\nPenggunaan: to get subdomain bug/host.\
\n\n????????????????????????????: `.cek <bug hosts>`\
\nPenggunaan: to cek respons bug/host.\
\n\n????????????????????????????: `.bin < bin number >`\
\nPenggunaan: to cek bin ip.\
\n\n????????????????????????????: `.cc <mm|yy|cvv`\
\nPenggunaan: to cek Credits Card Stats."
})
