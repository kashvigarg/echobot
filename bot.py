import os
from dotenv import load_dotenv
import telebot
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
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
    bulk_start_handler = CommandHandler('begin', begin)
    bulk_end_handler = CommandHandler('done', end)
    audio_handler = MessageHandler(filters.AUDIO, audio_upload)
    voice_handler = MessageHandler(filters.VOICE, audio_chat)
    videonote_handler = MessageHandler(filters.VIDEO_NOTE, video_chat)
    video_handler = MessageHandler(filters.VIDEO, video_upload)
    
    application.add_handler(start_handler)
    application.add_handler(audio_handler)
    application.add_handler(voice_handler)
    application.add_handler(help_handler)
    application.add_handler(video_handler)
    application.add_handler(videonote_handler)

    application.run_polling()