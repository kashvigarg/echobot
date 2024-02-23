import whisper
from jsonf import *


async def detect_lang(model,audio):
    audio_test = whisper.pad_or_trim(audio) #fits the audio into 30s 
    test=model.transcribe(audio_test)
    lang=test["language"]

    if lang not in ['id','vi','th','my','ms','zh',]:
        return False
    
async def trans_eng(audio):
    model=whisper.load_model("small")
    if await detect_lang(model,audio)==False:
        return False
    eng=model.transcribe(audio,task="translate")
    eng_json(eng["text"])


async def trans_both(audio):
    model=whisper.load_model("small")
    
    if await detect_lang(model,audio)==False:
        return False
    
    sea_lang=model.transcribe(audio)

    eng=model.transcribe(audio,task="translate")

    sea_json(sea_lang["text"],eng["text"])

trans_both("indotest1.mp3")
