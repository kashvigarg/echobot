from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, constants
from telegram.ext import ContextTypes
from constants import *
from internal.functions import *
from internal.features import*
from bot_globals import curr_privacy, curr_mode
from aux_methods import *

async def change_mode(update, context: ContextTypes.DEFAULT_TYPE):
    global curr_mode

    message_text = (
        "Select your preference:\n"
        "1. Receive the transcribed text from your media file as well as an English translation of the same.\n"
        "2. Receive only the English translation of an uploaded file.\n"
        "3. Receive only a textual transcription of an uploaded file.\n\n"
    )

    keyboard_buttons = [InlineKeyboardButton(text, callback_data=option) for option, text in options.items()]

    reply_markup = InlineKeyboardMarkup([keyboard_buttons[i:i + 1] for i in range(0, len(keyboard_buttons), 1)])

    await context.bot.send_message(chat_id=update.message.from_user.id, text=message_text, reply_markup=reply_markup)

async def change_privacy(update, context: ContextTypes.DEFAULT_TYPE):
    global curr_privacy
    
    if (curr_privacy =='no'):
        curr_privacy = 'yes'
    else:
        curr_privacy = 'no'
    
    if (curr_privacy == 'no'):
        await context.bot.send_message(chat_id=update.message.from_user.id, text=f"Privacy setting modified. Your data won't be shared or stored.")
    else:
        await context.bot.send_message(chat_id=update.message.from_user.id, text=f"Privacy setting modified. You are now anonymously contributing to our open source dataset. \n\n You can view the same [here]({dataset_link}).", parse_mode='Markdown')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    message_text =  message_text = (
    "Choose an initial translation preference:\n"
    "1. Receive the transcribed text from your media file as well as an English translation of the same.\n"
    "2. Receive only the English translation of an uploaded file.\n"
    "3. Receive only a textual transcription of an uploaded file.\n\n"
    "You can modify this preference anytime using the /trmode command."
)

    keyboard_buttons = [InlineKeyboardButton(text, callback_data=option) for option, text in options.items()]

    reply_markup = InlineKeyboardMarkup([keyboard_buttons[i:i+1] for i in range(0, len(keyboard_buttons), 1)])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=start_msg)
    await context.bot.send_message(chat_id=user_id, text=message_text, reply_markup=reply_markup)

async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    choice = query.data.lower()

    if choice not in options:
       await context.bot.send_message(chat_id=user_id, text="Invalid choice. Please choose a valid option.")
       return 

    await query.answer()
    global curr_mode
    curr_mode = query.data
    msg_data = options_data[curr_mode]
    await query.edit_message_text(text=f"Translation setting modified.\n {msg_data}")


async def audio_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.audio
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    await handle_media(data, data_size, data_res, update, 'audio file', context)


async def audio_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.voice
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    await handle_media(data, data_size, data_res, update, 'voice recording', context)

async def video_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    await handle_media(data, data_size, data_res, update, 'video file', context)

async def video_chat(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.video_note
    chat_id = update.message.chat_id
    data_size, data_res = await check_size(data.file_size)
    await handle_media(data, data_size, data_res, update, 'video chat', context)

async def info_command(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info_msg, parse_mode='Markdown')

async def language_command(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=languages_supported_msg)
  
async def doc_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.document
    chat_id = update.message.chat_id
    global curr_privacy
    global curr_mode
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
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Received:  media file!")
        if curr_mode == 'both':
            lang = trans_both(f'media/{file_name}', curr_privacy)
        elif curr_mode == 'english_only':
            lang = trans_eng(audio=f'media/{file_name}')
        elif curr_mode == 'sea_only':
            lang = trans_sea(audio=f'media/{file_name}')
        else:
            lang = False

        if (lang==False):
            await delete_file(file_name=file_name)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=content_region_msg)
        else:
            json_name = file_name.split('.')[0] + '.json'
            json_file = f'media/{json_name}'
            
            await context.bot.send_document(chat_id=chat_id, document=json_file)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=confirmation_msg)

            await delete_file(file_name=file_name)
            await delete_file(file_name=json_name)
            
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your file occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

async def link_upload(update : Update, context: ContextTypes.DEFAULT_TYPE):
    data_link = update.message.text

    data_saved, file_name, file_size = await download_youtube_audio(data_link)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Received: Youtube URL!")
    if (data_saved==False):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Failed to parse uploaded media :(")
    else:
        file_name = "yt" + ".mp4"
        size, is_valid = await check_size(file_size=file_size)

        await handle_link(size, is_valid, update, file_name, context)
        

async def help(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg)

async def error_handler(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=error_msg)