import math
a, b, c, d, x = map(int, input().split())

if d == 0:
    y = ((2 * c ** 2) + a * b * math.cos(x ** 2)) / (a * math.sin(x ** 2) + b ** 3)
else:
    y = (2 * b * c + a ** 2) / ((a * 3) + (2 * c ** 2) + d ** 3)

print("%.2f" % y)
