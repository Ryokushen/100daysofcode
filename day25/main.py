
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color = data['Primary Fur Color'].drop_duplicates()
colors = fur_color.tolist()

fur_color_gray_count = sum(data['Primary Fur Color'] == 'Gray')
fur_color_cin_count = sum(data['Primary Fur Color'] == 'Cinnamon')
fur_color_black_count = sum(data['Primary Fur Color'] == 'Black')
counts = [fur_color_gray_count, fur_color_cin_count, fur_color_black_count]

data1 = {'color': colors[1:],
         'count': counts
         }
data2 = pandas.DataFrame(data1)
data2.to_csv('squirrel_count.csv')

