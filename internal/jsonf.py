import json

def merge_text(eng, sea_lang,file):
    object={}
    object['english'] = eng
    object[sea_lang] = sea_lang

    with open(file[:-4].json, 'w') as json_file:
        json.dump(object, json_file)



def eng_json(eng,file):
    object={}
    object['english'] = eng

    with open(file[:-4].json, 'w') as json_file:
        json.dump(object, json_file)

