from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================

@register(outgoing=True, pattern='^.aslm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝐀𝐒𝐒𝐀𝐋𝐀𝐌𝐔'𝐀𝐋𝐀𝐈𝐊𝐔𝐌 𝐓𝐎𝐓𝐓𝐓𝐓!!`")


@register(outgoing=True, pattern='^.gjm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAK, JANGAN MAKSA SU!!")


@register(outgoing=True, pattern='^.wslm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`𝐖𝐀'𝐀𝐋𝐀𝐈𝐊𝐔𝐌𝐒𝐀𝐋𝐀𝐌 𝐓𝐎𝐓𝐓𝐓𝐓 𝐓𝐎𝐋!!`")


@register(outgoing=True, pattern='^.gjj(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAJELAS KAU JAMET")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YABEGONOBAE..**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEMEK NYA ANAK INI, BEUH BASI BAU TRASI...**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL LU MO LU JUAL PER METER BERAPA ??**")


@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BABI....**")


@register(outgoing=True, pattern='^.gjk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BAT KONTOL ANJINK BABI...**")


@register(outgoing=True, pattern='^.dih(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIH.. GAJE LU!! MENDING LU LIVE SHOW SONO BIAR LAKU BANGKE!!**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, LO SANGEAN!!!**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SKIP LU BAU PEJUU..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI, ANAK HASIL ZINA..!!**")


@register(outgoing=True, pattern='^.em(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EA.. MEME NYA SELUBANG BUAYA!!!**")


@register(outgoing=True, pattern='^.eh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH NGENTOT YUU...!**")


@register(outgoing=True, pattern='^.ucp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU SAPE BABI, NAK HAROM SOSOAN LU!!!**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HEY, NAK NGENTOT!! GOSAH SO KERAS..**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC NYA AJA KEK SAMPAH!! PALAGI OWN NYA BAU BANGKE KONTOL!!!**")
    

CMD_HELP.update({
    "salam2":
    ".aslm\
\nPenggunaan:\
\n\n.wslm\
\nPenggunaan:\
\n\n.gjj\
\nPenggunaan:\
\n\n.gjn\
\nPenggunaan:\
\n\n.gjb\
\nPenggunaan:\
\n\n.yb\
\nPenggunaan:\
\n\n.gjk\
\nPenggunaan:"
})

CMD_HELP.update({
    "salam3":
    ".dih\
\nPenggunaan:\
\n\n.bsl\
\nPenggunaan:\
\n\n.hai\
\nPenggunaan:\
\n\n.eh\
\nPenggunaan:\
\n\n.em\
\nPenggunaan:\
\n\n.gls\
\nPenggunaan:\
\n\n.hey\
\nPenggunaan:\
\n\n.loh\
\nPenggunaan:\
\n\n.ucp\
\nPenggunaan:\
\n\n.m\
\nPenggunaan:\
\n\n.k\
\nPenggunaan:"
})
