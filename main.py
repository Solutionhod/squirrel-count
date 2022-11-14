import csv
import pandas

with open("weather_data.csv") as data_file:
    contents = data_file.readlines()
    print(contents)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            new_row = int(row[1])
            temperature.append(new_row)

    print(temperature)


data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
sum_of_temp = 0
for temp in temp_list:
    sum_of_temp += temp

average_temp = sum_of_temp / len(temp_list)
print(average_temp)


# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_data = data["Primary Fur Color"].to_list()
# print(fur_color_data)
gray_color = fur_color_data.count("Gray")
# print(gray_color)
cinnamon_color = fur_color_data.count("Cinnamon")
# print(cinnamon_color)
black_color = fur_color_data.count("Black")
# print(black_color)
squirrel_count_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [gray_color, cinnamon_color, black_color]
}
data = pandas.DataFrame(squirrel_count_dict)
data.to_csv("squirrel_count.csv")
