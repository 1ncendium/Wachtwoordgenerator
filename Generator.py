# Code door Remco van der Meer, gemaakt op 5/14/2019

import random
import pyperclip

symbool = 0
kleine = 0
grote = 0
nummer = 0
aantal = 0
wachtwoord = []

lengte = input("Welkom, hoelang wil je dat je wachtwoord wordt? (standaard is 20)\n")
lengte = 20 if lengte is '' else int(lengte)

while aantal < lengte:
    rand = random.randint (0,3)
    if rand == 0:
        kleine += 1
        b = int(random.randint (97,123))
        wachtwoord.append(b)
    elif rand == 1:
        grote += 1
        b = random.randint (65,91)
        wachtwoord.append(b)
    elif rand == 2:
        nummer += 1
        b = random.randint (48,58)
        wachtwoord.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbool += 1
        if r == 0:
            b = random.randint (33,48)
            wachtwoord.append(b)
        elif r == 1:
            b = random.randint (91,97)
            wachtwoord.append(b)
        elif r == 2:
            b = random.randint (123,126)
            wachtwoord.append(b)
    aantal += 1

wachtwoord = "".join([chr(c) for c in wachtwoord])

pyperclip.copy(wachtwoord)

print ("Je geweldige nieuwe wachtwoord van %s karakters lang is: \n" % lengte)

print('✈✈✈✈✈')
print(wachtwoord)
print('✈✈✈✈✈')

print ("\nUitstekende keuze, je wachtwoord bevat",kleine,"kleine letters,",grote,"grote letters ,",nummer,"nummers en",symbool,"symbolen")
input('Je nieuwe wachtwoord is gekopieerd naar het clipboard.')
