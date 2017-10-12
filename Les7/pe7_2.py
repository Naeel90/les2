while True:
    woord = input('Geef een string van vier letters:')
    if len(woord) != 4:
        print('{} heeft {} letters'.format(woord,len(woord)))
    else:
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break