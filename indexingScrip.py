import json
import itertools

data_json = open('data.json').read()
data = json.loads(data_json)
data_dict = data['data']

gross_diff = 0.0
buy_price = 0
sell_price = 0
buy_date = 0
sell_date = 0

list = []
for i in data_dict[::-1]:
    list.append([i['quote_date'],i['low'],i['high']])

final_list = []
for a, b  in itertools.combinations(list, 2):
    final_list.append([a,b])

for i in final_list:
    # # initialize
    if buy_price == 0:
        gross_diff = i[0][2] - i[0][1]
        buy_price = i[0][1]
        sell_price = i[1][2]
        buy_date = i[0][0]
        sell_date = i[1][0]
    elif gross_diff < (i[1][2] - i[0][1]):
        buy_price = i[0][1]
        sell_price = i[1][2]
        buy_date = i[0][0]
        sell_date = i[1][0]
        gross_diff = sell_price - buy_price

print(buy_price, buy_date, sell_price, sell_date, gross_diff)

