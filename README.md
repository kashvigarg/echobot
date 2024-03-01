# ECHOBOT
EchoBot is a Telegram bot designed to streamline data collection for research in the field of Large Language Models (LLM), specifically focusing on languages spoken in Southeast Asia. It is an easy to use tool, that comes with extensive documentation and a friendly user interface.

Explore our [dataset](https://docs.google.com/spreadsheets/d/1GcFxt5QD1e0MsxaHb9Wlb6XS-tMt7esv5ocmgUj6V_Q/edit?usp=sharing) for a closer look at how all the features finally come together.

## Getting Started
To start interacting with the bot
Head over to this link
[Echobot](https://t.me/echo_kd_bot)

OR

Open Telegram on desktop/Mobile, in the search bar type `echo_kd_bot`.

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
The bot handles a wide range of user inputs, including audio, video, and all in-app recorded content. It is equipped to recognize YouTube links across different operating systems and browsers through the use of Regular Expressions. Once identified, it downloads files from their respective sources and channels them through a machine learning pipeline powered by OpenAI's Whisper model, producing highly accurate media transcriptions. On demand, English translations of the uploaded media are also generated. Post processing, the bot integrates anonymized content into an open-source dataset, respecting user privacy preferences. This dataset is currently built upon the Google Sheets API. In cases where submissions are restricted by privacy settings, the bot ensures the secure removal of all associated files. Users are kept well-informed with clear confirmation messages at each stage of the process.


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
and the service account json file as `service_account.json`, both in the root folder.

Then finally run the following command to get the bot running.
```
python bot.py
```
