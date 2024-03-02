# <img src="https://github.com/kashvigarg/echobot/blob/main/files/logoechobot.webp" width="37px"> ECHOBOT
EchoBot is a Telegram bot designed to streamline data collection for research in the field of Large Language Models (LLM), specifically focusing on languages spoken in Southeast Asia. Transcribe/Translate various audio/video files belonging to languages spoken in South East Asian region and get respective result in a json format, the data is then included in the public dataset upon user's consent. It is an easy to use tool, that comes with extensive documentation and a friendly user interface.

<p align="center">
  <img src="https://github.com/kashvigarg/echobot/blob/main/files/echobot1.jpg" alt="First Image" style="width:32%; display:inline-block;"/>
  <img src="https://github.com/kashvigarg/echobot/blob/main/files/echobot2.jpg" alt="Second Image" style="width:32%; display:inline-block;"/>
  <img src="https://github.com/kashvigarg/echobot/blob/main/files/echobot3.jpg" alt="Third Image" style="width:32%; display:inline-block;"/>
</p>

Explore our [dataset](https://docs.google.com/spreadsheets/d/1GcFxt5QD1e0MsxaHb9Wlb6XS-tMt7esv5ocmgUj6V_Q/edit?usp=sharing) for a closer look at how all the features finally come together.

## Getting Started
Start interacting with the bot [here](https://t.me/echo_kd_bot).

OR

Find us on Telegram, whether you're using a desktop or mobile device. Simply search for `echo_kd_bot` in the search bar.

### User guide
- Start using EchoBot with the `/start` command. You can then choose from a variety of translation preferences.
- To share files, simply upload video and audio files, or record new audio/video messages.
- The `/trmode` command can be used to toggle between translation settings;
  1. Both: Receive a transcription of your uploaded media's audio in the original language, as well as an English translation of the same
  2. English only: Receive only the English translation of your uploaded media's audio
  3. SEA only: Receive only the transcription of your uploaded media in the original language.
- View all supported languages using the `/languages` command.
- The `/privacy` command toggles between privacy settings. You can choose to keep your data private or anonymously contribute to our dataset.
- Use `/info` to learn more about our project and data policies.
- The `/help` command can be used to get a quick overview of how to use all features within the bot.

  #### Testing
  For testing the bot the user may use the following files [Test file 1](https://github.com/kashvigarg/echobot/blob/main/files/indotest1.mp3) , [Test file 2](https://github.com/kashvigarg/echobot/blob/main/files/indo4.mp3) , with the default privacy options, ie. the file transription/translation won't be stored in the [dataset](https://docs.google.com/spreadsheets/d/1GcFxt5QD1e0MsxaHb9Wlb6XS-tMt7esv5ocmgUj6V_Q/edit#gid=0)

## Features
- **Relevancy to SEA-based Research**
  
  The bot, on receiving media, autodetects its language, accepting only those which fall under the Southeast Asian region. It currently supports **Vietnamese**, **Thai**, **Indonesian**, **Burmese/Myanmar**, **Malay**, **Lao/Laotian**. 
  
- **Data Compatible with LLM Corpora Policies**

  The bot generates a transcript for all provided media, along with an English translation. A `json` file, containing the translated, as well as transcribed text is returned to the user. The data within this file   is properly structured in the form of key-value pairs, where the key denotes the identified language. The `json` formatting of potential training data allows the respective LLM to understand and respond to
  conversational cues, such as questions, requests, and follow-up questions.

- **Supports multiple media formats**
  
  The bot accepts all audio and video formats, including `.mp4`, `.mov`, `.webm` for video, as well as `.wav`, `.mp3`, `.mpeg`, `.oga` for audio focused content. The user can also upload any on-device media to the
  chat, in addition to being able to record content directly within the Telegram app.

- **Open Sourced Data Collection**
  
  Users around the world can contribute to our dataset, through the bot. Within the dataset, the records are structured according to the following parameters; `SEA_TRANSCRIPTION` containing media
  transcriptions of the uploaded files in their regional language, `ENG` containing their respective english translations, along with `LANGUAGE` identifying the original language of the content.

- **User Friendly Interface**
  
  The bot features an easy-to-use and intuitive interface with clearly mentioned instructions and helpful messages. It is fairly simple to navigate through all the included features using the `\help` command.
  The user can upload multiple media files at once, and the bot notifies them once those files have been processed. 
  
- **Respect for User Privacy**

  We respect the user's privacy and concern for their shared media. Adhering to this, the bot ensures secure removal of all uploaded files. The processed data is not stored in the open-source dataset without the
  user's consent.


## How It works
The bot handles a wide range of user inputs, including audio, video, and all in-app recorded content. It then, automatically recognises the language of the uploaded media. This helps in filtering out data irrelevant to SEA context. Once identified, the files fed by the user are then fetched from the Telegram server and then, channelled through a machine learning backend. EchoBot is powered by OpenAI's  `Whisper` model, that produces highly accurate media transcriptions. On demand, English translations of the uploaded media are also generated. 

Post processing, the bot integrates anonymized content into an open-source dataset, respecting user privacy preferences. This dataset is currently built upon the Google Sheets API. In cases where submissions are restricted by privacy settings, the bot ensures the secure removal of all associated files. Users are kept well-informed with clear confirmation messages at each stage of the process.

The bot uses a model with 244 Million parameters and is hosted using a Virtual machine with 4vcpus and 8 GB RAM .

## Build From Source
Requires Python version 3.8 * 

To build the bot from source 
run the following commands

```
git clone https://github.com/kashvigarg/echobot
cd echobot
```
The bot requires `ffmpeg` installed on the system

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

```
Once inside the repository run 
```
pip install requirements.txt
```
To run the bot locally, you'll need a Telegram Bot Token and a Google Cloud Service Account Key. 

Obtaining a BOT Token is as simple as contacting [@BotFather](https://t.me/botfather), issuing the /newbot command and following the steps until you're given a new token. You can find a step-by-step guide [here](https://core.telegram.org/bots/features#creating-a-new-bot).

To generate a Service Account Key, you can follow the instructions mentioned in [this article](https://developers.google.com/sheets/api/quickstart/python). 

Save the value of the bot token in the .env file as 
`BOT_TOKEN="Value of token"`
and the service account json file as `service_account.json`, both in the root folder.

Then finally run the following command to get the bot running.
```
python bot.py
```

**Note:** *Later versions of python may cause version mismatch of various python libraries installed , which may need to be resolved manually. 

**Note:** The language model currently won't be able to recognize files as one of the SEA language files if the initial few seconds of the file contains any other language.
      At the same time in some cases it may face hallucinations while processing very small (1-4 seconds) files.

#### Submission details
stackup username - deejay
