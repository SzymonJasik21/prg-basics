def check_order(word, target):
    if word < target:
        return 'przed słowem'
    elif word > target:
        return 'po słowie'
    else:
        return 'to samo słowo'

if __name__ == "__main__":
    owoc = 'banan'
    testowy = 'agrest'
    
    relacja = check_order(testowy, owoc)
    print('Twój wyraz, ' + testowy + ', jest ' + relacja + ' ' + owoc + '.')
    