![version](https://img.shields.io/badge/version-1.0.0-blue)
![GitHub repo size](https://img.shields.io/github/repo-size/ngdechev/smartbot?color=green)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/ngdechev/library)

# MokokoBot - Discord Bot

`MokokoBot` is a multipurpose discord bot written in `discord.py` library. For now the commands are limited, but in future i will add more. I am creating the bot, because I want to try new programming language - `Python`. To check the existing commands and future commits please navigate to the `dev` branch.

The bot must have the following permissions to function properly: `Manage Roles`, `Kick Members`, `Ban Members`, `Read Messages`, <br> `Send Messages`, `Manage Messages`, `Read Message History`. 

## Commands

`!kick @member [reason]` -> Kick member from the guild.

`!ban @member [reason]` -> Ban member from the guild.

`!unban @member [reason]` -> Unban member from the guild.

`!setprefix [new prefix]` -> Set the prefix to whatever you want.

`!clear [number of messages]` -> Clear number of message.

`!ping` -> Ping!

## How to run the bot

To run the bot you need to install [Python](https://www.python.org/downloads/). Then you need to install `discord.py`:

```bash
pip install discord.py
```

Also you need to install [PostgreSQL](https://www.postgresql.org/download/). Create table in the database called `Guilds` (you can see the required fields in the **Project Development** section). Then run the command:

```bash
python bot.py
```

## Project Development
`MokokoBot` has 1 table in the database called `Guilds`:

| Field Name | Data Type  | Description                      |
|------------|------------|----------------------------------|
| guild_id   | Text       | Server ID                        |
| prefix     | Text       | Server Prefix                    |

The following programming languages were used for the development of the project:
1. **Python** - *v3.11.1*
2. **PostgreSQL** - *v6.15*

And the following libraries:

1. **discord.py** - *v3.7.4* 

And the following tools:

1. **PyCharm** - *2022 v3.2*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Discord](https://img.shields.io/badge/DISCORD.PY-blue?style=for-the-badge&logo=discord) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
