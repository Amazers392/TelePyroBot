from pyrogram import Client, Filters

from pyrobot import COMMAND_HAND_LER, app
from pyrobot.helper_functions.cust_p_filters import sudo_filter

@app.on_message(Filters.command("id", COMMAND_HAND_LER) & sudo_filter)
async def get_id(client, message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message
        if rep.audio:
            file_id = rep.audio.file_id
        elif rep.document:
            file_id = rep.document.file_id
        elif rep.photo:
            file_id = rep.photo.file_id
        elif rep.sticker:
            file_id = rep.sticker.file_id
        elif rep.video:
            file_id = rep.video.file_id
        elif rep.animation:
            file_id = rep.animation.file_id
        elif rep.voice:
            file_id = rep.voice.file_id
        elif rep.video_note:
            file_id = rep.video_note.file_id
        elif rep.contact:
            file_id = rep.contact.file_id
        elif rep.location:
            file_id = rep.location.file_id
        elif rep.venue:
            file_id = rep.venue.file_id
        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        await message.edit("This User's ID: `{}`\nThis chat's ID:\n`{}`".format(user_id, message.chat.id), parse_mode="md")
    elif file_id:
        await message.edit("This File's ID: `{}`".format(file_id), parse_mode="md")
    else:
        await message.edit("This chat's ID:\n`{}`".format(message.chat.id), parse_mode="md")
