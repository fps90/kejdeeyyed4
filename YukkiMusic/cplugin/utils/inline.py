from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config

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


strem1  = [

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
            text="𝗖𝗵𝗮𝗻𝗻𝗲𝗹 💸•",
            url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(
            text="𝗚𝗿𝗼𝘂𝗽 💸•",
            url=config.SUPPORT_GROUP)
    ],
    [
        InlineKeyboardButton(
            text="خاوەنی بۆت 🎸",
            url=f"https://t.me/IQ7amo",
),
],
]
