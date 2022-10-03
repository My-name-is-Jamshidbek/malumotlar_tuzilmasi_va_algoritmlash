#1-step: Start
#2-step: We take n as factorial and create variables i
#3-step: factorial=1 , i=1
#4-step: until i = n
#                   factorial = factorial * i
#                   i = i+1
#5-step: return factorial
#6-step: Stop



def factorial_while_loop(n,factorial=1,i=1):
    while i != n:
        factorial*=i
        i+=1
    return factorial

def factorial_for_loop(n,factorial=1):
    for i in range(1,n):factorial*=i
    return factorial

def factorial_recursion(n,factorial = 1,):
    if n==1:return factorial
    return factorial_recursion(n-1,factorial*n)

