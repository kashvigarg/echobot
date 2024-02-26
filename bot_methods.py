from telegram import Update
from telegram.ext import ContextTypes
from constants import *
from internal.functions import *
from internal.features import*

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)

async def audio_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.audio
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = data.file_name 
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received an audio file!")
        lang = trans_both(audio=f'media/{file_name}')
        if (lang==False):
            await delete_file(file_name=file_name)
            await context.bot.send_message(chat_id=update.effective_chat.id, text="We're currently only accepting media with SEA context.")
        else:
            json_name = file_name.split('.')[0] + '.json'
            json_file = f'media/{json_name}'
            
            await context.bot.send_document(chat_id=chat_id, document=json_file) 
            await delete_file(file_name=file_name)
            await delete_file(file_name=json_name)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=confirmation_msg)
            
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your file occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def audio_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.voice
    
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = "voicerec" + data.file_unique_id + ".oga"
        file = await data.get_file()
        print(file)
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        lang = trans_both(audio=f'media/{file_name}')
        if (lang=='False'):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="We're currently only accepting media with SEA context.")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a voice recording!") 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = data.file_name 
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        lang = trans_both(audio=f'media/{file_name}')
        if (lang=='False'):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="We're currently only accepting media with SEA context.")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a video file!") 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video_note
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = "videorec" + data.file_unique_id + ".mp4"
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        lang = trans_both(audio=f'media/{file_name}')
        if (lang=='False'):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="We're currently only accepting media with SEA context.")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a video chat message!") 
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def help(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg)