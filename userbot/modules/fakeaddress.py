import json
import urllib.request


from userbot.events import register
from userbot import CMD_HELP


# Port By @VckyouuBitch From gemoyProject
# Buat Kamu Yang Hapus Credits. Intinya Kamu Anjing:)
@register(outgoing=True, pattern="^.ip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    adress = input_str

    token = "19e7f2b6fe27deb566140aae134dec6b"

    api = "http://api.ipstack.com/" + adress + "?access_key=" + token + "&format=1"

    result = urllib.request.urlopen(api).read()
    result = result.decode()

    result = json.loads(result)
    gemoy1 = result["type"]
    gemoy2 = result["country_code"]
    gemoy3 = result["region_name"]
    gemoy4 = result["city"]
    gemoy5 = result["zip"]
    gemoy6 = result["latitude"]
    gemoy7 = result["longitude"]
    await event.edit(
        f"<b><u>INFORMASI BERHASIL DIKUMPULKAN</b></u>\n\n<b>Ip type :-</b><code>{gemoy1}</code>\n<b>Country code:- </b> <code>{gemoy2}</code>\n<b>State name :-</b><code>{gemoy3}</code>\n<b>City name :- </b><code>{gemoy4}</code>\n<b>zip :-</b><code>{gemoy5}</code>\n<b>Latitude:- </b> <code>{gemoy6}</code>\n<b>Longitude :- </b><code>{gemoy7}</code>\n",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "fakeaddress": "**IP HACK**\
\n\n**Syntax : **`.ip <ip address>`\
\n**Usage :** Memberikan detail tentang alamat ip."
    }
)
