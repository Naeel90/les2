import datetime
import csv
with open('inloggers.csv', 'w', newline='') as overheidCSV:
    writer = csv.writer(overheidCSV, delimiter=';')
    writer.writerow(('Data', 'Voorletter', 'Achternaam', 'Geboortedatum', 'Email'))
    while True:
        vandaag = datetime.datetime.today()
        tijd = vandaag.strftime("%a %d %b %Y at %H:%M")
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        writer.writerow((tijd,voorl, naam, gbdatum, email))