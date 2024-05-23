from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

helpmenu = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴘʟᴀʏ", callback_data="clone_cb play"),
            InlineKeyboardButton(text="ᴛᴇʟᴇɢʀᴀᴘʜ", callback_data="clone_cb telegraph"),
            InlineKeyboardButton(text="ɢᴏᴏɢʟᴇ", callback_data="clone_cb google"),
        ],
        [
            InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="clone_home"),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ],
)

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)

close_key = [

    [

        InlineKeyboardButton(
            text="𝗘𝗻𝗱 🎸•",
            callback_data="end_cb"
        ),
        InlineKeyboardButton(
            text="𝗣𝗮𝘂𝘀𝗲 🎸•",
            callback_data="pause_cb"
        ),
        InlineKeyboardButton(
            text="𝗥𝗲𝘀𝘂𝗺𝗲 🎸•",
            callback_data="resume_cb",
        ),
    ],
    [
        InlineKeyboardButton(
            text=_["P_B_2"],
            callback_data=f"downloadvideo {videoid}"),
        InlineKeyboardButton(
            text=_["P_B_1"],
            callback_data=f"downloadaudio {videoid}")
    ],
    [
        InlineKeyboardButton(
            text="زیادم بکە بۆ گرووپ یان کەناڵت ⚡️•",
            url=f"https://t.me/{viv.username}?startgroup=true",
),
],
]
