from bot_globals import curr_mode, curr_privacy
from internal.functions import *
from internal.features import *
from constants import *
from google_sheets import *

async def handle_media(data, data_size, data_res, update, file_type, context):
    global curr_privacy
    global curr_mode
    if (data_res):
        # video note , voice recording, video
        file_name = ''
        if (file_type in ['voice recording', 'video file', 'video chat']):
            ext = ".oga" if file_type == 'voice recording' else ".mp4"
            file_name = "media" + data.file_unique_id + ext
        else:
            file_name = data.file_name
        file = await data.get_file()
        file_path = file.file_path
        await download_file(file_path=file_path, file_name=file_name)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Received: {file_type}!")

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
            await context.bot.send_message(chat_id=update.effective_chat.id, text="We're currently only accepting media with SEA context.")
        else:
            json_name = file_name.split('.')[0] + '.json'
            json_file = f'media/{json_name}'
            await context.bot.send_document(chat_id=update.effective_chat.id, document=json_file) 
            await context.bot.send_message(chat_id=update.effective_chat.id, text=confirmation_msg)

            await delete_file(file_name=file_name)
            await delete_file(file_name=json_name)
            
            
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your file occupies {data_size} MB. EchoBot currently doesn't support files exceeding 25 MB :(")

