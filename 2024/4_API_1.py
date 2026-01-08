import csv
with open('agenti.csv',newline= '',encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=";")
    for row in csvreader:
        if row[0] == "Valsts iestāde" or row[0] == "Izglītības iestāde":
            print(row[2]))
        
