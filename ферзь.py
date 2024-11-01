# позиция ферзя а1 а2, позиция фигуры b1 b2

a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
c1 = int
c2 = int
k = 20
if a1 == b1:
    print("yes")
elif a2 == b2:
    print("yes")
else:
    c1 = a1  # перенос значений а1 а2 в другую переменную для 2го цикла
    c2 = a2
    a1 = a1 - 8
    a2 = a1 - 8
    for i in k:
        if a1 == b1 and a2 == a1:
            print("yes")
            break
        else:
            a1 = a1 + 1
            a2 = a2 + 1
    c1 = c1 - 8
    c2 = c2 + 8
    for i in k:
        if c1 == b1 and c2 == b2:
            print("yes")
            break
        else:
            c1 = c1 + 1
            c2 = c2 - 1
