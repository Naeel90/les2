def seizoen(maand):
    if maand ==1 or maand ==2 or maand == 12:
        print("het is de wintr")


    elif maand >=3 and maand <=5:
        print('het is de lente')

    elif maand >5 and maand <=8:
        print("het is de zomer")


    elif maand>8 and maand <=11:
        print('het is de herfst')
    else:
        print(False)






seizoen(-1)

