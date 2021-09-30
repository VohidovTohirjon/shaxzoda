from Nuqta import  *

###public propertylar: markaz:Nuqta, radius butun son
        ###- public methodlar: kesibUtadimi(), Aylana qabul qiladi va
            ###shaxzoda shu aylanani kesib o'tsa True, bo'lmasa False qaytaradi"""
class Aylana:
    radius = 0
    markaz = Nuqta(0, 0)

    def __init__(self, radius:int, markaz:Nuqta):
        self.radius = radius
        self.markaz = markaz

    def niIchidami(self, nuqta: Nuqta):
        return (True if self.markaz.gachaMasofa(nuqta) < self.radius else False)