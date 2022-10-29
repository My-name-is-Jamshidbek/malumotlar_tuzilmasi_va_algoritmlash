import math
def factorial(son,n=1):
    if math.factorial(n) == son:return n
    else:return factorial(son=son,n=n+1)
print(factorial(6))