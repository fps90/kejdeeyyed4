#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import PK
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.database.memorydatabase import (
    get_active_chats,
    get_active_video_chats,
)

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND))
async def activevc(_, message: Message):
    if message.from_user.id not in SUDOERS:
        return await message.reply_text(
            "<b>✫ ببورە ئەزیزم ئەم فەرمانە تەنیا بۆ گەشەپێدەرە</b>"
        )
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ....ᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ", protect_content=PK
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"**ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ's:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND))
async def activevi_(_, message: Message):
    if message.from_user.id not in SUDOERS:
        return await message.reply_text(
            "<b>✫ ببورە ئەزیزم ئەم فەرمانە تەنیا بۆ گەشەپێدەرە</b>"
        )
    mystic = await message.reply_text(
        "ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ....ᴘʟᴇᴀsᴇ ʜᴏʟᴅ ᴏɴ", protect_content=PK
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "ᴘʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴘ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's")
    else:
        await mystic.edit_text(
            f"**ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ's:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["/ac","/av","چالاکی پەخش"], ""))
async def vc(client, message: Message):
    if message.from_user.id not in SUDOERS:
        return await message.reply_text(
            "<b>✫ ببورە ئەزیزم ئەم فەرمانە تەنیا بۆ گەشەپێدەرە</b>"
        )
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(
        f"<b>✫ زانیاری چالاکی پەخشکردن :</b>\n\n<b>دەنگی : {ac_audio}\nڤیدیۆ : {ac_video}</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✯ داخستن ✯', callback_data=f"close")]]))


__MODULE__ = "Acᴛɪᴠᴇᴠᴄ"
__HELP__ = """📈<u>ᴀᴄᴛɪᴠᴇᴠᴄ Cᴏᴍᴍᴀᴅ:</u>
/ac - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ ʙᴏᴛ.
/activevoice - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.
/activevideo - Cʜᴇᴄᴋ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴏɴ ʙᴏᴛ.
/stats - Cʜᴇᴄᴋ Bᴏᴛs Sᴛᴀᴛs"""
