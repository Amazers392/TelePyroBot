import os
import shutil
import datetime
import asyncio
from prettytable import PrettyTable
import requests
from pyrogram import Client, Filters
from pyrobot import COMMAND_HAND_LER

__PLUGIN__ = os.path.basename(__file__.replace(".py", ""))

__help__ = f"""
Check info of cases Covid19(Corona) Disease.

-> `{COMMAND_HAND_LER}corona` - for Global Stats
-> `{COMMAND_HAND_LER}corona <country>` - for a Country Stats
"""

@Client.on_message(Filters.command("covid", COMMAND_HAND_LER) & Filters.me)
async def covid(client, message):
    await message.edit("`Processing...`", parse_mode="md")
    cmd = message.text.split(' ', 1)
    if len(cmd) == 1:
        r = requests.get("https://corona.lmao.ninja/v2/all?yesterday=true").json()
        last_updated = datetime.datetime.fromtimestamp(r['updated'] / 1000).strftime("%Y-%m-%d %I:%M:%S")

        ac = PrettyTable()
        ac.header = False
        ac.title = "Global Statistics"
        ac.add_row(["Cases", f"{r['cases']:,}"])
        ac.add_row(["Cases Today", f"{r['todayCases']:,}"])
        ac.add_row(["Deaths", f"{r['deaths']:,}"])
        ac.add_row(["Deaths Today", f"{r['todayDeaths']:,}"])
        ac.add_row(["Recovered", f"{r['recovered']:,}"])
        ac.add_row(["Active", f"{r['active']:,}"])
        ac.add_row(["Critical", f"{r['critical']:,}"])
        ac.add_row(["Cases/Million", f"{r['casesPerOneMillion']:,}"])
        ac.add_row(["Deaths/Million", f"{r['deathsPerOneMillion']:,}"])
        ac.add_row(["Tests", f"{r['tests']:,}"])
        ac.add_row(["Tests/Million", f"{r['testsPerOneMillion']:,}"])
        ac.align = "l"
        await message.edit(f"`{str(ac)}`\nLast updated on: {last_updated}", parse_mode="md")

    country = cmd[1]
    r = requests.get(f"https://skuzapis.herokuapp.com/covid/data?country={country}").json()
    if "cases" not in r:
        await message.edit("`The country could not be found!`", parse_mode="md")
        await asyncio.sleep(3)
        await message.delete()
    else:
        cc = PrettyTable()
        cc.header = False
        country = r['countryInfo']['iso3'] if len(r['country']) > 12 else r['country']
        cc.title = f"Corona Cases in {country}"
        cc.add_row(["Cases", f"{r['cases']:,}"])
        cc.add_row(["Cases Today", f"{r['todayCases']:,}"])
        cc.add_row(["Deaths", f"{r['deaths']:,}"])
        cc.add_row(["Deaths Today", f"{r['todayDeaths']:,}"])
        cc.add_row(["Recovered", f"{r['recovered']:,}"])
        cc.add_row(["Active", f"{r['active']:,}"])
        cc.add_row(["Critical", f"{r['critical']:,}"])
        cc.add_row(["Cases/Million", f"{r['casesPerOneMillion']:,}"])
        cc.add_row(["Deaths/Million", f"{r['deathsPerOneMillion']:,}"])
        cc.add_row(["Tests", f"{r['totalTests']:,}"])
        cc.add_row(["Tests/Million", f"{r['testsPerOneMillion']:,}"])
        cc.align = "l"
        await message.edit(f"`{str(cc)}`\nRecently updated.", parse_mode="md")


def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return
