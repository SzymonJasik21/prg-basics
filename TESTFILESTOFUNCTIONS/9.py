#import random
#for i in range (10) : #od 0 do 9 ( ostatnia nie jest brana pod uwage)
#for i in range (10): 
 #   x = random.random() * 100 #do 100
#print ( x )


import random

osoby = ['Ania', 'Bartek', 'Kasia', 'Piotr']
wybrana_osoba = random.choice(osoby)
print(wybrana_osoba)

# Tak robiono dawniej (trudniejsze i mniej czytelne):
random.shuffle(osoby)
print(osoby)       #  ----> losowa kolejnosc listy

litery = 'abcdefgh'
losowa_litera = random.choice(litery)
print(losowa_litera)