import requests
import json
import asyncio
import os
from pyrogram import Client, Filters
from pyrobot import COMMAND_HAND_LER, TMP_DOWNLOAD_DIRECTORY

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ =  f"""
Get Screenshot of any website.

`{COMMAND_HAND_LER}webss <website url>`: Get screenshot of the Website URL.
"""

@Client.on_message(Filters.command("webss", COMMAND_HAND_LER) & Filters.me)
async def web_screenshot(client, message):
    await message.edit("`Fetching image...`")
    link = message.text.split(" ", 1)[1]
    if not link.startswith("http"):
        link = "https://" + link
    response = requests.get(f"https://sjprojectsapi.herokuapp.com/ss/?url={link}")
    ss = json.loads(response.text)
    if not ss == response.json():
        await message.edit("**Some error occured**\n`Try Again Later`")
        return
    url_requested = ss['url']

    try:
        ssp = ss['high']
    except KeyError:
        ssp = ss['low']
    except:
        await message.edit("`Some Error Occurred, Try again Later`")

    img_link = ssp['url']
    img_size = ssp['size']
    extension = ssp['extension']

    caption = f"**Raw File:** {img_link}\n**URL:** {url_requested}"

    img = requests.get(f"{img_link}")
    imgfile = open(f"{TMP_DOWNLOAD_DIRECTORY}/web_screenshot.{extension}", "wb")
    imgfile.write(img.content)
    imgfile.close()
    imgloc = f"{TMP_DOWNLOAD_DIRECTORY}/web_screenshot.{extension}"

    try:
        await message.reply_document(
            document=imgloc,
            caption=caption,
            disable_notification=True,
            reply_to_message_id=message.message_id)
        await message.edit("`Done!`")
        await asyncio.sleep(3)
        os.remove(imgloc)
        await message.delete()
    except Exception as ef:
        await message.edit(f"**Error:**\n{ef}")
