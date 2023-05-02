import sys

n, x = map(int, input().split())
for i in range(n):
    print("+", x)
    sys.stdout.flush()
    digit = int(input())
    x = (x - digit + n) % n + 1
print("!", x)
sys.stdout.flush()
