from math import *

class Nuqta:
### public propertylar x va y butun sonni qabul qilmoqda
    ###   konstruktorida x va y ni qabul qilib propertylarga joylaydi
        ### public method: gachaMasofa() → ushbu method boshqa bir
            ### nuqta qabul qiladi joriy nuqtadan o'sha berilgan nuqtagacha
                ###  bo'lgan masofani float sifatida qaytaradi

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def gachaMasofa(self, b):
        return sqrt((self.x - b.x) ** 2 + (self.y - b.y) ** 2)