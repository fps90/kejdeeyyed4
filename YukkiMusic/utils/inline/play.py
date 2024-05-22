import math
from typing import Union
from pyrogram.types import InlineKeyboardButton

from YukkiMusic.utils.formatters import time_to_seconds

from YukkiMusic import app

def track_markup(_, user_id, channel, fplay):
    buttons = [

        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],

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
            InlineKeyboardButton(text="𝖱𝖾𝗉𝗅𝖺𝗒", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="𝖤𝗇𝖽", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["ALINA"],
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
        ],
    ]

    return buttons


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

    buttons  = [

        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],

        [
            InlineKeyboardButton(
                text="II 𝖯𝖺𝗎𝗌𝖾",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),

            InlineKeyboardButton(
                text="▢ 𝖲𝗍𝗈𝗉", callback_data=f"ADMIN Stop|{chat_id}"
            ),

            InlineKeyboardButton(
                text="𝖲𝗄𝗂𝗉 ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="▷ 𝖱𝖾𝗌𝗎𝗆𝖾", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝖱𝖾𝗉𝗅𝖺𝗒 ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["HOME"],
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons


def stream_markup(_, videoid, chat_id):
    buttons  = [

        [
            
            InlineKeyboardButton(
                text= "✚ 𝖯𝗅𝖺𝗒𝖫𝗂𝗌𝗍 ✚",
                callback_data=f"vip_playlist {videoid}"
            ),
        
        
            InlineKeyboardButton(
                text=_["Control"],
                callback_data=f"Pages Back|3|{videoid}|{chat_id}",
            ),
        ],
        [

            InlineKeyboardButton(
                text=_["DOWN"],
                callback_data=f"Nonee",
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
                text=_["ALINA"],
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AlinaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AlinaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_3"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
           InlineKeyboardButton(

                text=_["S_B_3"],

                url=f"https://t.me/{app.username}?startgroup=true",

            ),

        ],
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
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
     ]
    return buttons

## Telegram Markup

def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text= "𝖭𝖾𝗑𝗍",
                callback_data=f"PanelMarkup None|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons

## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],


        [
            InlineKeyboardButton(
                text="II 𝖯𝖺𝗎𝗌𝖾",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),

            InlineKeyboardButton(
                text="▢ 𝖲𝗍𝗈𝗉", callback_data=f"ADMIN Stop|{chat_id}"
            ),

            InlineKeyboardButton(
                text="𝖲𝗄𝗂𝗉 ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="▷ 𝖱𝖾𝗌𝗎𝗆𝖾", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝖱𝖾𝗉𝗅𝖺𝗒 ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["HOME"],
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons

def stream_markup2(_, chat_id):
    buttons = [
          [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
          ],

          [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),

            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [

            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons

def stream_markup_timer2(_, chat_id, played, dur):
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
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),

            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],

        [

            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎧 𝖲𝗎𝖿𝖿𝗅𝖾",
                callback_data=f"ADMIN Shuffle|{chat_id}",
            ),
            InlineKeyboardButton(
                text="𝖫𝗈𝗈𝗉 ↺", callback_data=f"ADMIN Loop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮ 10 𝖲𝖾𝖼",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            InlineKeyboardButton(
                text="10 𝖲𝖾𝖼 ❯",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["NEXT"],
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
                InlineKeyboardButton(
                    text="🕒 0.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
                InlineKeyboardButton(
                    text="🕤 1.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

def panel_markup_5(_, videoid, chat_id):
    buttons = [ 

         [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="II 𝖯𝖺𝗎𝗌𝖾", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▢ 𝖲𝗍𝗈𝗉 ▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="𝖲𝗄𝗂𝗉 ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),

        ],
        [
            InlineKeyboardButton(text="▷ 𝖱𝖾𝗌𝗎𝗆𝖾", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝖱𝖾𝗉𝗅𝖺𝗒 ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["HOME"],
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
            InlineKeyboardButton(
                text=_["NEXT"],
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(
                    text="🕒 0.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                ),
                InlineKeyboardButton(
                    text="🕓 0.75𝗑",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                ),
                InlineKeyboardButton(
                    text="🕤 1.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.0",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5𝗑",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                ),
                InlineKeyboardButton(
                    text="🕛 2.0𝗑",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                ),
            ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
            ),
        ],
    ]
    return buttons

def panel_markup_4(_, vidid, chat_id, played, dur):
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
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="II 𝖯𝖺𝗎𝗌𝖾",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),

            InlineKeyboardButton(
                text="▢ 𝖲𝗍𝗈𝗉 ▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),

            InlineKeyboardButton(
                text="𝖲𝗄𝗂𝗉 ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="▷ 𝖱𝖾𝗌𝗎𝗆𝖾", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="𝖱𝖾𝗉𝗅𝖺𝗒 ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["HOME"],
                callback_data=f"MainMarkup {vidid}|{chat_id}",
            ),
        ],
    ]

    return buttons

def panel_markup_clone(_, vidid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),

            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"downloadvideo {vidid}"),
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"downloadaudio {vidid}")
        ],
        [
            InlineKeyboardButton(
                text= "✚ ᴘʟᴀʏʟɪsᴛ ✚",
                callback_data=f"vip_playlist {vidid}"
            ),
        ],
    ]

    return buttons
