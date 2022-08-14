
# list_data = []
# with open('weather_data.csv', mode='r') as template1:
#     for data in template1.readlines():
#         list_data.append(data.strip())
#
# print(list_data)

import csv
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
    temperatures[1:] = [int(x) for x in temperatures[1:]]
    print(temperatures[1:])