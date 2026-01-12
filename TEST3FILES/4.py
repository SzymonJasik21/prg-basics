class Samochod:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok

    def __str__(self):
        if self.rok < 2010:
            status = "OLD"
        else:
            status = "NEW"
        return self.marka + "_" + status + "_" + str(self.rok)

if __name__ == "__main__":
    print(Samochod("Toyota", 2005))
    print(Samochod("Tesla", 2023))