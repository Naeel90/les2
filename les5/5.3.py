kaart= open('kaartnummers.txt','r')
linen=kaart.readlines()
kaart.close()

aantalregels=len(linen)

print('deze file telt',aantalregels,'regels')

hkaarnummer=0
rnummer=0
regel=0

for line in linen:
    regel+=1
    elm= line.split(",")
    kaarnummer =int(elm[0])
    if kaarnummer>hkaarnummer:
        hkaarnummer=kaarnummer
        rnummer=regel

print('het grootste kaart nummer is:',hkaarnummer,"dat staat op regel",rnummer)
