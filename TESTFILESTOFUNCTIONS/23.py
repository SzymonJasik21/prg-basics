#eng2sp = {'one ': 'uno ', 'two ': 'dos ', 'three ': 'tres '}
#print ( eng2sp )
#{'one ': 'uno ', 'two ': 'dos ', 'three ': 'tres '}

#print ( eng2sp ['two '])

#vals = list ( eng2sp . values () )
#'uno' in vals

#print(vals)

#len( eng2sp )
#print(len( eng2sp ))

word = 'brontosaurus'
d = dict()
for c in word :
    if c not in d :
        d[c] = 1
    else :
        d[c] = d [c] + 1
print (d)

