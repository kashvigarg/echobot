import json


def eng_json(eng):
    object={}
    object['eng']=eng
    with open("test.json",'w') as json_file:
        json.dump(object,json_file)

def sea_json(sea,eng):
    object={}
    object['sea_lang']=sea
    object['eng']=eng

    with open("test.json",'w') as json_file:
        json.dump(object,json_file)