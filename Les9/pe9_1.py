while True:
    try:
        bedrag = 4356
        aantal = int(input('Aantal='))
        if aantal < 0:
            raise AssertionError('Negatieve getallen zijn niet toegestaan!')
        resultaat = bedrag / aantal
        print(resultaat)
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except AssertionError as error:
        print(error)
    except:
        print("Onjuiste invoer!")