import requests
from pyrogram import filters
from pyrogram.enums import ChatAction

from YukkiMusic import app, api


@app.on_message(filters.command(["bard"]))
async def bard(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "**نموونە :**\n\n`/bard Who's best player in world `"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        Z = await api.bard(user_input)
        result = Z["candidates"][0]["content"]["parts"][0]["text"]
        await message.reply_text(result)
    except requests.exceptions.RequestException as e:
        pass
