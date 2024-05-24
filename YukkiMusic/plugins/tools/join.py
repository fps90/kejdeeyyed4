from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from YukkiMusic import app

#--------------------------

MUST_JOIN = "EHS4SS"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://graph.org/file/d43f056ca2a5e2e598fd2.jpg", caption=f"**🧑🏻‍💻︙ببوورە ئەزیزم تۆ جۆین نیت؛\n🔰︙سەرەتا پێویستە جۆینی کەناڵی بۆت ♥️؛\n👾︙بکەیت بۆ بەکارهێنانم جۆین بە ⚜️؛\n💎︙کەناڵی بۆت: @EHS4SS\n\n👾︙کاتێ جۆینت کرد ستارت بکە /start , /help 📛!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("♥️ جۆینی کەناڵ بکە ♥️", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"**بۆت بکە ئەدمین لە کەناڵی**: {MUST_JOIN} !")
