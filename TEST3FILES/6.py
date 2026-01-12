class Lot:
    def __init__(self, miasto, dystans):
        self.miasto = miasto
        self.dystans = dystans

    def __str__(self):
        if self.dystans > 1000:
            kod = self.miasto[:3].upper() + "LONG"
        else:
            kod = self.miasto[:3].lower() + "SHORT"
        
        return kod + str(self.dystans)

if __name__ == "__main__":
    print(Lot("Warszawa", 1500))
    print(Lot("Berlin", 500))