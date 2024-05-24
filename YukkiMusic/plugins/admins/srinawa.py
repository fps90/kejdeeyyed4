from pyrogram import Client, filters
from YukkiMusic import app
from YukkiMusic.utils.alina_ban import admin_filter

@app.on_message(filters.regex("^سڕینەوە [0-9]+$") & admin_filter & filters.group)
async def del_message(c, msg):
    textt = msg.text
    num = int(textt.split(" ")[1])
    list1 = []
    msg_id = msg.id
    for i in range(1, num):
        list1.append(msg_id)
        msg_id = msg_id - 1
    try:
        await c.delete_messages(msg.chat.id, list1)
    except Exception as e:
        await msg.reply(e)
