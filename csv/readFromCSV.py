import csv

with open("./csv/example.csv") as csvfile:
  csvContent = csv.reader(csvfile, delimiter=",")

  dates = []
  colours = []
  for row in csvContent:
    colour = row[3]
    date = row[0]

    dates.append(date)
    colours.append(colour)
    print(row)

  print(dates, colours)

  whatColour = input("What colour do you wish to know the date of?")
  index = colours.index(whatColour)

  desiredDate = dates[index]

  print("The date of ", whatColour, " is ", desiredDate)
