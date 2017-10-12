def namen():
    counter = {}
    while True:
        name = input('Volgende naam:')
        if name != '':
            if name in counter:
                counter[name] += 1
            else:
                counter[name] = 1
        else:
            break
    for item in counter:
            print('Er is {1:} student met de naam {0:}'.format(item,counter[item]))
namen()