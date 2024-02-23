import whisper
from jsonf import *
import os

def detect_lang(model,audio):
    audio = whisper.load_audio(audio)
    audio_test = whisper.pad_or_trim(audio) #fits the audio into 30s 
    test=model.transcribe(audio_test)
    lang=test["language"]

    if lang not in ['id','vi','th','my','ms','zh']:
        return "False"
    else:
        return lang
    
def trans_eng(audio):
    model=whisper.load_model("small")

    lang_test=detect_lang(model,audio)
    if lang_test=='False':
        return False
    
    eng=model.transcribe(audio,task="translate")

    file_name=os.path.splitext(audio)[0]+'.json'
    eng_json(eng["text"],file_name)


def trans_both(audio):
    model=whisper.load_model("small")

    lang_test=detect_lang(model,audio)
    if lang_test=='False':
        return False
    
    sea_lang=model.transcribe(audio)

    eng=model.transcribe(audio,task="translate")
    file_name=os.path.splitext(audio)[0]+'.json'

    sea_json(sea_lang["text"],eng["text"],lang_test,file_name)

trans_both("indotest1.mp3")
