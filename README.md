# ECHOBOT
EchoBot is a Telegram bot designed to streamline data collection for research in the field of Large Language Models (LLM), specifically focusing on languages spoken in Southeast Asia. It is an easy to use tool, that comes with extensive documentation and a friendly user interface.


## Getting Started
Head over to this link
()[]

Search for `echo_kd_bot` on the Telegram search bar on desktop/mobile

### User guide


## Features
- Easy to use , UI/UX
- accepts on device video/audio , in-app recorded video/audio.
- Supports all telegram video/audio formats.
- accepts only sea context , autodetcts language
- Audio/video transcription + translatation, returns json 
- open source collection of data , easily to access , privacy managed
- parses uploaded audio/videos, video/audio Urls

## How It works


## Build From Source
Requires Python version >=3.8.10

To build the bot from source 
run the following commands

```
git clone https://github.com/kashvigarg/echobot
cd echobot
```

Once inside the repository run 
```
pip install requirements.txt
```
To run the bot locally you'll need a Telegram Bot token which can be ..., and a google cloud service account json key, which can be ...
save the value of the bot token in the .env file as 
`BOT_TOKEN="Value of token"`
and the service account json file as `serviceaccount.json`, both in the root folder.

Then finally run the following command to get the bot running.
```
python bot.py
```
