def kwader(grondtalen):
    grondtal=0
    for i in grondtalen:
        if i >0:
            grondtal=grondtal+(i**2)
    print(grondtal)
kwader([5,4,3,-81])
