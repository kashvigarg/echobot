import os
from dotenv import load_dotenv
import telebot
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from bot_methods import *

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    audio_handler = MessageHandler(filters.AUDIO, audio_upload)
    voice_handler = MessageHandler(filters.VOICE, audio_chat)
    videonote_handler = MessageHandler(filters.VIDEO_NOTE, video_chat)
    video_handler = MessageHandler(filters.VIDEO, video_upload)
    callback_handler = CallbackQueryHandler(handle_choice)
    media_file_handler = MessageHandler(filters.Document.ALL, doc_upload)
    processing_mode_handler = CommandHandler('trmode', change_mode)
    
    application.add_handler(start_handler)
    application.add_handler(audio_handler)
    application.add_handler(voice_handler)
    application.add_handler(help_handler)
    application.add_handler(video_handler)
    application.add_handler(videonote_handler)
    application.add_handler(media_file_handler)
    application.add_handler(callback_handler)
    application.add_handler(processing_mode_handler)

    application.run_polling()