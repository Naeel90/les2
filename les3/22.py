def rng(lst):
    res = max(lst) - min(lst)
    return res

lijstVanGebruiker = eval(input('enter een lijst'))

print(rng(lijstVanGebruiker))
