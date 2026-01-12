class Pogoda:
    def __init__(self, miasto, temp):
        self.miasto = miasto
        self.temp = temp

    def __str__(self):
        if self.temp > 0:
            znak = "+"
        else:
            znak = ""
            
        return self.miasto + ":" + znak + str(self.temp) + "C"

if __name__ == "__main__":
    print(Pogoda("Krakow", 15))
    print(Pogoda("Zakopane", -5))