import asyncio
import random
from pyrogram import Client, filters, idle
from YukkiMusic import app
from strings.filters import command


SLEEP = 0.1


@app.on_message(filters.regex("^بڵێ|^بلی") & filters.group)
async def say(app, message):
    if message.text.startswith("بلی") and message.reply_to_message:
        txt = message.text.split(None, 1)[1]
        return await message.reply_to_message.reply(txt)

    elif message.text.startswith("بڵێ"):
        txt = message.text.split(None, 1)[1]
        return await message.reply(txt)
