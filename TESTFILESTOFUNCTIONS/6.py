def procesor():
    historia = []
    
    def dodaj(element):
        nonlocal historia
        historia.append(element)
        return f"Aktualna lista: {historia}"
    
    return dodaj

moj_proces = procesor()
print(moj_proces("A"))
print(moj_proces("B"))