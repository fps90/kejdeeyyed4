import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus, ChatMembersFilter
from pyrogram.errors import UserNotParticipant, FloodWait
from pyrogram.types import ChatPermissions
from YukkiMusic import app
from YukkiMusic.utils.alina_ban import admin_filter
from YukkiMusic.utils.database import get_assistant

SPAM_CHATS = []


@app.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall",""], prefixes=["/", "@"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
        )
        return
    if replied:
        try:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(["admin", "admins", "admintag", "tagadmin"], prefixes=["/", "@"])
    & admin_filter
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@admins Hi Friends`"
        )
        return
    if replied:
        try:
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{replied.text}\n\n usertxt",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            usernum = 0
            usertxt = ""
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                usernum += 1
                usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        ["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"]
    )
    & admin_filter
)
async def tag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /acancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@aall Hi Friends`"
        )
        return
    if replied:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f"[{m.user.first_name}](tg://openmessage?user_id={m.user.id})"
            if usernum == 7:
                await userbot.send_message(
                    message.chat.id,
                    f"{replied.text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]

        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            usernum += 1
            usertxt += f'<a href="tg://openmessage?user_id={m.user.id}">{m.user.first_name}</a>'

            if usernum == 7:
                await userbot.send_message(
                    message.chat.id, f"{text}\n{usertxt}", disable_web_page_preview=True
                )
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "cancelmention",
            "offmention",
            "mentionoff",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


__MODULE__ = "Tᴀɢᴀʟʟ"
__HELP__ = """

@all ᴏʀ /all | /tagall ᴏʀ  @tagall | /mentionall ᴏʀ  @mentionall [ᴛᴇxᴛ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ] ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴜsᴇʀ's ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴛ ʙᴏᴛ

@aall ᴏʀ /aall | /atagall ᴏʀ  @atagall | /amentionall ᴏʀ  @amentionall  [ᴛᴇxᴛ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ] ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴜsᴇʀ's ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙʏ ʙᴏᴛ's ᴀssɪsᴛᴀɴᴛ


/admin ᴏʀ @admin | /admintag ᴏʀ @admintag | /tagadmin ᴏʀ @tagadmin | /admins Oʀ @admins [ᴛᴇxᴛ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ] ᴛᴏ ᴛᴀɢ ᴀʟʟ ᴀᴅᴍɪɴ's ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

/cancel Oʀ @cancel |  /offmention Oʀ @offmention | /mentionoff Oʀ @mentionoff | /cancelall Oʀ @cancelall - ᴛᴏ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴀɴʏ ᴛᴀɢ ᴘʀᴏᴄᴇss

**__Nᴏᴛᴇ__** Tʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴄᴀɴ ᴏɴʟʏ ᴜsᴇ ᴛʜᴇ Aᴅᴍɪɴs ᴏғ Cʜᴀᴛ ᴀɴᴅ ᴍᴀᴋᴇ Sᴜʀᴇ Bᴏᴛ ᴀɴᴅ ᴀssɪsᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ's
"""
