#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
import math
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic.utils.formatters import time_to_seconds
from config import SUPPORT_CHANNEL

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
            text="𝗘𝗻𝗱",
            callback_data=f"ADMIN Stop|{chat_id}"
        ),
        InlineKeyboardButton(
            text="𝗣𝗮𝘂𝘀𝗲",
            callback_data=f"ADMIN Pause|{chat_id}"
        ),
        InlineKeyboardButton(
            text="𝗥𝗲𝘀𝘂𝗺𝗲",
            callback_data=f"ADMIN Resume|{chat_id}",
        ),
    ],
    [
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"downloadvideo {videoid}"),
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"downloadaudio {videoid}",
            ),
        ],
        [
            InlineKeyboardButton(text="𝗠𝘂𝘁𝗲", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(
                text="𝗨𝗻𝗺𝘂𝘁𝗲", callback_data=f"ADMIN Unmute|{chat_id}"
            ),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL)],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [

    [

        InlineKeyboardButton(
            text="𝗘𝗻𝗱",
            callback_data=f"ADMIN Stop|{chat_id}"
        ),
        InlineKeyboardButton(
            text="𝗣𝗮𝘂𝘀𝗲",
            callback_data=f"ADMIN Pause|{chat_id}"
        ),
        InlineKeyboardButton(
            text="𝗥𝗲𝘀𝘂𝗺𝗲",
            callback_data=f"ADMIN Resume|{chat_id}",
        ),
    ],
    [
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"downloadvideo {videoid}"),
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"downloadaudio {videoid}",
            ),
        ],
        [
            InlineKeyboardButton(text="𝗠𝘂𝘁𝗲", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(
                text="𝗨𝗻𝗺𝘂𝘁𝗲", callback_data=f"ADMIN Unmute|{chat_id}"
            ),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], url=SUPPORT_CHANNEL)],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 40:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 50 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="𝗠𝘂𝘁𝗲", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(
                text="𝗨𝗻𝗺𝘂𝘁𝗲", callback_data=f"ADMIN Unmute|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close"),
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="𝗠𝘂𝘁𝗲", callback_data=f"ADMIN Mute|{chat_id}"),
            InlineKeyboardButton(
                text="𝗨𝗻𝗺𝘂𝘁𝗲", callback_data=f"ADMIN Unmute|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text=text="〆 ᴄʟᴏsᴇ 〆", callback_data="close"),
        ],
    ]
    return buttons


## By Anon
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")]]
)

## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"YukkiPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")],
    ]
    return buttons
