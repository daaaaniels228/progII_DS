import csv
with open('agenti.csv',newline= '',encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=";")
    saraksts=[]
    for row in csvreader:
        if row[0] == "Valsts iestāde" or row[0] == "Izglītības iestāde":
            splitted = row[2].split(",")
            #print(splitted)
            if splitted[1] == " Rīga":
                saraksts.append(row[1])
    #print(saraksts)
    sortedSaraksts = saraksts.sort()
    print(sortedSaraksts)
    print(type(sortedSaraksts))
        
