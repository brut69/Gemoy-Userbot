from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb.`")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb.`")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumssalam wr. wb.`")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wa'alaikumssalam wr. wb.`")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Astagfirullah aladzin..`")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Astagfirullah..`")

CMD_HELP.update({
"`salam`": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P` | `.p`\
\nPenggunaan: Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L` `.l`\
\nPenggunaan: Untuk Menjawab Salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.atg`\
\nPenggunaan: Istighfar 1.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ast`\
\nPenggunaan: Istighfar 2."
})
