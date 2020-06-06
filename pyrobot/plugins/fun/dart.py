from pyrogram import Client, Filters

from pyrobot import COMMAND_HAND_LER, PyroBotCMD
from pyrobot.helper_functions.cust_p_filters import sudo_filter
# EMOJI CONSTANTS
DART_E_MOJI = "🎯"
# EMOJI CONSTANTS


@PyroBotCMD.on_message(Filters.command(["throw", "dart"], COMMAND_HAND_LER) & sudo_filter)
async def throw_dart(client, message):
    """ /throw an @AnimatedDart """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
