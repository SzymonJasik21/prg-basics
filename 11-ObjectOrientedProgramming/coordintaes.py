class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        count = 0
        for x, y in self.coordinates:
            if x > 0 and y > 0:
                count += 1
        
        return count >= n