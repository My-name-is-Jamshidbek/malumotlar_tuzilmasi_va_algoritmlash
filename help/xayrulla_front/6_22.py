import math

a = int(input())
b = int(input())
c = int(input())
x = int(input())
z = int(input())
h = int(input())

if (x * z != 0):
    m = math.pow((a / x ** 2), 1 / 5) - math.pow((c ** 2 / b ** 2), 2)
    print("%.2f" % m)
elif a < b:
    m = ((2 * a * b ** 3 + math.ln(c ** 2)) / (math.pow(((a + b) ** 2), 1 / 3) - 2 * math.ln(a * b ** 2)))
    print("%.2f" % m)
else:
    print("Javob yo'q")