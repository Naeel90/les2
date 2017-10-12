import csv

with open('newfile.csv', 'r', newline='') as myCSVFile:
    lees = csv.reader(myCSVFile, delimiter=';')
    header = next(lees)
    lists = []
    hoog_prijs = 0
    naaam = ""
    for i in lees:
        i[4] = float(i[4].strip())
        if i[4] > hoog_prijs:
            hoog_prijs = i[4]
            naaam = i[2]
    # print(hoog_prijs,"and",naaam)


        # naam = i[2]
        # prijs = float(i[4])
        # voorraad = int(i[3])
        # artikelnummer = int(i[0])
        # artikelcode = i[1]
    #     lists.append([artikelnummer,artikelcode,naam, voorraad,prijs])
    # print(lists)
    # prijs_lst = []
    # for list in lists:
    #     prijs_lst.append(list[4])
    # print(prijs_lst)
    # v_lst = []
    # for list in lists:
    #     v_lst.append(list[3])
    # print(v_lst)
    # print('Het duurste artikel is {} en die kost', max(prijs_lst),' Euro')
    # print('Er zijn slechts',min(v_lst) ,'exemplaren in voorraad van het product met nummer {}')
    # print('In totaal hebben wij' ,sum(v_lst), 'producten in ons magazijn liggen')
    #





    # writer = csv.writer(myCSVFile, delimiter=';')
    # writer.writerow(('Artikelnummer', 'Artikelcode','Naam','Voorraad', 'Prijs'))

    # while True:
    #     a_nr = input('#Artikelnummer? ')
    #
    #     if a_nr == '':
    #         break
    #
    #     a_cd = input('Artikelcode? ')
    #     naam = input('Naam? ')
    #     v = input('Voorraad? ')
    #     prijs = input('Prijs? ')
    #
    #     writer.writerow((a_nr, a_cd,naam,v,prijs))

