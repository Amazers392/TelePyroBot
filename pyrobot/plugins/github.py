import aiohttp
from pyrogram import Client, Filters
from pyrobot import COMMAND_HAND_LER
from pyrobot.utils.cust_p_filters import sudo_filter


@Client.on_message(Filters.command("github", COMMAND_HAND_LER) & sudo_filter)
async def github(client, message):
    if len(message.text.split()) == 1:
            await message.edit("Usage: `github (username)`", parse_mode="md")
            return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`" + username +
                                        " not found`", parse_mode="md")

            result = await request.json()

            url = result.get("html_url", None)
            name = result.get("name", None)
            company = result.get("company", None)
            bio = result.get("bio", None)
            created_at = result.get("created_at", "Not Found")

            REPLY = (
                f"**GitHub Info for `{username}**`"
                f"\n**Username:** `{name}`\n**Bio:** `{bio}`\n**URL:** {url}"
                f"\n**Company:** `{company}`\n**Created at:** `{created_at}`"
            )

            if not result.get("repos_url", None):
                    return await message.edit(REPLY, parse_mode="md")
            async with session.get(result.get("repos_url", None)) as request:
                result = request.json
                if request.status == 404:
                    return await message.edit(REPLY, parse_mode="md")

                result = await request.json()

                REPLY += "\n**Repos:**\n"

                for nr in range(len(result)):
                    REPLY += f"[{result[nr].get('name', None)}]({result[nr].get('html_url', None)})\n"

                await message.edit(REPLY, parse_mode="md")
