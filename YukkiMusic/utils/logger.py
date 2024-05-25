#
# Copyright (C) 2024 - present by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from YukkiMusic import app
from YukkiMusic.utils.database import is_on_off
from config import LOG_GROUP_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "گرووپی تایبەت"

        logger_text = f"""
<b>{app.mention} پەخشی گرووپەکان</b>

<b>ئایدی گرووپ :</b> <code>{message.chat.id}</code>
<b>ناوی گرووپ :</b> {message.chat.title}
<b>یوزەری گرووپ :</b> @{message.chat.username}

<b>ئایدی بەکارهێنەر :</b> <code>{message.from_user.id}</code>
<b>ناو :</b> {message.from_user.mention}
<b>یوزەر :</b> @{message.from_user.username}

<b>ناوی گۆرانی :</b> {message.text.split(None, 1)[1]}
<b>جۆری پلاتفۆڕم :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)
        return
