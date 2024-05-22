from pyrogram import filters
from SafoneAPI import SafoneAPI
from YukkiMusic import app


async def get_advice():
    a = SafoneAPI()
    b = await a.advice()
    c = b["advice"]
    return c


@app.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)
