#
# Copyright (C) 2021-present by TeamYukki@Github, < https://github.com/TeamYukki >.
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
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.extraction import extract_user
from YukkiMusic.utils.database import add_gban_user, remove_gban_user
from YukkiMusic.utils.decorators.language import language



@app.on_message(filters.command(["block","/block","بلۆک"], "") & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in BANNED_USERS:
        return await message.reply_text(_["block_1"].format(user.mention))
    await add_gban_user(user.id)
    BANNED_USERS.add(user.id)
    await message.reply_text(_["block_2"].format(user.mention))


@app.on_message(filters.command(["unblock","/unblock","لادانی بلۆک"], "") & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in BANNED_USERS:
        return await message.reply_text(_["block_3"].format(user.mention))
    await remove_gban_user(user.id)
    BANNED_USERS.remove(user.id)
    await message.reply_text(_["block_4"].format(user.mention))


@app.on_message(filters.command(["blocked", "blockedusers", "blusers","/blocked", "/blockedusers", "/blusers","بلۆککراوەکان"], "") & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)


__MODULE__ = "Blᴀᴄᴋʟɪsᴛ"
__HELP__ = """⚠️<u>Bʟᴀᴄᴋʟɪsᴛ Cʜᴀᴛ Fᴜɴᴄᴛɪᴏɴ:</u>
/blacklistchat [CHAT_ID] - Bʟᴀᴄᴋʟɪsᴛ ᴀɴʏ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
/whitelistchat [CHAT_ID] - Wʜɪᴛᴇʟɪsᴛ ᴀɴʏ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ ғʀᴏᴍ ᴜsɪɴɢ Mᴜsɪᴄ Bᴏᴛ
/blacklistedchat - Cʜᴇᴄᴋ ᴀʟʟ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛs.

👤<u>Bʟᴏᴄᴋᴇᴅ Fᴜɴᴄᴛɪᴏɴ:</u>
/block [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Pʀᴇᴠᴇɴᴛs ᴀ ᴜsᴇʀ ғʀᴏᴍ ᴜsɪɴɢ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs.
/unblock [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's Bʟᴏᴄᴋᴇᴅ Lɪsᴛ.
/blockedusers - Cʜᴇᴄᴋ ʙʟᴏᴄᴋᴇᴅ Usᴇʀs Lɪsᴛs

👤<u>Gʙᴀɴ ғᴜɴᴄᴛɪᴏɴ:</u>
/gban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Gʙᴀɴ ᴀ ᴜsᴇʀ ғʀᴏᴍ ʙᴏᴛ's sᴇʀᴠᴇᴅ ᴄʜᴀᴛ ᴀɴᴅ sᴛᴏᴘ ʜɪᴍ ғʀᴏᴍ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ.
/ungban [Usᴇʀɴᴀᴍᴇ ᴏʀ Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] - Rᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ ғʀᴏᴍ Bᴏᴛ's ɢʙᴀɴɴᴇᴅ Lɪsᴛ ᴀɴᴅ ᴀʟʟᴏᴡ ʜɪᴍ ғᴏʀ ᴜsɪɴɢ ʏᴏᴜʀ ʙᴏᴛ
/gbannedusers  - Cʜᴇᴄᴋ Gʙᴀɴɴᴇᴅ Usᴇʀs Lɪsᴛs
"""
