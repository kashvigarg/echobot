options = {
    'both': 'Both',
    'english_only': 'English only',
    'sea_only': 'SEA only'
}

privacy_setting = {
    'yes' : 'Yes', 
    'no' : 'No'
}

start_msg = (
    "Welcome to EchoBot! 🌏 We're collecting audio with South East Asian context. Share the sounds of your surroundings and contribute to our datasets."
    "Not sure what to do? Use /help for a quick guide on how to use the bot and make meaningful contributions."
)

help_msg = (
    "Welcome to EchoBot! Contribute audio with South East Asian context using these commands:\n\n"
    "To share a files:\n"
    "- Simply upload video and audio files, or\n"
    "- Record a new audio/video message.\n\n"
    "/context [description]: Add a brief description to your audio.\n"
    "/language [code]: Set your preferred language (e.g., /language en for English).\n"
    "/review: Check stats on your recent submission.\n"
    "/trmode: Toggle between translation modes.\n"
    "/privacy: Change privacy settings.\n"
    "/info: Learn more about our project and data policies.\n\n"
    
    "Feel free to explore and make your contributions memorable!"
)

confirmation_msg = (
    "Thanks for your contribution! Your media has been received. Feel free to use /review to check or edit your submission."
)

allowed_mime_types= mime_types = [
    'audio/mpeg',  # for mp3, mpweg, mpga
    'video/mp4',   # for mp4
    'audio/mp4',   # for m4a
    'audio/wav',   # for wav
    'audio/webm'   # for webm
]