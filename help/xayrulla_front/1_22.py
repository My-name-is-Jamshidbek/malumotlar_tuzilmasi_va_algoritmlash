import math

x, y = map(int, input().split())

m = math.cos(2 + x ** 2) + (1 + 3.5 * x ** 2) / (math.cos(y) ** 2)

print("%.2f" % m)
