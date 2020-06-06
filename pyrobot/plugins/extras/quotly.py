from pyrogram import Client, Filters

from pyrobot import COMMAND_HAND_LER, PyroBotCMD
from pyrobot.helper_functions.cust_p_filters import sudo_filter
import random
import time

@PyroBotCMD.on_message(Filters.command("qbot", COMMAND_HAND_LER) & sudo_filter)
async def quotly(client, message):
    if not message.reply_to_message:
        await message.edit("Reply to any users text message")
        return
    await message.edit("```Making a Quote```", parse_mode="md")
    await message.reply_to_message.forward("@QuotLyBot")
    is_sticker = False
    progress = 0
    while not is_sticker:
        try:
            msg = await client.get_history("@QuotLyBot", 1)
            check = msg[0]["sticker"]["file_id"]
            is_sticker = True
        except:
            time.sleep(0.5)
            progress += random.randint(0, 10)
            try:
                await message.edit("```Making a Quote```\nProcessing {}%".format(progress), parse_mode="md")
                if progress >= 100:
                    pass
            except:
                await message.edit("__ERROR SUUUU__", parse_mode="md")
    await message.edit("```Complete !```", parse_mode="md")
    msg_id = msg[0]["message_id"]
    await client.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
