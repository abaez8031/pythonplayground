import pandas

# with open("weather_data.csv") as data_file:
#   data = weather_data.readlines()
#   print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# {
    # 'day': {
    # 0: 'Monday',
    # 1: 'Tuesday',
    # 2: 'Wednesday',
    # 3: 'Thursday',
    # 4: 'Friday',
    # 5: 'Saturday',
    # 6: 'Sunday'
    # },
    # 'temp': {
    # 0: 12,
    # 1: 14,
    # 2: 15,
    # 3: 14,
    # 4: 21,
    # 5: 22,
    # 6: 24
    # },
    # 'condition': {
    # 0: 'Sunny',
    # 1: 'Rain',
    # 2: 'Rain',
    # 3: 'Cloudy',
    # 4: 'Sunny',
    # 5: 'Sunny',
    # 6: 'Sunny'
    # }
# }

# temp_list = data["temp"].to_list()

# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].median())
# print(data["temp"].mode())
# print(data["temp"].max())

# Get data in columns
# print(data.temp)
# print(data["temp"])

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# id, furcolor, count

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
