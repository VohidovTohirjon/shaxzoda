from Shaxzoda import *
from Aylana import *

#Endi barcha klasslarni yig'gan holda main, ya'ni asosiy python faylida ularni ishlatishga harakat qilamiz

testcase = int(input()) #testcaselar sonini integer sifatida yozamiz
while testcase != 0:    #testcaselar nechta bo'lsa shuncha marta cikl amalga oshiriladi
    x, y, x1, y1 = map(int, input().split()) #koordinatalarni olamiz

    tekshirish = Shaxzoda(Nuqta(x, y), Nuqta(x1, y1))
    sum = 0
    planets = int(input())

    while planets != 0:

        x, y, r = map(int, input().split())
        Circle = Aylana(r, Nuqta(x, y))

        if tekshirish.kesibUtadimi(Circle) == True:
            sum += 1
        planets -= 1
    print(sum)
    testcase -= 1