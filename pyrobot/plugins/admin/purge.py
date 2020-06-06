"""Purge Messages
Syntax: .purge"""

import asyncio

from pyrogram import Client, Filters

from pyrobot import (
    COMMAND_HAND_LER,
    TG_MAX_SELECT_LEN,
    app
)

from pyrobot.helper_functions.admin_check import admin_check
from pyrobot.helper_functions.cust_p_filters import sudo_filter

@app.on_message(Filters.command("purge", COMMAND_HAND_LER) & sudo_filter)
async def purge(client, message):
    """ purge upto the replied message """
    if message.chat.type not in (("supergroup", "channel")):
        return

    is_admin = await admin_check(message)

    if not is_admin:
        return

    status_message = await message.reply_text("Oof", quote=True)
    await message.delete()
    message_ids = []
    count_del_etion_s = 0

    if message.reply_to_message:
        for a_s_message_id in range(message.reply_to_message.message_id, message.message_id):
            message_ids.append(a_s_message_id)
            if len(message_ids) == TG_MAX_SELECT_LEN:
                await client.delete_messages(
                    chat_id=message.chat.id,
                    message_ids=message_ids,
                    revoke=True
                )
                count_del_etion_s += len(message_ids)
                message_ids = []
        if len(message_ids) > 0:
            await client.delete_messages(
                chat_id=message.chat.id,
                message_ids=message_ids,
                revoke=True
            )
            count_del_etion_s += len(message_ids)

    await status_message.edit_text(
        f"Deleted `{count_del_etion_s}` messages", parse_mode="md"
    )
    await asyncio.sleep(5)
    await status_message.delete()
