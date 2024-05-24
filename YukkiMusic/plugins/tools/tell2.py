from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from config import OWNER_ID
from pyrogram.types import VideoChatEnded, Message
from YukkiMusic.core.call import Yukki
# vc on
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("<b>• ئەدمین تێلی کردەوە وەرن ⎋</b>")
       
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {da} چرکە و داخرا ⎋**")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 1 خولەك ⎋**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 2 خولەك ⎋**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {ma[0]} خولەك ⎋**")  
        else:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {ma[0]} خولەك ⎋**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 1 کاتژمێر ⎋**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 2 کاتژمێر ⎋**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {ho[0]} کاتژمێر ⎋**")  
        else:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {ho[0]} کاتژمێر ⎋**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 1 ڕۆژ ⎋**")
        elif 2 <= day[0] < 3:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی 2 ڕۆژ ⎋**")
        elif 3 <= day[0] < 11:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {day[0]} ڕۆژ ⎋**")  
        else:
            await message.reply(f"**🎻┋ تێل کۆتایی پێھات، ماوەکەی {day[0]} ڕۆژ ⎋**")
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"<b>• لەلایەن ← {message.from_user.mention} </b>"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"<b>\n• بانگێشتکرایی ←[{user.first_name}](tg://user?id={user.id}) </b>"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}")
           except:
             pass  


####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& SUDOERS)
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"**◗⋮◖ بە سەرکەوتوویی لێفت دەکەم گەشەپێدەر**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


####


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
