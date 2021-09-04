# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from covid import Covid
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.covid (.*)")
async def corona(event):
    await event.edit("`Pengolahan...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Dikonfirmasi   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif      : {country_data['active']}`\n"
        output_text += f"`🤕Kritis    : {country_data['critical']}`\n"
        output_text += f"`😟Kematian Baru  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Meninggal      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔Kasus Baru   : {country_data['new_cases']}`\n"
        output_text += f"`😇Pulih   : {country_data['recovered']}`\n"
        output_text += f"`🧪Jumlah tes: {country_data['total_tests']}`\n\n"
        output_text += f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "Belum ada informasi tentang negara ini!"

    await event.edit(f"`Info Virus Corona di {country}:`\n\n{output_text}")


@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Pengolahan...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️Dikonfirmasi   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️Aktif      : {country_data['active']}`\n"
        output_text += f"`🤕Kritis    : {country_data['critical']}`\n"
        output_text += f"`😟Kematian Baru  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️Meninggal      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔Kasus Baru   : {country_data['new_cases']}`\n"
        output_text += f"`😇Pulih   : {country_data['recovered']}`\n"
        output_text += "`🧪Total tests : N/A`\n\n"
        output_text += f"Data disediakan oleh [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "Belum ada informasi tentang negara ini!"

    await event.edit(f"`Info Virus Corona di {negara}:`\n\n{output_text}")


CMD_HELP.update({"covid": "`.covid `**<negara>**"
                 "\n`Usage: Dapatkan informasi tentang data covid-19 di negara Anda.`\n\n"
                 "`.covid`"
                 "\n`Usage: Dapatkan informasi tentang data covid-19 di Seluruh Dunia.`\n"})
