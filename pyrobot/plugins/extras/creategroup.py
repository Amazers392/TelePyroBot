from pyrogram import Client, Filters

from pyrobot import COMMAND_HAND_LER, app
from pyrobot.helper_functions.cust_p_filters import sudo_filter

@app.on_message(Filters.command("creategroup", COMMAND_HAND_LER) & sudo_filter)
async def creategroup(client, message):
    rm = await message.reply_text("Trying to make a group...")
    await client.create_supergroup("Userbot Group", "Group made by Userbot")
    await rm.edit("Check the group with title - 'Userbot Group'")
