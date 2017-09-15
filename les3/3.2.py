leeftijd= eval(input('geef je leef tijd:'))
pasport= (input('ben je Nederlander:'))


if pasport == "ja" and leeftijd >= 18:
    print('Gefeliciteerd, je mag stemmen ')

else:
    if pasport== "nee" or leeftijd<18:

      print('jij kan niet stemen')
