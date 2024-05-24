from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from YukkiMusic import app
from YukkiMusic.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic.utils.database import get_assistant
import asyncio
from YukkiMusic.misc import SUDOERS
from YukkiMusic.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from YukkiMusic import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.utils.alina_ban import admin_filter
from YukkiMusic.utils.database import get_assistant, is_active_chat


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)



@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0e5e4a6fc3cd618701ebd.png",
        caption=f"""**🧑🏻‍💻┋ تەنیا گەشەپێدەر و خاوەنی بۆت\nدەتوانن ئەم فەرمانە بەکاربهێنن\n🧑🏻‍💻┋ پەیوەندی بکە بە گەشەپێدەر بۆ دروستکردنی کۆپی بۆتی ئەلینا**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🧑🏻‍💻 گەشەپێدەر 🧑🏻‍💻", url=f"https://t.me/IQ7amo"
                    )
                ]
            ]
        ),
    )
# --------------------------------------------------------------------------------- #
import time


@app.on_message(command(["/addbots", "زیادکردنی بۆت", "/addbot", f"/addbots@{app.username}"]) & SUDOERS)
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("**🧑🏻‍💻┋ فەرمانت هەڵە بەکار‌هێنا بەم شێوازە بنووسە :\n/addbots @bot_username**")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("**✅┋ زیادکردنی بۆت لە هەموو گرووپەکان**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001962701094:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**✅┋ زیادکردنی {bot_username} بۆ گرووپ\n\n✅┋ زیادکرا بۆ: {done} گرووپ\n❌┋ شکستی هێنا لە {failed} گرووپ\n\n⎋┋ زیادکرا لەلایەن ⇜ @{userbot.username}**"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**✅┋ زیادکردنی {bot_username} بۆ گرووپ\n\n✅┋ زیادکرا بۆ: {done} گرووپ\n❌┋ شکستی هێنا لە {failed} گرووپ\n\n⎋┋ زیادکرا لەلایەن ⇜ @{userbot.username}**"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**🧑🏻‍💻 {bot_username} بە سەرکەوتوویی زیادکرا\n\n✅┋ زیادکرا بۆ: {done} گرووپ\n❌┋ شکستی هێنا لە {failed} گرووپ\n\n⎋┋ زیادکرا لەلایەن ⇜ @{userbot.username}**"
        )
    except Exception as e:
        await message.reply(f"**❌┋ هەڵە : {str(e)}**")
