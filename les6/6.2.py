lijst=eval(input("Geef lijst met minimaal 10 strings: "))
lys=[]
if len(lijst) >=10:
 for i in lijst:
     if len(i)==4:
         lys.append(i)
 print("De nieuw-gemaakte lijst met alle vier-letter strings is:",lys)

else:
    print(False)



