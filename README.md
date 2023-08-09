# Angel and Mortals Bot

Send anonymous messages between angels and mortals. 

**[NEW]** Now supports photos, stickers, documents, audio, video, and animations!

## Read on Medium

https://chatbotslife.com/building-a-chatbot-for-angel-mortal-5d389ab7acde

## User data

Data used for the game was small so just use file PLAYERS_FILENAME to store usernames of players.
Order of columns is player, angel and mortal with one header row.

Sample:
```
Player,Angel,Mortal
username1,username2,username3
username2,username3,username1
username3,username1,username2
```

## Environment variables

Have a .env file with the following:
ANGEL_BOT_TOKEN=
ANGEL_ALIAS=Angel
MORTAL_ALIAS=Mortal

## Useful references
https://python-telegram-bot.readthedocs.io/en/stable/telegram.bot.html#telegram.Bot.sendAnimation
https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message

