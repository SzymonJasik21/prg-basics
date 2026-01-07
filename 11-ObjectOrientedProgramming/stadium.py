class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total = 0
        for sector_letter in s:
            if sector_letter in self.sectors:
                total += self.sectors[sector_letter]
        return total