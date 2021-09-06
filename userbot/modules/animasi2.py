# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.

import time
from asyncio import sleep
from collections import deque
from random import choice, getrandbits, randint
from re import sub

import requests
from cowpy import cow

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.admin import get_user_from_event

# ================= CONSTANT =================
METOOSTR = [
    "Aku Juga Terimakasih",
    "Haha Iya, Aku Juga",
    "Sama Haha",
    "Aku Juga Gabut",
    "Sama Sini",
    "Haha Iya",
    "Aku Juga",
]

ZALG_LIST = [
    [
        "̖",
        " ̗",
        " ̘",
        " ̙",
        " ̜",
        " ̝",
        " ̞",
        " ̟",
        " ̠",
        " ̤",
        " ̥",
        " ̦",
        " ̩",
        " ̪",
        " ̫",
        " ̬",
        " ̭",
        " ̮",
        " ̯",
        " ̰",
        " ̱",
        " ̲",
        " ̳",
        " ̹",
        " ̺",
        " ̻",
        " ̼",
        " ͅ",
        " ͇",
        " ͈",
        " ͉",
        " ͍",
        " ͎",
        " ͓",
        " ͔",
        " ͕",
        " ͖",
        " ͙",
        " ͚",
        " ",
    ],
    [
        " ̍",
        " ̎",
        " ̄",
        " ̅",
        " ̿",
        " ̑",
        " ̆",
        " ̐",
        " ͒",
        " ͗",
        " ͑",
        " ̇",
        " ̈",
        " ̊",
        " ͂",
        " ̓",
        " ̈́",
        " ͊",
        " ͋",
        " ͌",
        " ̃",
        " ̂",
        " ̌",
        " ͐",
        " ́",
        " ̋",
        " ̏",
        " ̽",
        " ̉",
        " ͣ",
        " ͤ",
        " ͥ",
        " ͦ",
        " ͧ",
        " ͨ",
        " ͩ",
        " ͪ",
        " ͫ",
        " ͬ",
        " ͭ",
        " ͮ",
        " ͯ",
        " ̾",
        " ͛",
        " ͆",
        " ̚",
    ],
    [
        " ̕",
        " ̛",
        " ̀",
        " ́",
        " ͘",
        " ̡",
        " ̢",
        " ̧",
        " ̨",
        " ̴",
        " ̵",
        " ̶",
        " ͜",
        " ͝",
        " ͞",
        " ͟",
        " ͠",
        " ͢",
        " ̸",
        " ̷",
        " ͡",
    ],
]

EMOJIS = [
    "😂",
    "😂",
    "👌",
    "✌",
    "💞",
    "👍",
    "👌",
    "💯",
    "🎶",
    "👀",
    "😂",
    "👓",
    "👏",
    "👐",
    "🍕",
    "💥",
    "🍴",
    "💦",
    "💦",
    "🍑",
    "🍆",
    "😩",
    "😏",
    "👉👌",
    "👀",
    "👅",
    "😩",
    "🚰",
]

INSULT_STRINGS = [
    "Jangan minum dan mengetik.",
    "Saya pikir Anda harus pulang atau lebih baik ke rumah sakit jiwa.",
    "Perintah tidak ditemukan. Sama seperti otak Anda.",
    "Apakah kamu sadar bahwa kamu membodohi dirimu sendiri? Ternyata tidak.",
    "Anda bisa mengetik lebih baik dari itu.",
    "Bot aturan 544 bagian 9 mencegah saya membalas orang bodoh seperti Anda.",
    "Maaf, kami tidak menjual otak.",
    "Percayalah kamu tidak normal.",
    "Saya yakin otak Anda terasa seperti baru, mengingat Anda tidak pernah menggunakannya.",
    "Jika saya ingin bunuh diri, saya akan meningkatkan ego Anda dan melompat ke IQ Anda.",
    "Zombie memakan otak ... kamu aman.",
    "Anda tidak berevolusi dari kera, mereka berevolusi dari Anda.",
    "Kembalilah dan bicara padaku ketika IQ mu melebihi umurmu.",
    "Saya tidak mengatakan Anda bodoh, saya hanya mengatakan bahwa Anda tidak beruntung dalam hal berpikir.",
    "Kamu berbicara bahasa apa? Karena terdengar seperti omong kosong.",
    "Kebodohan bukanlah kejahatan jadi kamu bebas pergi.",
    "Anda adalah bukti bahwa evolusi BISA mundur.",
    "Aku akan bertanya berapa umurmu tapi aku tahu kamu tidak bisa menghitung setinggi itu.",
    "Sebagai orang luar, apa pendapat Anda tentang umat manusia?",
    "Otak bukanlah segalanya. Dalam kasusmu mereka bukan apa-apa.",
    "Biasanya orang hidup dan belajar. Kamu hidup saja.",
    "Aku tidak tahu apa yang membuatmu begitu bodoh, tapi itu benar-benar berhasil.",
    "Teruslah berbicara, suatu hari nanti kamu akan mengatakan sesuatu yang cerdas! (Meskipun aku ragu)"
    "Shock saya, katakan sesuatu yang cerdas.",
    "IQ Anda lebih rendah dari ukuran sepatu Anda.",
    "Aduh! Neurotransmiter Anda tidak lagi bekerja.",
    "Apakah kamu gila kamu bodoh.",
    "Setiap orang berhak untuk menjadi bodoh tetapi Anda menyalahgunakan hak istimewa tersebut.",
    "Maaf aku menyakiti perasaanmu saat menyebutmu bodoh. Kupikir kamu sudah tahu itu.",
    "Anda harus mencoba mencicipi sianida.",
    "Enzim Anda dimaksudkan untuk mencerna racun tikus.",
    "Kamu harus mencoba tidur selamanya.",
    "Ambil pistol dan tembak dirimu sendiri.",
    "Anda bisa membuat rekor dunia dengan melompat dari pesawat tanpa parasut.",
    "Berhenti berbicara BS dan melompat di depan kereta peluru yang sedang berjalan.",
    "Cobalah mandi dengan Hydrochloric Acid daripada air.",
    "Coba ini: jika Anda menahan napas di bawah air selama satu jam, Anda dapat menahannya selamanya.",
    "Go Green! Berhenti menghirup Oksigen.",
    "Tuhan sedang mencarimu. Kamu harus pergi untuk bertemu dengannya.",
    "berikan 100% mu. Sekarang, pergi donor darah.",
    "Cobalah melompat dari gedung seratus lantai tetapi Anda hanya dapat melakukannya sekali.",
    "Anda harus menyumbangkan otak Anda melihat bahwa Anda tidak pernah menggunakannya.",
    "Relawan untuk target dalam jarak tembak.",
    "Tembak kepala itu menyenangkan. Dapatkan dirimu sendiri.",
    "Anda harus mencoba berenang dengan hiu putih besar.",
    "Anda harus mengecat diri Anda dengan warna merah dan berlari dalam bull marathon.",
    "Anda bisa tetap di bawah air selama sisa hidup Anda tanpa harus kembali lagi.",
    "Bagaimana kalau kamu berhenti bernapas selama 1 hari? Itu akan bagus.",
    "Cobalah memprovokasi harimau saat kalian berdua berada di dalam sangkar.",
    "Sudahkah Anda mencoba menembak diri Anda sendiri setinggi 100m menggunakan kanon.",
    "Anda harus mencoba menahan TNT di mulut Anda dan menyalakannya.",
    "Cobalah bermain menangkap dan melempar dengan RDX itu menyenangkan.",
    "Saya dengar phogine beracun tapi saya rasa Anda tidak keberatan menghirupnya untuk bersenang-senang.",
    "Luncurkan diri Anda ke luar angkasa sambil melupakan oksigen di Bumi.",
    "Kamu harus mencoba bermain ular tangga, dengan ular sungguhan dan tanpa tangga.",
    "Menari telanjang di beberapa kabel HT.",
    "Gunung Berapi Aktif adalah kolam renang terbaik untuk Anda.",
    "Anda harus mencoba mandi air panas di gunung berapi.",
    "Cobalah untuk menghabiskan satu hari di peti mati dan itu akan menjadi milikmu selamanya.",
    "Pukul Uranium dengan neutron yang bergerak lambat di hadapanmu. Ini akan menjadi pengalaman yang berharga.",
    "Anda bisa menjadi orang pertama yang menginjak matahari. Selamat mencoba.",
]

UWUS = [
    "(・`ω´・)",
    ";;w;;",
    "owo",
    "UwU",
    ">w<",
    "^w^",
    r"\(^o\) (/o^)/",
    "( ^ _ ^)∠☆",
    "(ô_ô)",
    "~:o",
    ";-;",
    "(*^*)",
    "(>_",
    "(♥_♥)",
    "*(^O^)*",
    "((+_+))",
]

FACEREACTS = [
    "ʘ‿ʘ",
    "ヾ(-_- )ゞ",
    "(っ˘ڡ˘ς)",
    "(´ж｀ς)",
    "( ಠ ʖ̯ ಠ)",
    "(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)",
    "(งツ)ว",
    "ʚ(•｀",
    "(っ▀¯▀)つ",
    "(◠﹏◠)",
    "( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)",
    "(∩｀-´)⊃━☆ﾟ.*･｡ﾟ",
    "(⊃｡•́‿•̀｡)⊃",
    "(._.)",
    "{•̃_•̃}",
    "(ᵔᴥᵔ)",
    "♨_♨",
    "⥀.⥀",
    "ح˚௰˚づ ",
    "(҂◡_◡)",
    "ƪ(ړײ)‎ƪ​​",
    "(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ",
    "(☞ﾟヮﾟ)☞",
    "[¬º-°]¬",
    "(Ծ‸ Ծ)",
    "(•̀ᴗ•́)و ̑̑",
    "ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง",
    "ლ(•́•́ლ)",
    "ʕ •́؈•̀ ₎",
    "♪♪ ヽ(ˇ∀ˇ )ゞ",
    "щ（ﾟДﾟщ）",
    "( ˇ෴ˇ )",
    "눈_눈",
    "(๑•́ ₃ •̀๑) ",
    "( ˘ ³˘)♥ ",
    "ԅ(≖‿≖ԅ)",
    "♥‿♥",
    "◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾",
    "乁( ◔ ౪◔)「      ┑(￣Д ￣)┍",
    "( ఠൠఠ )ﾉ",
    "٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ",
    "ఠ_ఠ",
    "(づ｡◕‿‿◕｡)づ",
    "(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡",
    "(づ￣ ³￣)づ",
    "(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ",
    "t(-_-t)",
    "(ಥ⌣ಥ)",
    "ヽ༼ ಠ益ಠ ༽ﾉ",
    "༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ",
    "(⊙_◎)",
    "¿ⓧ_ⓧﮌ",
    "ಠ_ಠ",
    "(´･_･`)",
    "ᕦ(ò_óˇ)ᕤ",
    "⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",
    r"¯\_(⊙︿⊙)_/¯",
    "٩◔̯◔۶",
    "°‿‿°",
    "ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ",
    "V•ᴥ•V",
    "q(❂‿❂)p",
    "ಥ_ಥ",
    "ฅ^•ﻌ•^ฅ",
    "ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）",
    "ಠ‿ಠ",
    "ヽ(´▽`)/",
    "ᵒᴥᵒ#",
    "( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)",
    "ヽ(´ー｀)ノ",
    "☜(⌒▽⌒)☞",
    "ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)",
    "┬─┬⃰͡ (ᵔᵕᵔ͜ )",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ",
    "(`･ω･´)",
    "ʕ•ᴥ•ʔ",
    "ლ(｀ー´ლ)",
    "ʕʘ̅͜ʘ̅ʔ",
    "（　ﾟДﾟ）",
    r"¯\(°_o)/¯",
    "(｡◕‿◕｡)",
]

RUNS_STR = [
    "Berlari ke Thanos..",
    "Berlari jauh, jauh dari bumi..",
    "Berlari lebih cepat dari Bolt karena aku pengguna bot !!",
    "Berlari ke Mia Khalifa..",
    "Grup ini terlalu berbahaya untuk ditangani, aku harus lari.",
    "`Berlari Dari Orang Yang Bau Sawi 😬`",
    "Aku sangat lelah untuk berlari dan mengejarmu 💔",
    "Aku pergi dulu",
    "Saya hanya berjalan pergi, karena saya terlalu gemuk untuk lari.",
    "Saya Cape!",
    "Larii Disini Bau Sawii 😭",
    "Saya lari karena saya sangat gabut.",
    "Lari... \nkarena diet bukanlah pilihan.",
    "Berlari Cepat Dari Orang Gila",
    "Lari... \nAda Wibuu...",
    "Jika kamu ingin menangkapku, kamu harus cepat... \nJika kamu ingin tinggal bersamaku, kamu harus menjadi orang yang baik... \nTapi jika kamu ingin melewati aku... \nKamu pasti bercanda. ",
    "Siapapun dapat berlari seratus meter, itu hitungan empat puluh dua ribu dua ratus berikutnya.",
    "Mengapa semua orang ini mengikuti saya?",
    "Apakah anak-anak masih mengejarku?",
    "Berlari Sekencang Super Dede.. Apakah Sopan Begitu?",
]

CHASE_STR = [
    "Menurutmu kemana kamu akan pergi?",
    "Hah? Apa? Apakah mereka lolos?",
    "ZZzzZZzz... Hah? Apa? Oh, hanya mereka lagi, lupakan.",
    "Kembali kesini!",
    "Tidak terlalu cepat...",
    "Awas ke dinding!",
    "Jangan tinggalkan aku sendiri dengan mereka !!",
    "Kamu lari, kamu mati.",
    "Bercanda, aku ada dimana-mana",
    "Kamu akan menyesali itu ...",
    "Kamu juga bisa mencoba /kickme, kudengar itu menyenangkan.",
    "Ganggu orang lain, tidak ada yang peduli.",
    "Kamu bisa lari, tapi kamu tidak bisa bersembunyi.",
    "Apakah hanya itu yang kamu punya?",
    "Saya di belakang Anda...",
    "Anda punya teman!",
    "Kita bisa melakukan ini dengan cara mudah, atau cara sulit.",
    "Anda tidak mengerti, bukan?",
    "Ya, sebaiknya kau lari!",
    "Tolong, ingatkan saya apakah saya peduli?",
    "Aku akan lari lebih cepat jika jadi kamu.",
    "Itu pasti droid yang kami cari.",
    "Semoga peluang selalu menguntungkan Anda.",
    "Kata-kata terakhir yang terkenal.",
    "Dan mereka menghilang selamanya, tidak pernah terlihat lagi.",
    "Oh, lihat aku! Saya sangat keren, saya bisa lari dari bot orang ini",
    "Ya ya, cukup ketuk /kickme.",
    "Ini, ambil cincin ini dan pergilah ke Mordor saat kamu melakukannya.",
    "Legenda mengatakan, mereka masih berjalan...",
    "Tidak seperti Harry Potter, orang tuamu tidak bisa melindungimu dariku.",
    "Ketakutan menyebabkan kemarahan. Kemarahan mengarah pada kebencian. Kebencian menyebabkan penderitaan. Jika Anda terus berlari dalam ketakutan, Anda mungkin"
    "jadilah Vader berikutnya.",
    "Beberapa kalkulasi nanti, saya telah memutuskan minat saya pada kejahatan Anda tepat 0.",
    "Legenda mengatakan, mereka masih berjalan.",
    "Teruskan, kami tidak yakin kami menginginkanmu di sini.",
    "Kamu seorang penyihir- Oh. Tunggu. Kamu bukan Harry, terus bergerak.",
    "JANGAN BERLARI DI SINI!",
    "Hasta la vista, sayang.",
    "Siapa yang membiarkan anjing keluar?",
    "Ini lucu, karena tidak ada yang peduli.",
    "Ah, sayang sekali, Aku suka yang itu.",
    "Terus terang, sayangku, aku tidak peduli.",
    "Milkshake saya membawa semua anak laki-laki ke halaman... Jadi lari lebih cepat!",
    "Anda tidak bisa MENANGANI kebenaran!",
    "Dahulu kala, di galaksi yang sangat jauh... Seseorang akan peduli tentang itu, Tapi sekarang tidak lagi.",
    "Hei, lihat mereka! Mereka lari dari palu yang tak terelakkan... Manis.",
    "Han menembak lebih dulu, Aku juga.",
    "Apa yang kamu kejar, kelinci putih?",
    "Seperti yang dikatakan The Doctor... LARI!",
]

HELLOSTR = [
    "Hemblo..👋",
    "'Eyyoo..",
    "Gabutkah kalian?",
    "Apa kabarmu hari ini?",
    "Eyyo, apa kabar hatimu disana?",
    "Eyyo, siapa di sana, saya sedang berbicara disini.",
    "Kamu tahu siapa aku?",
    "Yoi bruh",
    "Wassup Gang",
    "Hah??",
    "Eyyo, sinar mentari pagiku..",
    "Hello epribadeh, sehat?",
    "Hmm.. Sepi kali disini",
    "Ciluk ba!",
    "Bagaimana kabar hati kalian hari ini?",
    "Hayyo, member baru",
    "Saya datang dengan damai dan sehat",
    "Ahoy, sobat!",
    "Hiya Ha..!!",
]

SHGS = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

CRI = [
    "أ‿أ",
    "╥﹏╥",
    "(;﹏;)",
    "(ToT)",
    "(┳Д┳)",
    "(ಥ﹏ಥ)",
    "（；へ：）",
    "(T＿T)",
    "（πーπ）",
    "(Ｔ▽Ｔ)",
    "(⋟﹏⋞)",
    "（ｉДｉ）",
    "(´Д⊂ヽ",
    "(;Д;)",
    "（>﹏<）",
    "(TдT)",
    "(つ﹏⊂)",
    "༼☯﹏☯༽",
    "(ノ﹏ヽ)",
    "(ノAヽ)",
    "(╥_╥)",
    "(T⌓T)",
    "(༎ຶ⌑༎ຶ)",
    "(☍﹏⁰)｡",
    "(ಥ_ʖಥ)",
    "(つд⊂)",
    "(≖͞_≖̥)",
    "(இ﹏இ`｡)",
    "༼ಢ_ಢ༽",
    "༼ ༎ຶ ෴ ༎ຶ༽",
]

SLAP_TEMPLATES_EN = [
    "{hits} {victim} dengan {item}.",
    "{hits} {victim} di wajah dengan {item}.",
    "{hits} {victim} sekitar sedikit dengan {item}.",
    "{throws} {item} ke {Victim}.",
    "mengambil {item} dan {throws} ke wajah {victim}.",
    "Menusuk {victim} dengan tombak cinta.",
    "{throws} beberapa {item} ke {victim}.",
    "mengambil {item} dan {throws} ke wajah {victim}.",
    "meluncurkan {item} ke arah umum {korban}.",
    "duduk di wajah {victim} sambil membanting {item}.",
    "mulai menampar {victim} dengan konyol dengan {item}.",
    "pin {victim} ke bawah dan berulang kali {hits} mereka dengan {item}.",
    "mengambil {item} dan {hits} {victim} dengannya.",
    "mulai menampar {victim} dengan konyol dengan {item}.",
    "menahan {victim} dan berulang kali {hits} mereka dengan {item}.",
    "memukul {victim} dengan {item}.",
    "mengambil {item} dan {hits} {victim} dengannya.",
    "mengikat {victim} ke kursi dan {throws} {item} padanya.",
    "{hits} {victim} {where} dengan {item}.",
    "mengikat {victim} ke tiang dan mencambuk mereka {where} dengan {item}."
    "memberikan dorongan ramah untuk membantu {victim} belajar berenang di lahar.",
    "mengirim {victim} ke /laut /lahar.",
    "mengirim {victim} ke lubang pembuangan.",
    "memenggal {victim}.",
    "melemparkan {victim} dari sebuah gedung.",
    "mengganti semua musik {victim} dengan lagu tahun 50n.",
    "spam email {victim}.",
    "membuat {victim} depresi.",
    "menampar {victim} tanpa apa-apa.",
    "pukul {victim} dengan gagang pesawat telfon.",
    "memukul kepala {victim}.",
    "taruh {victim} di tong sampah.",
    "Menendang {victim} dan melemparnya ke sungai.",
    "letakkan {victim} di rumah hantu.",
    "menampar {victim} dengan tongkat besi!",
]

ITEMS_EN = [
    "Tabung Gas",
    "Televisi 69 In",
    "Egrang",
    "Raket Nyamuk",
    "Gelas Kaca",
    "Buku",
    "Linggis",
    "Telur Busuk",
    "Jarum Jam",
    "Bayi Tabung",
    "Obeng",
    "Almunium",
    "Emas",
    "Printer",
    "Toa Masjid",
    "Gas Elpiji",
    "Pom PERTAMINI",
    "Tandon Air",
    "Bola Bowling",
    "Laptop",
    "Ambulance Kopid",
    "Wajan Bekas Gorengan",
    "Virus Karona",
    "Meja Kantor",
    "Meja KUA",
    "Lemari",
    "Ember Besi",
    "Besi Beton",
    "Timah Panas",
    "Harimau",
    "Batu Krikil",
    "Makanan Basi",
    "Pesawat AirBus",
    "Roket Owner",
    "Satelit Nasa",
    "Matahari",
    "Meteor",
    "Berkas Kantor",
    "Beton panas",
    "Cermin",
    "Batu Giok",
    "Botol Mijon",
    "Nezuko",
    "Kaset Pita",
    "Tiang Jemuran",
    "Pisau Lipat",
    "Es Cristal Cup",
    "Asteroid",
]

THROW_EN = [
    "melempar",
    "melemparkan",
]

HIT_EN = [
    "memukul",
    "menendang",
    "menampar",
    "memukul",
    "melempar",
]

WHERE_EN = ["di pipi", "di kepala", "di pantat", "di badan"]

# ID translation by @yincen
SLAP_TEMPLATES_ID = [
    "{hits} {victim} dengan {item}.",
    "{throws} sebuah  {item} kepada {victim}.",
    "mengambil  {item} dan {hits} {victim} .",
    "Mengambil Sebuah {item} dan {hits} {victim} Dengan itu.",
    "Menjatuhkan {victim} Ke Lava.",
    "Mengirimkan {victim} ke Kawah.",
    "Membuang {victim} Ke Laut.",
    "Mengeluarkan {victim} Dari Bumi.",
    "Melempar {victim} Ke luar angkasa.",
    "Menaruh {victim} di Pluto.",
    "Melemparkan sebuah {item} ke {victim}.",
    "Melemparkan {item} kepada {victim}.",
    "Menampar {victim} menggunakan {item}.",
    "Membuang {victim} Ke udara.",
    "Menghapus {victim} Dari Daftar Teman.",
    "Melemparkan {item} {where} {victim}.",
    "Meletakan {item} {where} {victim}.",
    "Menyerang {victim} menggunakan {anime}.",
    "Mengehack Seluruh akun {victim}",
]

ITEMS_ID = [
    "Tabung Gas",
    "Televisi 69 In",
    "Egrang",
    "Raket Nyamuk",
    "Gelas Kaca",
    "Buku",
    "Linggis",
    "Telur Busuk",
    "Jarum Jam",
    "Bayi Tabung",
    "Obeng",
    "Almunium",
    "Emas",
    "Printer",
    "Toa Masjid",
    "Gas Elpiji",
    "Pom PERTAMINI",
    "Tandon Air",
    "Bola Bowling",
    "Laptop",
    "Ambulance Kopid",
    "Wajan Bekas Gorengan",
    "Virus Karona",
    "Meja Kantor",
    "Meja KUA",
    "Lemari",
    "Ember Besi",
    "Besi Beton",
    "Timah Panas",
    "Harimau",
    "Batu Krikil",
    "Makanan Basi",
    "Pesawat AirBus",
    "Roket Owner",
    "Satelit Nasa",
    "Matahari",
    "Meteor",
    "Berkas Kantor",
    "Beton panas",
    "Cermin",
    "Batu Giok",
    "Botol Mijon",
    "Nezuko",
    "Kaset Pita",
    "Tiang Jemuran",
    "Pisau Lipat",
    "Es Cristal Cup",
    "Asteroid",
]

THROW_ID = [
    "Melempar",
    "Melemparkan",
    "Mematak",
]

HIT_ID = [
    "Memukul",
    "melemparkan",
    "Memukuli",
    "Membogem",
]

WHERE_ID = ["di pipi", "di kepala", "di bokong", "di badan"]


SLAP_TEMPLATES_Jutsu = [
    "Menyerang {victim} Menggunakan {hits}.",
    "Menyerang {victim} Menggunakan {item}.",
    "Melemparkan {throws} kepada {victim} .",
    "Melemparkan {throws} {where} {victim}.",
]

ITEMS_Jutsu = [
    "KAA MEE HAA MEE HAA",
    "Chibaku Tensei",
    "Amaterasu",
]

THROW_Jutsu = [
    "Futon Rasen Shuriken",
    "Shuriken",
]

HIT_Jutsu = [
    "Rasengan",
    "Chidori",
]


WHERE_Jutsu = ["Di Pipi", "Di Kepala", "Di Bokong", "Di Badan ,Di Pantat"]


HILIH = [
    "┐(´д｀)┌",
    "┐(´～｀)┌",
    "┐(´ー｀)┌",
    "┐(￣ヘ￣)┌",
    "╮(╯∀╰)╭",
    "╮(╯_╰)╭",
    "┐(´д`)┌",
    "┐(´∀｀)┌",
    "ʅ(́◡◝)ʃ",
    "┐(ﾟ～ﾟ)┌",
    "┐('д')┌",
    "┐(‘～`;)┌",
    "ヘ(´－｀;)ヘ",
    "┐( -“-)┌",
    "ʅ（´◔౪◔）ʃ",
    "ヽ(゜～゜o)ノ",
    "ヽ(~～~ )ノ",
    "┐(~ー~;)┌",
    "┐(-。ー;)┌",
    r"¯\_(ツ)_/¯",
    r"¯\_(⊙_ʖ⊙)_/¯",
    r"¯\_༼ ಥ ‿ ಥ ༽_/¯",
    "乁( ⁰͡  Ĺ̯ ⁰͡ ) ㄏ",
]

GAMBAR_LOP = """
──────(♥)(♥)──────(♥)(♥)  ─𝙂
────(♥)(♥)(♥)────(♥)(♥)(♥)  ─𝙀
──(♥)██████(♥)(♥)██████(♥)  ─𝙈
─(♥)████████(♥)████████(♥)  ─𝙊
─(♥)██████████████████(♥)  ─𝙔
──(♥)████████████████(♥)  ─𝙐
────(♥)████████████(♥)  ──𝙎
──────(♥)████████(♥)  ──𝙀
────────(♥)████(♥)  ──𝙍
─────────(♥)██(♥)  ──𝘽
───────────(♥)  ──𝙊
──────────(♥) ──𝙏
"""

AENJEAYE = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⣠⣶⣿⣿⣶⣄⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠻⣿⣿⣿⣿⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠉⠉⠀⠀⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠙⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠁⣠⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⡏⠉⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⣠⣶⣿⣿⣶⣄⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠻⣿⣿⣿⣿⠟⠀⣸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⠀⠀⠉⠉⠀⠀⠉⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠉⠛⠛⠋⠉⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠉⠛⠛⠋⠉⠀⣀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣦⣄⣀⠉⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

# ===========================================


@register(outgoing=True, pattern=r"^\.anjay$")
async def anjay(njay):
    await njay.edit(AENJEAYE)


@register(outgoing=True, pattern=r"^\.(\w+)say (.*)")
async def univsaye(cowmsg):
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$", ignore_unsafe=True)
async def kek(keks):
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern=r"^\.coinflip (.*)")
async def coin(event):
    r = choice(["heads", "tails"])
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r == "heads":
        if input_str == "heads":
            await event.edit("Koin mendarat di: **KEPALAMU**.\\Anda benar.")
        elif input_str == "tails":
            await event.edit(
                "Koin mendarat di: **KEPALAMU**.\nAnda salah, coba lagi ..."
            )
        else:
            await event.edit("Koin mendarat di: **KEPALAMU**.")
    elif r == "tails":
        if input_str == "tails":
            await event.edit("Koin mendarat di: **PANTAT**.\\Anda benar.")
        elif input_str == "heads":
            await event.edit(
                "Koin mendarat di: **PANTAT**.\nAnda salah, coba lagi ..."
            )
        else:
            await event.edit("Koin mendarat di: **PANTAT**.")


@register(pattern=r"^\.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    replied_user = await get_user_from_event(event)
    if replied_user:
        replied_user = replied_user[0]
    else:
        return
    caption = await slap(replied_user, event)

    try:
        await event.edit(caption)

    except BaseException:
        await event.edit(
            "`Can't slap this person, need to fetch some sticks and stones !!`"
        )


async def slap(replied_user, event):
    user_id = replied_user.id
    first_name = replied_user.first_name
    username = replied_user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"
    slap_str = event.pattern_match.group(1)
    if slap_str == "en" or slap_str != "id" and slap_str != "jutsu":
        temp = choice(SLAP_TEMPLATES_EN)
        item = choice(ITEMS_EN)
        hit = choice(HIT_EN)
        throw = choice(THROW_EN)
        where = choice(WHERE_EN)
    elif slap_str == "id":
        temp = choice(SLAP_TEMPLATES_ID)
        item = choice(ITEMS_ID)
        hit = choice(HIT_ID)
        throw = choice(THROW_ID)
        where = choice(WHERE_ID)
    else:
        temp = choice(SLAP_TEMPLATES_Jutsu)
        item = choice(ITEMS_Jutsu)
        hit = choice(HIT_Jutsu)
        throw = choice(THROW_Jutsu)
        where = choice(WHERE_Jutsu)
    return "..." + temp.format(
        victim=slapped, item=item, hits=hit, throws=throw, where=where
    )


@register(outgoing=True, pattern="^-_-$", ignore_unsafe=True)
async def llol(lel):
    okay = "-_-"
    for _ in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern=r"^\.(yes|no|maybe|decide)$")
async def decide(event):
    decision = event.pattern_match.group(1).lower()
    message_id = event.reply_to_msg_id if event.reply_to_msg_id else None
    if decision != "decide":
        r = requests.get(f"https://yesno.wtf/api?force={decision}").json()
    else:
        r = requests.get("https://yesno.wtf/api").json()
    await event.delete()
    await event.client.send_message(
        event.chat_id, str(r["answer"]).upper(), reply_to=message_id, file=r["image"]
    )


@register(outgoing=True, pattern="^;_;$", ignore_unsafe=True)
async def fun(e):
    t = ";_;"
    for _ in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\.fp$")
async def facepalm(e):
    await e.edit("🤦‍♂")


@register(outgoing=True, pattern=r"^\.cry$")
async def cry(e):
    await e.edit(choice(CRI))


@register(outgoing=True, pattern=r"^\.insult$")
async def insult(e):
    await e.edit(choice(INSULT_STRINGS))


@register(outgoing=True, pattern=r"^\.cp(?: |$)(.*)")
async def copypasta(cp_e):
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            reply_text += owo.upper() if bool(getrandbits(1)) else owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern=r"^\.vapor(?: |$)(.*)")
async def vapor(vpr):
    reply_text = []
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.str(?: |$)(.*)")
async def stretch(stret):
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")

    count = randint(3, 10)
    reply_text = sub(
        r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
        (r"\1" * count),
        message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern=r"^\.zal(?: |$)(.*)")
async def zal(zgfy):
    reply_text = []
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(3):
            textz = randint(0, 2)

            if textz == 0:
                charac = charac.strip() + choice(ZALG_LIST[0]).strip()
            elif textz == 1:
                charac = charac.strip() + choice(ZALG_LIST[1]).strip()
            else:
                charac = charac.strip() + choice(ZALG_LIST[2]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.hello$")
async def hoi(hello):
    await hello.edit(choice(HELLOSTR))


@register(outgoing=True, pattern=r"^\.owo(?: |$)(.*)")
async def focos(owo):
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await owo.edit("` UwU tidak ada teks yang diberikan! `")

    reply_text = sub(r"(r|l)", "w", message)
    reply_text = sub(r"(R|L)", "W", reply_text)
    reply_text = sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern=r"^\.ii(?: |$)(.*)")
async def faces(ii):
    textx = await ii.get_reply_message()
    message = ii.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await ii.edit("` Hilih tidak ada teks yang diberikan! `")
        return

    reply_text = sub(r"(a|i|u|e|o)", "i", message)
    reply_text = sub(r"(A|I|U|E|O)", "I", reply_text)
    reply_text = sub(r"\!+", " " + choice(HILIH), reply_text)
    reply_text += " " + choice(HILIH)
    await ii.edit(reply_text)


@register(outgoing=True, pattern=r"^\.hai$")
async def sayhi(e):
    await e.edit(
        "\n✨✨✨✨✨✨✨✨✨✨✨✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️❤️❤️❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️❤️❤️❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨❤️❤️✨✨❤️❤️✨✨❤️❤️✨"
        "\n✨✨✨✨✨✨✨✨✨✨✨✨")


@register(outgoing=True, pattern=r"^\.react$")
async def react_meme(react):
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=r"^\.shg$")
async def shrugger(shg):
    await shg.edit(choice(SHGS))


@register(outgoing=True, pattern=r"^\.chase$")
async def police(chase):
    await chase.edit(choice(CHASE_STR))


@register(outgoing=True, pattern=r"^\.run$")
async def runner_lol(run):
    await run.edit(choice(RUNS_STR))


@register(outgoing=True, pattern=r"^\.metoo$")
async def metoo(hahayes):
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for _ in range(15):
        t = t[:-1] + "of"
        await e.edit(t)


@register(outgoing=True, pattern=r"^\.10iq$")
async def iqless(e):
    await e.edit("♿")


@register(outgoing=True, pattern=r"^\.fuck$")
async def iqbot(e):
    await e.edit("🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕🖕🖕🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕\n🖕🖕")


@register(outgoing=True, pattern=r"^\.bye$")
async def iqboot(e):
    await e.edit("Kek, Terima Kasih Sama Sama")


@register(outgoing=True, pattern=r"^\.moon$")
async def moon(event):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.earth$")
async def earth(event):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.clock$")
async def clock(event):
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.rain$")
async def rain(event):
    deq = deque(list("☀️🌤⛅️🌥☁️🌧⛈"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.love$")
async def love(event):
    deq = deque(list("❤️🧡💛💚💙💜🖤💕💞💓💗💖💘💝"))
    try:
        for _ in range(32):
            await sleep(0.1)
            await event.edit("".join(deq))
            deq.rotate(1)
    except BaseException:
        return


@register(outgoing=True, pattern=r"^\.mock(?: |$)(.*)")
async def spongemocktext(mock):
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await mock.edit("`MEMBERI SESUATU UNTUK MENJEMPUT!`")

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern=r"^\.clap(?: |$)(.*)")
async def claptext(memereview):
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await memereview.edit("`Hah, aku tidak bertepuk tangan sia-sia!`")
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=r"^\.bt$")
async def bluetext(bt_e):
    if await bt_e.get_reply_message() and bt_e.is_group:
        await bt_e.edit(
            "/BLUETEXT /MUST /CLICK.\n"
            "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?"
        )


@register(outgoing=True, pattern=r"^\.f (.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await event.edit(pay)


@register(outgoing=True, pattern=r"^\.lfy (.*)")
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {"format": "json", "url": lfy_url}
    r = requests.get("http://is.gd/create.php", params=payload)
    await lmgtfy_q.edit(
        "Here you are, help yourself." f"\n[{query}]({r.json()['shorturl']})"
    )


@register(pattern=r"\.scam(?: |$)(.*)", outgoing=True)
async def scam(event):
    options = [
        "typing",
        "contact",
        "game",
        "location",
        "voice",
        "round",
        "video",
        "photo",
        "document",
        "cancel",
    ]
    input_str = event.pattern_match.group(1)
    args = input_str.split()
    if len(args) == 0:  # Let bot decide action and time
        scam_action = choice(options)
        scam_time = randint(30, 60)
    elif len(args) == 1:  # User decides time/action, bot decides the other.
        try:
            scam_action = str(args[0]).lower()
            scam_time = randint(30, 60)
        except ValueError:
            scam_action = choice(options)
            scam_time = int(args[0])
    elif len(args) == 2:  # User decides both action and time
        scam_action = str(args[0]).lower()
        scam_time = int(args[1])
    else:
        await event.edit("`Invalid Syntax !!`")
        return
    try:
        if scam_time > 0:
            await event.delete()
            async with event.client.action(event.chat_id, scam_action):
                await sleep(scam_time)
    except BaseException:
        return


@register(pattern=r"\.type(?: |$)(.*)", outgoing=True)
async def typewriter(typew):
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        return await typew.edit("`Give a text to type!`")
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ""
    await typew.edit(typing_symbol)
    await sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await sleep(sleep_time)
        await typew.edit(old_text)
        await sleep(sleep_time)


@register(outgoing=True, pattern=r"^\.leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`Anda harus Keluar dari Grup kek!`")


@register(outgoing=True, pattern=r"^\.fail$")
async def fail(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `"
            "`\n████▌▄▌▄▐▐▌█████ `"
            "`\n████▌▄▌▄▐▐▌▀████ `"
            "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `"
        )


@register(outgoing=True, pattern=r"^\.lol$")
async def leol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n░█░░░█▀█░█░░ `"
            "\n░█░░░█░█░█░░ `"
            "\n░▀▀▀░▀▀▀░▀▀▀ `"
        )


@register(outgoing=True, pattern=r"^\.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
            "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
            "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
        )


@register(outgoing=True, pattern=r"^\.stfu$")
async def stfu(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n██████████████████████████████`"
            "`\n██▀▀▀▀████▀▀▀▀████▀▀▀▀▀███▀▀██▀▀█`"
            "`\n█──────██──────██───────██──██──█`"
            "`\n█──██▄▄████──████──███▄▄██──██──█`"
            "`\n█▄────▀████──████────█████──██──█`"
            "`\n█▀▀██──████──████──███████──██──█`"
            "`\n█──────████──████──███████──────█`"
            "`\n██▄▄▄▄█████▄▄████▄▄████████▄▄▄▄██`"
            "`\n█████████████████████████████████`"
        )


@register(outgoing=True, pattern=r"^\.gtfo$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n███████████████████████████████ `"
            "`\n█▀▀▀▀▀▀▀█▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀█ `"
            "`\n█───────█──────█───────█──────█ `"
            "`\n█──███──███──███──███▄▄█──██──█ `"
            "`\n█──███▄▄███──███─────███──██──█ `"
            "`\n█──██───███──███──██████──██──█ `"
            "`\n█──▀▀▀──███──███──██████──────█ `"
            "`\n█▄▄▄▄▄▄▄███▄▄███▄▄██████▄▄▄▄▄▄█ `"
            "`\n███████████████████████████████ `"
        )


@register(outgoing=True, pattern=r"^\.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            r"`(\_/)`"
            "`\n(•_•)`"
            "`\n >🌹 *ini buat kamu`"
            "`\n`"
            r"`(\_/)`"
            "`\n(•_•)`\n"
            r"`🌹<\ *𝗧𝗔𝗣𝗜 𝗕𝗢𝗢𝗡𝗚`"
        )


@register(outgoing=True, pattern=r"^\.fag$")
async def fgtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n█████████`"
            "`\n█▄█████▄█`"
            "`\n█▼▼▼▼▼`"
            "`\n█       𝗥𝗔𝗔𝗔𝗔𝗔𝗪𝗥𝗥𝗥`"
            "`\n█▲▲▲▲▲`"
            "`\n█████████`"
            "`\n ██   ██`"
        )


@register(outgoing=True, pattern=r"^\.taco$")
async def taco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(r"{\__/}" "\n(●_●)" "\n( >🌮 Want a taco?")


@register(outgoing=True, pattern=r"^\.paw$")
async def paw(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern=r"^\.tf$")
async def tf(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@register(outgoing=True, pattern=r"^\.gey$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
            "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
            "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈NIGGA YOU GEY`"
            "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
        )


@register(outgoing=True, pattern=r"^\.gay$")
async def ghey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
            "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
            "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈ANDA GAY`"
            "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
        )


@register(outgoing=True, pattern=r"^\.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
            "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
        )


@register(outgoing=True, pattern=r"^\.hey$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
            "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
            "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`"
        )


@register(outgoing=True, pattern=r"^\.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
            "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
            "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
            "`\n┗━━┻━┛`"
        )


@register(outgoing=True, pattern=r"^\.koc$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8✊===D")
        await e.edit("8=✊==D")
        await e.edit("8==✊=D")
        await e.edit("8===✊D")
        await e.edit("8==✊=D")
        await e.edit("8=✊==D")
        await e.edit("8===✊D💦")
        await e.edit("8==✊=D💦💦")
        await e.edit("8=✊==D💦💦💦")
        await e.edit("8✊===D💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦")
        await e.edit("8=✊==D💦💦💦💦💦💦💦")
        await e.edit("8✊===D💦💦💦💦💦💦💦💦")
        await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
        await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
        await e.edit("8=✊==D Lah Kok Habis?")
        await e.edit("𝗧𝗢𝗕𝗔𝗧 𝗞𝗔 𝗧𝗢𝗕𝗔𝗧 😭😭😭😭")


@register(outgoing=True, pattern=r"^\.(?:lop|lop)\s?(.)?")
async def emoji_lop(e):
    emoji = e.pattern_match.group(1)
    lop = GAMBAR_LOP
    if emoji:
        lop.replace("😂", emoji)
    await e.edit(lop)


CMD_HELP.update(
    {
        "animasi2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cowsay`"
        "\nPenggunaan: sapi yang mengatakan sesuatu."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `:/`"
        "\nPenggunaan: Cek sendiri ;)"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `-_-`"
        "\nPenggunaan: Ok..."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `;_;`"
        "\nPenggunaan: Seperti `-_-` tapi menangis."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cp`"
        "\nPenggunaan: Copypasta meme yang terkenal"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vapor`"
        "\nPenggunaan: Menguap semuanya!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.str`"
        "\nPenggunaan: Regangkan."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.10iq`"
        "\nPenggunaan: Kamu bodoh !!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.zal`"
        "\nPenggunaan: Menimbulkan perasaan kacau."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Oem`"
        "\nPenggunaan: Oeeeem"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Oof`"
        "\nPenggunaan: Ooooof"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fp`"
        "\nPenggunaan: Telapak tangan :P"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.moon`"
        "\nPenggunaan: animasi bulan kensar."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.clock`"
        "\nPenggunaan: animasi jam kensar."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.hai`"
        "\nPenggunaan: Salam semua!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.coinflip <heads/tails>`"
        "\nPenggunaan: Lempar koin !!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.owo`"
        "\nPenggunaan: UwU"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.react`"
        "\nPenggunaan: Buat userbot Anda bereaksi terhadap semuanya."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.slap` `.slap id` `.slap jutsu`"
        "\nPenggunaan: membalas menampar mereka dengan benda-benda acak!!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.cry`"
        "\nPenggunaan: y u du dis, i cri."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.shg`"
        "\nPenggunaan: Angkat bahu itu!!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.run`"
        "\nPenggunaan: Biarkan Aku Lari, lari, LARI!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.chase`"
        "\nPenggunaan: Lebih baik kamu mulai berlari"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.metoo`"
        "\nPenggunaan: Haha iya"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mock`"
        "\nPenggunaan: Lakukan dan temukan kesenangan yang sesungguhnya."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.clap`"
        "\nPenggunaan: Puji orang!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.f <emoji/character>`"
        "\nPenggunaan: Beri Hormat."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.bt`"
        "\nPenggunaan: Percayalah, Anda akan menemukan ini berguna."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.type`"
        "\nPenggunaan: Hanya perintah kecil untuk membuat keyboard Anda menjadi mesin tik!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.lfy <query>`"
        "\nPenggunaan: Biarkan saya Google itu untuk Anda dengan sangat cepat!!"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.decide` alternates <.yes, .no, .maybe>"
        "\nPenggunaan: Cepat ambil keputusan."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.scam <action> <time>`"
        "\nTindakan yang Tersedia <mengetik, kontak, permainan, lokasi, suara, putaran, video, foto, dokumen, batal>"
        "\nPenggunaan: Buat tindakan obrolan palsu, untuk bersenang-senang. <Tindakan default: mengetik>"
        "\nDan Banyak Lagi..."
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.nou | .bot | .gey | .gay | .tf | .paw | .taco | .nih | .ii`"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.fag | .gtfo | .stfu | .lol | .lool | .fail | .leave"
        "\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.love | .lop | .rain | .earth | .fuck | .oke | .koc | .anjay`"
        "\nPenggunaan: Silakan Explore sendiri weh."})
