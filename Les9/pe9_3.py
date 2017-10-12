import csv
with open('gamers.csv', 'r') as Gemerscsv:
    lezer = csv.reader(Gemerscsv, delimiter=';')
    lst = []
    for i in lezer:
        lst.append([i[0],i[1], int(i[2])])
    print(lst)
