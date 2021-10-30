import requests

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import man_cmd
from userbot.utils import edit_or_reply


@bot.on(man_cmd(outgoing=True, pattern="truth$"))
async def tede_truth(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/truth").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Truth**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


@bot.on(man_cmd(outgoing=True, pattern="dare$"))
async def tede_dare(event):
    try:
        resp = requests.get("https://api-tede.herokuapp.com/api/dare").json()
        results = resp["message"]
        await edit_or_reply(event, f"**#Dare**\n\n`{results}`")
    except Exception:
        await edit_or_reply(event, "**Something went wrong LOL...**")


CMD_HELP.update(
    {
        "truthdare": 
        "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `truthdare`\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `truth`\
        \nPenggunaan: Untuk tantangan.\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `dare`\
        \nPenggunaan: Untuk kejujuran.\
    "
    }
)
