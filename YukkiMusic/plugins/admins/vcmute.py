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
from config import BANNED_USERS
from YukkiMusic import app
from YukkiMusic.utils.inline import close_markup
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import is_muted, mute_on, mute_off
from YukkiMusic.utils.decorators import AdminRightsCheck


@app.on_message(filters.command(["vcmute"]) & ~filters.private & ~BANNED_USERS)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(chat_id)
    await Yukki.mute_stream(chat_id)
    user_mention = message.from_user.mention if message.from_user else "𝖠𝖽𝗆𝗂𝗇"
    await message.reply_text(
        _["admin_6"].format(user_mention), reply_markup=close_markup(_)
    )

@app.on_message(filters.command(["vcunmute"]) & ~filters.private & ~BANNED_USERS)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if not await is_muted(chat_id):
        return await message.reply_text(_["admin_7"], disable_web_page_preview=True)
    await mute_off(chat_id)
    await Yukki.unmute_stream(chat_id)
    user_mention = message.from_user.mention if message.from_user else "𝖠𝖽𝗆𝗂𝗇"
    await message.reply_text(
        _["admin_8"].format(user_mention), reply_markup=close_markup(_)
    )
