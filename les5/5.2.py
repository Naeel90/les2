kaart= open('kaartnummers.txt','r')
kaartten=kaart.readlines()

for g in kaartten:
    lis=g.strip().split(',')
    print('{} heeft kaartnummer:{}'.format(lis[1],lis[0]))
kaart.close()




