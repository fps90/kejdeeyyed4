#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message

from YukkiMusic.misc import SUDOERS

from .play import pytgcalls
from .utils import is_active_chat, is_streaming, stream_off, stream_on
from .utils.active import _clear_


@Client.on_message(filters.command(["pause", "resume", "end", "stop","ڕاگرتن","وەستان"]) & ~filters.private)
async def pause_str(client, message: Message):
    try:
        await message.delete()
    except BaseException:
        pass
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("**» بۆ تێلی نەکردۆتەوە**")
    check = await client.get_chat_member(message.chat.id, message.from_user.id)

    if (
        check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    ) or message.from_user.id not in SUDOERS:
        return await message.reply_text(
            "**» تۆ ئەدمین نییت دڵە**"
        )

    admin = (
        await client.get_chat_member(message.chat.id, message.from_user.id)
    ).privileges
    if not admin.can_manage_video_chats:
        return await message.reply_text(
            "**» تۆ ڕۆڵی تەواوت نییە بۆ بەڕێوەبردنی تێل**"
        )
    if message.text.lower() == "/pause":
        if not await is_streaming(message.chat.id):
            return await message.reply_text(
                "**•⎆┊ لە بیرت چووە کە پێشتر وەستێنراوە ♥️•**"
            )
        await pytgcalls.pause_stream(message.chat.id)
        await stream_off(message.chat.id)
        return await message.reply_text(
            text=f"<b>•⎆┊ ئێستا پەخشکردن بۆ ماوەیەکی کاتی وەستاوە ♥•\n\n•⎆┊ لەلایەن : {message.from_user.mention} </b>",
        )
    elif message.text.lower() == "/resume":

        if await is_streaming(message.chat.id):
            return await message.reply_text(
                "**•⎆┊ لە بیرت چووە کە پێشتر دەستی بە پەخشکردن کردەوە ♥️•**"
            )
        await stream_on(message.chat.id)
        await pytgcalls.resume_stream(message.chat.id)
        return await message.reply_text(
            text=f"<b>•⎆┊ ئێستا پەخشکردن دەست پێدەکاتەوە♥•\n\n•⎆┊ لەلایەن : {message.from_user.mention} </b>",
        )
    elif message.text.lower() == "/end" or message.text.lower() == "/stop" or message.text.lower() == "ڕاگرتن" or message.text.lower() == "وەستان":
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_call(message.chat.id)
        except BaseException:
            pass

        return await message.reply_text(
            text=f"<b>•⎆┊ پەخشکردن ڕاگرترا|وەستا♥•\n\n•⎆┊ لەلایەن : {message.from_user.mention} </b>",
        )
