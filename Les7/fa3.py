def inlezen_beginstation(stations):
    while True:
        station=input("voer een begin station in :")
        if station in stations:
            return station
        print("dat station bestaat niet, probeer het nogmaals.")

def inlezen_eindstation(stations, beginstation):
    while True:
        station=input("voer een eindstation in:")
        bestaat = False
        if station in stations:
            bestaat = True
        if bestaat == False:
            print("Dit station bestaat niet, probeer het nogmaals.")
        elif stations.index(station) > stations.index(beginstation):
            return station
        else:
            print("Het eindstation moet na het beginstation liggen.")

def omroepen_reis(stations, beginstation, eindstation):
    print("jouw begin station is: ",beginstation, ", het ", stations.index(beginstation)+1, "e station")
    print("jouw eind station is: ",eindstation, ", het ", stations.index(eindstation)+1, "e station")
    print("de afstand bedraagt: ",stations.index(eindstation)-stations.index(beginstation),"station(s)")
    print("de prijs van het kaartje is: ",(stations.index(eindstation)-stations.index(beginstation))*5,"euro")
    print("jij stapt in de trein in: ",beginstation)
    for i in range(stations.index(beginstation)+1,stations.index(eindstation)):
        print("- ", stations[i])
    print("jij stapt uit de trein in: ",eindstation)



stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", "Eindhoven", "Weert",
"Roermond", "Sittard", "Maastricht"]
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
