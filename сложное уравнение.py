a = int(input())
b = int(input())
c = int(input())
D = (b**2) - 4 * a * c
if a == 0:
    if b == -c:
        print("бесконечность решений")
    else:
        x1 = (-c) / (b)
elif D < 0:
    print("нет решений")
elif D == 0:
    x1 = (-b) / (2 * a)
    print(x1)
else:
    x1 = ((-b) + (D**2)) / (2 * a)
    x2 = ((-b) - (D**2)) / (2 * a)
    print(x1, x2)
