import whisper
from jsonf import *
import os

def detect_lang(model,audio):
    audiop = whisper.load_audio(audio)
    audio_test = whisper.pad_or_trim(audiop) #fits the audio into 30s 
    mel = whisper.log_mel_spectrogram(audio_test)

    _, probs = model.detect_language(mel)
 
    lang=max(probs, key=probs.get)

    if lang not in ['id','vi','th','my','ms','zh','lo']:
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