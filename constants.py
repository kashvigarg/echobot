dataset_link = 'https://docs.google.com/spreadsheets/d/1GcFxt5QD1e0MsxaHb9Wlb6XS-tMt7esv5ocmgUj6V_Q/edit?usp=sharing'

options = {
    'both': 'Both',
    'english_only': 'English Only',
    'sea_only': 'SEA Only'
}

options_data = {
    'both': 'You\'ll now receive both the media transcription and English translation of uploaded files',
    'english_only': 'You\'ll receive the English translation of uploaded files',
    'sea_only': 'You\'ll receive the media translation of uploaded files'
}

privacy_setting = {
    'yes' : 'Yes', 
    'no' : 'No'
}

start_msg = (
    "Welcome to EchoBot! 🌏 We're collecting audio with South East Asian context, for LLM Research. Share the sounds of your surroundings and contribute to our datasets.\n\n"
    "Not sure what to do? Use /help for a quick guide on common commands."
)
help_msg = (
    "Welcome to the User Help Guide:\n\n"
    "🎤 To share files:\n"
    "   - Upload video and audio files, or\n"
    "   - Record a new audio/video message.\n\n"
    "🔄 /trmode: Toggle between translation settings.\n"
    "    You'll receive an option to choose from:\n"
    "       1. Both: Receive a transcription of your uploaded media's audio in the original language, as well as an English translation of the same.\n"
    "       2. English only: Receive only the English translation of your uploaded media's audio.\n"
    "       3. SEA only: Receive only the transcription of your uploaded media in the original language.\n\n"
    "❓ /languages: View all languages currently supported by EchoBot.\n\n"
    "🔒 /privacy: Toggle between privacy settings. Use /info for further detail on how we use your data.\n\n"
    "ℹ️ /info: Learn more about our project and data policies.\n\n"
    


    "Feel free to explore and make your contributions memorable!"
)

info_msg = (
    "Data Use Policy:\n"
    f"By setting your privacy mode to 'Open', you allow us to use and store your contributed data in our open-source dataset for language model (LLM) research.\nYou can view the same [here]({dataset_link}).\n"
    "If you choose 'Closed', your data will neither be shared nor stored.\n\n"

    "You can toggle between privacy settings using the /privacy command.\n\n"
    
    "We appreciate your contribution, and your trust is important to us."
)


content_region_msg = (
    "We appreciate your interest! However, we are specifically focusing on media with South East Asian (SEA) context. Feel free to contribute content related to this region.\n\n"
    "Use /languages to find more about included languages and tongues."
)

languages_supported_msg = (
    "We currently support the following languages in the South East Asian (SEA) region:\n\n"
    "Indonesian\n"
    "Vietnamese\n"
    "Thai\n"
    "Myanmar\n"
    "Malay\n"
    "Lao\n"
)


confirmation_msg = (
    "Thanks for your valuable contribution! We appreciate your participation in our project."
)

allowed_mime_types= mime_types = [
    'audio/mpeg',  # for mp3, mpweg, mpga
    'video/mp4',   # for mp4
    'audio/mp4',   # for m4a
    'audio/wav',   # for wav
    'audio/webm'   # for webm
]