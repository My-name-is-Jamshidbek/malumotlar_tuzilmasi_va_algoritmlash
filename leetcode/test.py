import math


def primefactors(n):
    rn1 = {}
    tbs = 1
    nbs = 1
    n2=0
    # even number divisible
    while n % 2 == 0:
        n = n / 2
        n2+=1
    # n became odd
    if n2:rn1[2] = n2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while (n % i == 0):
            if i in rn1.keys():
                rn1[i] = rn1[i] + 1
            else:
                rn1[i] = 1
            n = n / i

    if n > 2:
        if n in rn1.keys():
            rn1[n] = rn1[n] + 1
        else:
            rn1[n] = 1
    for i in rn1:
        nbs *= rn1[i] + 1
        if i % 2 != 0:
            tbs *= rn1[i] + 1
    return nbs-tbs

n = int(input())
n1 = []
for i in range(n):
    n2 = int(input())
    n1.append(n2)
for n in n1:print(primefactors(n))