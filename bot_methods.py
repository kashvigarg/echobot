from telegram import Update
from telegram.ext import ContextTypes
from constants import *
from functions import *
from internal.features import*
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)

async def begin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)

async def audio_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.audio
    data_size, data_res = check_size(data.file_size)
    if (data_res):
        print(data.file_name) 
        file = await data.get_file()
        path = file.file_path
        print(path)

        req = path 
        res = requests.get(req)
        data_name = data.file_name
        open(data.file_name, "wb").write(res.content)
        lang = trans_both(audio=data_name)
        print("Lang: ", lang)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received an audio file!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your file occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def audio_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.audio
    data_size, data_res = check_size(data.file_size)
    if (data_res):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a voice file!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video
    data_size, data_res = check_size(data.file_size)
    if (data_res):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a video file!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video_note
    data_size, data_res = check_size(data.file_size)
    if (data_res):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a video chat!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def help(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg)