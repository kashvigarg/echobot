import json

languages={"id":"indonesian",
           "vi":"vietnamese",
           "th":"thai",
           "my":"myanmar",
           "ms":"malay",
           "zh":"chinese",
           "lo": "lao"}

def eng_json(eng, file_name):
    object={}
    object['eng']=eng

    with open(file_name,'w') as json_file:
        json.dump(object,json_file)


def sea_json(sea,eng,lang,file_name):
    object={}
    object[languages[lang]]=sea
    object['eng']=eng

    with open(file_name,'w') as json_file:
        json.dump(object,json_file)