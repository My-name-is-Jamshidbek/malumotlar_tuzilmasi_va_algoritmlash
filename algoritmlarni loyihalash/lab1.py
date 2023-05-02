import math

a, b, c = map(int, input().split())

if a == 0:
    if b == 0:
        if c == 0:
            print("-1")
        else:
            print("0")
    else:
        x = -c / b
        print("1")
        print("{:.4f}".format(x))
else:
    D = b * b - 4 * a * c
    if D < 0:
        print("0")
    elif D == 0:
        x = -b / (2 * a)
        print("1")
        print("{:.4f}".format(x))
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("2")
        print("{:.4f}".format(x1))
        print("{:.4f}".format(x2))

# https://acmp.ru/index.asp?main=task&id_task=411