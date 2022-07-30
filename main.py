import csv

dwarf = []
stars = []

with open("dwarf.csv") as file:
    for i in csv.reader(file):
        dwarf.append(i)

with open("stars.csv") as file:
    for i in csv.reader(file):
        stars.append(i)

headers1 = stars[0]
planet_data1 = stars[1:]

headers2 = dwarf[0]
planet_data2 = dwarf[1:]

headers = headers1 + headers2
planet_data = []

for i, data in enumerate(planet_data1):
    planet_data.append(planet_data1[i] + planet_data2[i])

with open("StarData.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(planet_data)