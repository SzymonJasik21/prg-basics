#friends = ['Józek ', 'Gienek ', 'Staszek ']
#for friend in friends :
 #   print ('Szczęśliwego Nowego Roku ', friend)
#print ('Zrobione !')

#count = 0
#for numbers in [9 , 41 , 12 , 3 , 74 , 15]:
#    count = count + 1
#print ('Ile:', count )

#total = 0
#for numbers in [9 , 41 , 12 , 3 , 74 , 15]:
#    total = total + numbers
#print ('Suma :', total )

#smallest = None
#print ('Przed :', smallest )
#for itervar in [9 , 41 , 12 , 3 , 74 , 15]:
#    if smallest is None or itervar < smallest :
#        smallest = itervar
#    print ('Pętla:', itervar , smallest )
#print ('Po:', smallest )

def find_min(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

if __name__ == "__main__":
    lista_liczb = [9, 41, 12, 3, 74, 15]
    wynik = find_min(lista_liczb)
    print(wynik)