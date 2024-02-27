import json

languages={"id":"indonesian",
           "vi":"vietnamese",
           "th":"thai",
           "my":"myanmar",
           "ms":"malay",
           "zh":"chinese",
           "lo": "lao",
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