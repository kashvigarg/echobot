import pygsheets 

def add_data_to_sheets(sea, eng, lang):
    client = pygsheets.authorize(service_account_file="echobot-415817-48c074d2441c.json") 
    worksheet = client.open('EchoBot-Dataset').sheet1
    new_row = [sea, eng, lang]

    cells = worksheet.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    last_row = len(cells)

    worksheet = worksheet.insert_rows(last_row, number=1, values= new_row)
