from pyrogram import Client, filters
from YukkiMusic import app
import requests


@app.on_message(filters.regex(r"(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"))
async def Start(app, message):
    try:
        msg = message.text
        url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
        music = url['data']['music']
        region = url['data']['region']
        tit = url['data']['title']
        vid = url['data']['play']
        ava = url['data']['author']['avatar']
        ##
        name = url['data']['music_info']['author']
        time = url['data']['duration']
        sh = url['data']['share_count']
        com = url['data']['comment_count']
        wat = url['data']['play_count']
        await app.send_photo(message.chat.id, ava,
                            caption=f'**✧ ¦ ناو : {name}\n✧ ¦ وڵات : {region}\n\n✧ ¦ ژمارەی بینەر : {wat}\n✧ ¦ ژمارەی کۆمێنت : {com}\n✧ ¦ ژمارەی شەیرەکان : {sh}\n✧ ¦ درێژی ڤیدیۆ : {time}**',
                             )
        await app.send_video(message.chat.id, vid, caption=f"{tit}")

    except:pass
