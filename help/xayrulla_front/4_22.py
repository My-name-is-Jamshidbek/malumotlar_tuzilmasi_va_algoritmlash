import math

a, b, c, x, y = map(int, input().split())

if a - abs(b) > 0:
    q = (a + b ** 2 + 2 * c ** 3) / math(a * math.sin(x ** 2) ** 2)
    print("%.2f" % q)
elif x * y > a ** 2:
    q = (a ** 2 - 2 * a * math.log(b) + c) / (a + 2 * c ** 2 + a * x * y)
    print("%.2f" % q)
else:
    print("yechim mavjud emas")
