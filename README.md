<p align="center">
  <img src="https://i.sitischu.com/kantek_main_smol_256.png">
</p>

# Kantek

Kantek is a userbot written in Python using Telethon.

## A word of warning

Kantek is mostly built to help with the administration of chats and is the main source for [SpamWatch](https://spamwat.ch) and [SpamBlockers](https://t.me/SpamBlockers).
Because of that, it checks every message your account receives for blacklisted items, this includes strings, domains, top-level domains, files, images and telegram entities. This means that for every message your account receives kantek might make multiple HTTP requests and resolve multiple telegram entities. The latter might lead to large (6+ hours) floodwaits from Telegram.

If you want to use kantek without the administration part, simply remove the `plugins/autobahn` folder to disable these features.

## Requirements

Python 3.6+ is required to run the bot.
MySQL is used to store bot data.

## Setup

- Copy the example config file to `config.py`
- Create a user and a Database in MySQL. Give the user full permissions to the Database.
  - Put the Authentication data into the config file.
- Run bot.py
