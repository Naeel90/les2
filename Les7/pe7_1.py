lst = []
while True:
    getal = eval(input('geef een getal: '))
    if getal != 0:
        lst.append(getal)
    else:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(lst),sum(lst)))
        break

