cijferICOR= 8
cijferPROG= 7
cijferCSN=  9


gemiddelde= (cijferPROG+cijferCSN+cijferICOR) /3
print(gemiddelde)

beloning= (cijferICOR+cijferCSN+cijferPROG) * 30
print(beloning)

overzicht= "Mijn cijfers gemiddeld een, %s. leveren een beloning van € .%s op!" %(gemiddelde,beloning)
print(overzicht)
