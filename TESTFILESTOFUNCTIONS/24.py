#counts = { 'chuck ' : 1 , 'annie ' : 42 , 'jan ' : 100 }

#print ( counts . get ('jan ', 0) ) 
#100 ----> index 0 stringu jan czyli 100
#print ( counts . get ('tim ', 0) )  
#0  --- > index 0 stringu time ktorego nie ma czyli wartosc 0

word = 'brontosaurus'
d = dict()
for c in word:
    d [c] = d.get (c,0) + 1
print (d)