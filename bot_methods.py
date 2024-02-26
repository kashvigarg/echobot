from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes
from constants import *
from internal.functions import *
from internal.features import*

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)

# options = {
#     'both': 'Receive both transcribed audio and translated English text',
#     'english_only': 'Receive only translated English text'
# }

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_id = update.message.from_user.id
#     message_text = "Please choose an option:"
    
#     # Create inline keyboard with options
#     keyboard = [
#         [InlineKeyboardButton(text, callback_data=option) for option, text in options.items()]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Send the message with the inline keyboard
#     await context.bot.send_message(chat_id=user_id, text=message_text, reply_markup=reply_markup)

# # Handle the user's choice
# def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     query = update.callback_query
#     user_id = query.from_user.id
#     choice = query.data.lower()

#     # Process the user's choice
#     if choice in options:
#         context.bot.send_message(chat_id=user_id, text=f"You selected: {options[choice]}")
#         # Now, you can proceed with the logic to send the chosen content.
#     else:
#         # Invalid choice
#         context.bot.send_message(chat_id=user_id, text="Invalid choice. Please choose an option.")



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
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = "voicerec" + data.file_unique_id + ".oga"
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a voice recording!") 
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
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = data.file_name
        if (file_name==None):
            file_name =  "videorec" + data.file_unique_id + ".mp4"
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Received a video file {file_name}!")
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
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def video_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video_note
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = "videorec" + data.file_unique_id + ".mp4"
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received a video chat!")
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
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your message occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")


  
async def doc_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.document
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    if (data_res):
        file_name = data.file_name 
        file = await data.get_file()
        file_path = file.file_path
        file_type = data.mime_type
        
        if (str(file_type) not in allowed_mime_types):
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Unsupported Input Format!")
            return 
        
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received am media file!")
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


async def help(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg)