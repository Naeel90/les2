voornaam = input('Voer uw voornaam in: ')
begin_s = input('Wat is uw begin station: ')
eind_s = input('Wat is uw eind station: ')
cobinatie = voornaam + begin_s + eind_s

def code(invoerstring):
    for i in range(0, len(invoerstring)):
        resultaat = chr(ord(invoerstring[i]) + 3)
        print(resultaat, end='')

code(cobinatie)