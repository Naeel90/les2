def standaardtarief(afstandKM):
    if afstandKM > 50:
        return (afstandKM) * 0.60 + 15
    elif (afstandKM) <= 0:
        return (afstandKM) * 0
    else:
        return (afstandKM) * 0.80


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit == True:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardtarief(afstandKM) * 0.35
        else:
            return standaardtarief(afstandKM) * (1 - 0.40)
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return standaardtarief(afstandKM) * (1 - 0.30)
        else:
            return standaardtarief(afstandKM)


print(ritprijs(11, True, 55))
print(ritprijs(11, False, 55))
print(ritprijs(11, False, 40))
print(ritprijs(11, True, 40))
print(ritprijs(11, False, -7))
print(ritprijs(11, True, -7))
print(ritprijs(11, False, 0))
print(ritprijs(11, True, 0))


print(ritprijs(40, False, 55))
print(ritprijs(40, True, 55))
print(ritprijs(40, True, 33))
print(ritprijs(40, False, 33))
print(ritprijs(40, False, -7))
print(ritprijs(40, True, -7))
print(ritprijs(40, False, 0))
print(ritprijs(40, True, 0))

print(ritprijs(66, False, 55))
print(ritprijs(66, True, 55))
print(ritprijs(66, False, 33))
print(ritprijs(66, True, 33))
print(ritprijs(66, False, -7))
print(ritprijs(66, True, -7))
print(ritprijs(66, False, 0))
print(ritprijs(66, True, 0))

