from Aylana import *

"""  public propertylari: `start:Nuqta`, `end:Nuqta`
         konstruktorida start va endlar qabul qilinadi va propertylarga joylanadi
        public methodlari: kesibUtadimi() → Aylana qabul qiladi va shaxzoda shu aylanani kesib o'tsa True yo'qsa False qaytaradi"""
class Shaxzoda:

    def __init__(self, start:Nuqta, end:Nuqta):
        self.start  = start
        self.end = end

    def kesibUtadimi(self, Circle: Aylana):
        if Circle.niIchidami(self.start) and Circle.niIchidami(self.end):
                return False
        if Circle.niIchidami(self.start) or Circle.niIchidami(self.end):
            return True
        else:
            return False