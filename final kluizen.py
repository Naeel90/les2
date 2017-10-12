max_kluizen = 12

def lees_kluizen():
    bestand=open('kluizen.txt', 'r+')
    regels=bestand.readlines()
    bestand.close()

    kluizen=[] #apaart1

    for regel in regels:

        split =regel.strip().split(',')
        kluis = [int(split[0]), split[1]]
        kluizen.append(kluis)
    return ( kluizen)

def schrijf_kluizen(kluizen):
    print("schrijf bestand")
    bestand=open("kluizen.txt","w")
    for kluis in kluizen:
        bestand.write(str(kluis[0])+','+kluis[1]+"\n")
    bestand.close()


def toon_aantal_kluizen_vrij():
    print("toon_aantal_kluizen vrij")
    kluizen=lees_kluizen() #apaart2
    print("Aantal kluizen vrij:",max_kluizen-len( kluizen))

def nieuwe_kluis():
    print("nieuwe_kluis")
    kluizen=lees_kluizen() #apaart3
    if len(kluizen)< max_kluizen:
        for kluisnummer in range(1,max_kluizen+1):
            gevonden=False
            for kluis in kluizen:
                if kluis[0] == kluisnummer:
                    gevonden=True
                    break
            if gevonden == False:
                 break

        wachtwoord=input("geef een wachtwoord")
        kluis=[kluisnummer,wachtwoord]
        kluizen.append(kluis)
        schrijf_kluizen(kluizen)
    else:
        print("geen kluizen beschikbaar")











def kluis_openen():
    print("kluis_openen")

    kluizennummer=lees_kluizen()
    wachtwoord=input("typ een wacht woord in:")
    open = False

    for kluis in kluizennummer:
        if kluis[1] ==wachtwoord:
            open = True
            break

    if open:
        print("kluis open")
    else:
        print("wachtwoord incorrect")


while True:
    print(" 1: Ik wil weten hoeveel kluizen nog vrij zijn","\n",
"2: Ik wil een nieuwe kluis","\n",
"3: Ik wil even iets uit mijn kluis halen","\n",
"4: Exit")
    myInput = int(input("Geef uw menukeuze: "))
    if myInput == 1:
        toon_aantal_kluizen_vrij()
    elif myInput==2:
        nieuwe_kluis()
    elif myInput==3:
        kluis_openen()

    elif myInput==4:
        break
