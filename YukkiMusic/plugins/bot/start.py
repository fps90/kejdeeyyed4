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
from random import choice
import time

from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    InputMediaPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS, PHOTO, START_IMG_URL
from config.config import OWNER_ID
from strings import get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS, _boot_
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.formatters import get_readable_time
from YukkiMusic.utils.inline import (
    alive_panel,
    help_mark,
    private_panel,
    start_pannel,
)
from YukkiMusic.utils.functions import MARKDOWN, WELCOMEHELP
from YukkiMusic.utils.database import get_assistant
from YukkiMusic.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5


IQ_PICS = [
"https://graph.org/file/9340f44e4a181b18ac663.jpg",
"https://graph.org/file/50037e072302b4eff55ba.jpg",
"https://graph.org/file/39f39cf6c6c68170f6bf2.jpg",
"https://graph.org/file/abf9931642773bc27ad7f.jpg",
"https://graph.org/file/60764ec9d2b1fda50c2d1.jpg",
"https://graph.org/file/a90c116b776c90d58f5e8.jpg",
"https://graph.org/file/b2822e1b60e62caa43ceb.jpg",
"https://graph.org/file/84998ca9871e231df0897.jpg",
"https://graph.org/file/6c5493fd2f6c403486450.jpg",
"https://graph.org/file/9dd91a4a794f15e5dadb3.jpg",
"https://graph.org/file/0a2fb6e502f6c9b6a04ac.jpg",
"https://graph.org/file/774380facd73524f27d26.jpg"

]

IQ_VIDS = [
"https://telegra.ph/file/79055663111eaa8824b26.mp4",
"https://telegra.ph/file/96b75e112896a00c47203.mp4",
"https://telegra.ph/file/f35b4a68ec793efe46c7c.mp4",
"https://graph.org/file/d55b419cf02dfcdd5a2b8.mp4",
"https://graph.org/file/cfa01d6254cfa3b6fd945.mp4",
"https://telegra.ph/file/b61c1ce580957e936d8fb.mp4",
"https://telegra.ph/file/f2aec19f7387741798fa8.mp4",
"https://telegra.ph/file/e13f1c42b949221f87e77.mp4"

]

emoji = [
    "👍",
    "❤",
    "🔥",
    "🥰",
    "👏",
    "😁",
    "🤔",
    "🤯",
    "😱",
    "😢",
    "🎉",
    "🤩",
    "🤮",
    "💩",
    "🙏",
    "👌",
    "🕊",
    "🤡",
    "🥱",
    "🥴",
    "😍",
    "🐳",
    "❤",
    "‍🔥",
    "🌚",
    "🌭",
    "💯",
    "🤣",
    "⚡",
    "🏆",
    "💔",
    "🤨",
    "😐",
    "🍓",
    "🍾",
    "💋",
    "😈",
    "😴",
    "😭",
    "🤓",
    "👻",
    "👨‍💻",
    "👀",
    "🎃",
    "🙈",
    "😇",
    "😨",
    "🤝",
    "✍",
    "🤗",
    "🫡",
    "🎅",
    "🎄",
    "☃",
    "💅",
    "🤪",
    "🗿",
    "🆒",
    "💘",
    "🙉",
    "🦄",
    "😘",
    "💊",
    "🙊",
    "😎",
    "👾",
    "🤷‍♂",
    "🤷",
    "🤷‍♀",
    "😡",
]
loop = asyncio.get_running_loop()

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_comm(client, message: Message, _):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_id = message.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            hu = await message.reply_text(f"**🧑🏻‍💻┋ {message.from_user.mention} بۆت سپام مەکە بەڕێز\n🧑🏻‍💻┋ پێنج چرکە بوەستە**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time
    await app.send_reaction(chat_id, message_id, random.choice(emoji))
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            if config.START_IMG_URL:
                return await message.reply_photo(
                    photo=START_IMG_URL,
                    caption=_["help_1"],
                    reply_markup=help_mark,
                )
                await app.send_reaction(chat_id, message_id, random.choice(emoji))
            else:
                return await message.reply_photo(
                    random.choice(IQ_PICS),
                    caption=_["help_1"],
                    reply_markup=keyboard,
                )
                await app.send_reaction(chat_id, message_id, random.choice(emoji))
        if name[0:4] == "song":
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            await message.reply_text(_["song_2"])
            return
        if name == "mkdwn_help":
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            await message.reply(
                MARKDOWN,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        if name == "greetings":
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            await message.reply(
                WELCOMEHELP,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )

        if name[0:3] == "sta":
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            m = await message.reply_text("🔎 ғᴇᴛᴄʜɪɴɢ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ sᴛᴀᴛs.!")
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ᴀɴᴅ ᴀᴜᴅɪᴏs]({config.SUPPORT_GROUP}) ** played {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(None, get_stats)
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            await asyncio.sleep(1)
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            if await is_on_off(config.LOG):
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"**🧑🏻‍💻┋ کەسێکی نوێ هاتە ناو بۆت پشکنینی گەشەپێدەران\n\n👤┋ ناوی : {message.from_user.mention}\n👾┋ یوزەری : @{message.from_user.username}\n🆔┋ ئایدی :** `{message.from_user.id}`",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                await Telegram.send_split_text(message, lyrics)
                return
            else:
                
                await message.reply_text("ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ʟʏʀɪᴄs.")
                return
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
            await asyncio.sleep(1)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 ғᴇᴛᴄʜɪɴɢ ɪɴғᴏ!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
**زانیاری گۆرانی

❇️ ناونیشان : {title}

⏳ ماوە : {duration} Mins
👀 بینەر: {views}
⏰ کاتی بڵاوکردنەوە : {published}
🎥 کەناڵ : {channel}
📎 لینکی کەناڵ [ئێرە دابگرە]({channellink})
🔗 لینکی گۆرانی : [ʟɪɴᴋ]({link}) **
"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text= "🎸 𝖵𝗂𝖽𝖾𝗈", callback_data=f"downloadvideo {query}"),
                        InlineKeyboardButton(text= "🎸 𝖠𝗎𝖽𝗂𝗈", callback_data=f"downloadaudio {query}"),
                
                    ],
                    [
                        InlineKeyboardButton(text="🎧 sᴇᴇ ᴏɴ ʏᴏᴜᴛᴜʙᴇ 🎧", url=link),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=key,
            )
            await asyncio.sleep(2)
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            if await is_on_off(config.LOG):
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"**🧑🏻‍💻┋ کەسێکی نوێ هاتە ناو بۆت زانیاری گۆرانی\n\n👤┋ ناوی : {message.from_user.mention}\n👾┋ یوزەری : @{message.from_user.username}\n🆔┋ ئایدی :** `{message.from_user.id}`",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await app.send_reaction(chat_id, message_id, random.choice(emoji))
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await app.send_reaction(chat_id, message_id, random.choice(emoji))
                await message.reply_photo(
                    random.choice(IQ_PICS),
                    caption=_["start_2"].format(app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            await message.reply_photo(
                random.choice(IQ_PICS),
                caption=_["start_2"].format(app.mention),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"**🧑🏻‍💻┋ کەسێکی نوێ هاتە ناو بۆت\n\n👤┋ ناوی : {message.from_user.mention}\n👾┋ یوزەری : @{message.from_user.username}\n🆔┋ ئایدی :** `{message.from_user.id}`",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def testbot(client, message: Message, _):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_id = message.id
    current_time = time()
    
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            await app.send_reaction(chat_id, message_id, random.choice(emoji))
            hu = await message.reply_text(f"**🧑🏻‍💻┋ {message.from_user.mention} بۆت سپام مەکە بەڕێز\n🧑🏻‍💻┋ پێنج چرکە بوەستە**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time
        
    out = alive_panel(_)
    uptime = int(time.time() - _boot_)
    chat_id = message.chat.id
    if config.START_IMG_URL:
        await app.send_reaction(chat_id, message_id, random.choice(emoji))
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_8"].format(app.mention, get_readable_time(uptime)),
            reply_markup=InlineKeyboardMarkup(out),
        )
    else:
        await app.send_reaction(chat_id, message_id, random.choice(emoji))
        await message.reply_video(
        random.choice(IQ_VIDS),
        caption=_["start_8"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    await add_served_chat(message.chat.id)
    
# Check if Userbot is already in the group
    try:
        userbot = await get_assistant(message.chat.id)
        message = await message.reply_text(f"**🧑🏻‍💻┋ پشکنین بۆ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) لە گرووپە یان نا •**")
        is_userbot = await app.get_chat_member(message.chat.id, userbot.id)
        if is_userbot:
            await message.edit_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) لە گرووپە ئێستا دەتوانی گەڕان بکەیت بۆ گۆرانی •**")
    except Exception as e:
        # Userbot is not in the group, invite it
        try:
            await message.edit_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) لە گرووپ نییە بانگهێشتی دەکەم ..**")
            invitelink = await app.export_chat_invite_link(message.chat.id)
            await asyncio.sleep(1)
            await userbot.join_chat(invitelink)
            await message.edit_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) لە گرووپە ئێستا دەتوانی گەڕان بکەیت بۆ گۆرانی •**")
        except Exception as e:
            await message.edit_text(f"**🧑🏻‍💻┋ ناتوانم [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) بانگهێشت بکەم\nبمکە ئەدمین تاوەکو بتوانم زیادی بکەم •**")


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**ᴛʜɪs ʙᴏᴛ's ᴘʀɪᴠᴀᴛᴇ ᴍᴏᴅᴇ ʜᴀs ʙᴇᴇɴ ᴇɴᴀʙʟᴇᴅ ᴏɴʟʏ ᴍʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ɪғ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴛʜɪs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ sᴏ sᴀʏ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇ ʏᴏᴜʀ ᴄʜᴀᴛ."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                    
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                chid = message.chat.id
                
                try:
                    userbot = await get_assistant(message.chat.id)
    
                    chid = message.chat.id
                    
                    
                    if message.chat.username:
                        await userbot.join_chat(f"**{message.chat.username}**")
                        await message.reply_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) هاتە گرووپەوە بەهۆی یوزەری گرووپ •**")
                    else:
                        invitelink = await app.export_chat_invite_link(chid)
                        await asyncio.sleep(1)
                        messages = await message.reply_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) جۆین دەکات بە بەکارهێنانی لینك •**")
                        await userbot.join_chat(invitelink)
                        await messages.delete()
                        await message.reply_text(f"**🧑🏻‍💻┋ [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) هاتە گرووپەوە بەهۆی لینکی گرووپ •**")
                except Exception as e:
                    await message.edit_text(f"**🧑🏻‍💻┋ تکایە بمکە ئەدمین بۆ بانگهێشت کردنی [یاریدەدەرەکەم](tg://openmessage?user_id={userbot.id}) بۆ گرووپ •**")

                await message.reply_video(
                    random.choice(IQ_VIDS),
                    caption=_["start_3"].format(
                        message.from_user.mentoin,
                        app.mention,
                        message.chat.title,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(app.mention, member.mention)
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(app.mention, member.mention)
                )
            return
        except:

            return


__MODULE__ = "Boᴛ"
__HELP__ = """✅<u>Bᴏᴛ Cᴏᴍᴍᴀɴᴅs:</u>

/stats - Gᴇᴛ Tᴏᴘ 𝟷𝟶 Tʀᴀᴄᴋs Gʟᴏʙᴀʟ Sᴛᴀᴛs, Tᴏᴘ 𝟷𝟶 Usᴇʀs ᴏғ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Cʜᴀᴛs ᴏɴ ʙᴏᴛ, Tᴏᴘ 𝟷𝟶 Pʟᴀʏᴇᴅ ɪɴ ᴀ ᴄʜᴀᴛ ᴇᴛᴄ ᴇᴛᴄ.

/sudolist - Cʜᴇᴄᴋ Sᴜᴅᴏ Usᴇʀs ᴏғ Yᴜᴋᴋɪ Mᴜsɪᴄ Bᴏᴛ

/lyrics [Mᴜsɪᴄ Nᴀᴍᴇ] - Sᴇᴀʀᴄʜᴇs Lʏʀɪᴄs ғᴏʀ ᴛʜᴇ ᴘᴀʀᴛɪᴄᴜʟᴀʀ Mᴜsɪᴄ ᴏɴ ᴡᴇʙ.

/song [Tʀᴀᴄᴋ Nᴀᴍᴇ] ᴏʀ [YT Lɪɴᴋ] - Dᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴛʀᴀᴄᴋ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ ɪɴ ᴍᴘ𝟹 ᴏʀ ᴍᴘ𝟺 ғᴏʀᴍᴀᴛs.

/player -  Gᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ Pʟᴀʏɪɴɢ Pᴀɴᴇʟ.

c sᴛᴀɴᴅs ғᴏʀ ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ.

/queue ᴏʀ /cqueue - Cʜᴇᴄᴋ Qᴜᴇᴜᴇ Lɪsᴛ ᴏғ Mᴜsɪᴄ."""
