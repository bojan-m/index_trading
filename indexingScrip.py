import json

data_json = open('data.json').read()
data = json.loads(data_json)
data_dict = data['data']

previous = []
gross = None
gross_date = []

for i in data_dict[::-1]:
    if gross is None:
        gross_date.append([i['quote_date'], i['high']-i['low']])
        previous = i
        gross = i['high']-i['low']
    else:
        gross_date.append([i['quote_date'], i['high'] - previous['low']])
        previous = i


print(gross_date)