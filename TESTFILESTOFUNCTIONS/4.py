dane = ["Python", "Java", "C++", "JavaScript"]

with open("jezyki.txt", "w") as f:
    print("LISTA JEZYKOW PROGRAMOWANIA", file=f)
    print("-" * 25, file=f)
    for i, jezyk in enumerate(dane, 1):
        print(f"{i}. {jezyk}", file=f)