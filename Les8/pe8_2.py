import random
def monopolyworp():
        dobbelsten1 = random.randrange(1, 7)
        dobbelsten2 = random.randrange(1, 7)
        som = dobbelsten1 + dobbelsten2
        if dobbelsten1 == dobbelsten2:
            print(dobbelsten1, '+', dobbelsten2, '=', som, '(dubbel)')

        else:
            print(dobbelsten1, '+', dobbelsten2, '=', som)

monopolyworp()