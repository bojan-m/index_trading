import json

def to_list_low(dict):
    list = []
    for i in data_dict[::-1]:
        list.append([i['low'], i['quote_date']])
    return list

def to_list_high(dict):
    list = []
    for i in data_dict[::-1]:
        list.append([i['high'], i['quote_date']])
    return list


data_json = open('data.json').read()
data = json.loads(data_json)
data_dict = data['data']
gross_list_with_dates = []

for i in to_list_low(data_dict):
     for j in to_list_high(data_dict):
         if j[1] > i[1]:
             gross_list_with_dates.append([j[0]-i[0], i[1], j[1]])

gross_list_with_dates.sort(reverse=True)
print(gross_list_with_dates[0])
