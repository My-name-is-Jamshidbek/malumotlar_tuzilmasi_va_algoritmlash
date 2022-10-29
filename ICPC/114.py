import math


def equationroots(a, b, c):

    if a == 0 and b != 0 and c != 0:
        print(1)
        print("%.4f"%float(-c/b))
    elif a == 0 and b == 0:
        print(0)
    elif a == 0 and b != 0 and c == 0:
        print(0)
        print(0)
    else:
        dis = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis))

        if dis > 0:
            print(2)
            print("%.4f"%float((-b + sqrt_val) / (2 * a)))
            print("%.4f"%float((-b - sqrt_val) / (2 * a)))

        elif dis == 0:
            print(1)
            print("%.4f"%float(-b / (2 * a)))

        else:
            print(2)
            print("%.4f"%str(- b / (2 * a)))
            print("%.4f"%str(- b / (2 * a)))


a,b,c = list(map(int, input().split()))
for a in range(10000):
    for b in range(10000):
        for c in range(10000):
            print(a,b,c)
            equationroots(a, b, c)
