def convert(C ):

     F=C*1.8+32
     return F

def tabel():
     print('{0:10}{1:9}'.format('F','C'))
     for i in range(-30,50,10):
         print('{:}  '.format(convert(i)),(i))

tabel()




