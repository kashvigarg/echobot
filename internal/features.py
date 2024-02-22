import whisper
import jsonf

def trans_eng(file):
    model = whisper.load_model("base.en")
    eng = model.transcribe(file)
    jsonf.eng_json(eng,file)
    

def trans_both(file):
    model = whisper.load_model("base")

    # make log-Mel spectrogram 
    mel = whisper.log_mel_spectrogram(file)    #.to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions()
    sea_lang = whisper.decode(model, mel, options)

    eng = model.transcribe(file)
    jsonf.merge_text(eng, sea_lang,file)
