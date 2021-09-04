# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported to UserBot by @Mayur_Karaniya

from github import Github
import os
import time
from datetime import datetime
# from sample_config import Config
# from uniborg.util import admin_cmd, humanbytes, progress, time_formatter
from userbot.events import register
# from userbot.events import humanbytes, progress, time_formatter
from userbot import CMD_HELP, GITHUB_ACCESS_TOKEN, GIT_REPO_NAME, bot


GIT_TEMP_DIR = "./userbot/temp/"
# @borg.on(admin_cmd(pattern="commit ?(.*)", allow_sudo=True))


@register(outgoing=True, pattern=r"^\.gcommit(?: |$)(.*)")
# @register(pattern=r".commit (.*)", outgoing=True)
async def download(event):
    if event.fwd_from:
        return
    if GITHUB_ACCESS_TOKEN is None:
        await event.edit("`Silakan TAMBAHKAN Token Akses yang Tepat dari github.com`")
        return
    if GIT_REPO_NAME is None:
        await event.edit("`Silakan TAMBAHKAN Nama Repo Github yang Tepat dari bot pengguna Anda`")
        return
    mone = await event.reply("Pengolahan ...")
    if not os.path.isdir(GIT_TEMP_DIR):
        os.makedirs(GIT_TEMP_DIR)
    start = datetime.now()
    reply_message = await event.get_reply_message()
    try:
        time.time()
        print("Mengunduh ke direktori TEMP")
        downloaded_file_name = await bot.download_media(
            reply_message.media,
            GIT_TEMP_DIR
        )
    except Exception as e:
        await mone.edit(str(e))
    else:
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await mone.edit("Diunduh ke `{}` in {} seconds.".format(downloaded_file_name, ms))
        await mone.edit("Berkomitmen ke Github....")
        await git_commit(downloaded_file_name, mone)


async def git_commit(file_name, mone):
    content_list = []
    access_token = GITHUB_ACCESS_TOKEN
    g = Github(access_token)
    file = open(file_name, "r", encoding='utf-8')
    commit_data = file.read()
    repo = g.get_repo(GIT_REPO_NAME)
    print(repo.name)
    create_file = True
    contents = repo.get_contents("")
    for content_file in contents:
        content_list.append(str(content_file))
        print(content_file)
    for i in content_list:
        create_file = True
        if i == 'ContentFile(path="' + file_name + '")':
            return await mone.edit("`File Sudah Ada`")
            create_file = False
    file_name = "userbot/modules/" + file_name
    if create_file:
        file_name = file_name.replace("./userbot/temp/", "")
        print(file_name)
        try:
            repo.create_file(
                file_name,
                "Uploaded New Plugin",
                commit_data,
                branch="master")
            print("Committed File")
            ccess = GIT_REPO_NAME
            ccess = ccess.strip()
            await mone.edit(f"`Commited On Your Github Repo`\n\n[Your Modules](https://github.com/{ccess}/tree/sql-extended/userbot/modules/)")
        except BaseException:
            print("Tidak Dapat Membuat Plugin")
            await mone.edit("Tidak Dapat Mengunggah Plugin")
    else:
        return await mone.edit("`Bunuh Diri yang Dilakukan`")


CMD_HELP.update({
    "gcommit":
    ".gcommit\
    \nUsage: Plugin Pengunggah File GITHUB untuk userbot. Otomatisasi Heroku harus Diaktifkan. Kalau tidak, Anda tidak malas, Untuk orang malas\
\nInstruksi:- Setel Variabel GITHUB_ACCESS_TOKEN dan GIT_REPO_NAME di Heroku vars First\
\n.commit reply_to_any_plugin juga dapat berupa jenis file apa pun. tapi untuk plugin harus di .py ."})
