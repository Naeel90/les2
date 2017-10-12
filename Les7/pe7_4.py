def ticker(filename):
    bestaand = open(filename, encoding='utf-8')
    lees_lst = bestaand.readlines()
    bestaand.close()
    dict = {}
    for line in lees_lst:
        sleutel = line.strip().split(':')[0]
        waarde = line.strip().split(':')[1]
        dict[sleutel]= waarde
    return dict
while True:
    dict = ticker('ticker_symbol.txt')
    company_naam = input('Enter Company name: ')
    for cn in dict:
        if cn == company_naam:
            print('Ticker symbol:',dict[cn])
    ticker_sympol = input('Enter Ticker symbol:')
    for key in dict:
         if dict[key] == ticker_sympol:
            print('Company name:',key)
    break
