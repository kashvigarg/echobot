import whisper
import json
import os
from internal.google_sheets import *

languages={"id":"indonesian",
           "vi":"vietnamese",
           "th":"thai",
           "my":"myanmar",
           "ms":"malay",
           "lo": "lao",
           "kh":"khmer",
           "eng":"english"}

def lang_json(text,file_name,lang="eng"):
    object={}
    object[languages[lang]]=text

    with open(file_name,'w') as json_file:
        json.dump(object,json_file)


def sea_json(sea,eng,lang,file_name):
    object={}
    object[languages[lang]]=sea
    object['eng']=eng

    with open(file_name,'w') as json_file:
        json.dump(object,json_file)
       
def detect_lang(model,audio):
    audiop = whisper.load_audio(audio)
    audio_test = whisper.pad_or_trim(audiop) #fits the audio into 30s 
    mel = whisper.log_mel_spectrogram(audio_test)

    _, probs = model.detect_language(mel)
 
    lang=max(probs, key=probs.get)

    if lang not in ['id','vi','th','my','ms','lo','km']:
        return "False"
    else:
        return lang
    
def trans_sea(audio):
    model=whisper.load_model("small")

    lang_test=detect_lang(model,audio)
    if lang_test=='False':
        return False
    
    sea=model.transcribe(audio)

    file_name=os.path.splitext(audio)[0]+'.json'
    lang_json(sea["text"],file_name,lang_test)
    
def trans_eng(audio):
    model=whisper.load_model("small")

    lang_test=detect_lang(model,audio)
    if lang_test=='False':
        return False
    
    eng=model.transcribe(audio,task="translate")

    file_name=os.path.splitext(audio)[0]+'.json'
    lang_json(eng["text"],file_name)


def trans_both(audio,priv):
    model=whisper.load_model("small")

    lang_test=detect_lang(model,audio)
    if lang_test=='False':
        return False
    
    sea_lang=model.transcribe(audio)

    eng=model.transcribe(audio,task="translate")
    file_name=os.path.splitext(audio)[0]+'.json'

    if priv=='yes':
        add_data_to_sheets(sea_lang["text"],eng["text"],languages[lang_test])

    sea_json(sea_lang["text"],eng["text"],lang_test,file_name)



#trans_sea("../media/indo4.mp3")
