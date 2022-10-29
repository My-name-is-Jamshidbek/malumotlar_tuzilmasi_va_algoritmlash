# a = [0,2,1,1]
# for j in range(int(input())):
#     n = int(input())
#     if n<4:print(a[n])
#     else:
#         print(n)
#         print(a[n%3])
#         print(n//3)
#         m = a[n%3]+(n//3)
#         print(m)
# # a = [0,2,1,1]
# # n = 3
# # if n<4:print(a[n])
# # else:
# #     m = a[n%3]+(n//3)
# #     print(m)m\

# 2

import math
a,b,c,x,y = list(map(int,input("Elementlarni probel bilan ajratgan holda kiriting>>").split()))
if x*y!=0:
    q = (x*a*math.sin(y**4)**3-a*b*c*math.cos(x**2)**3)/b*c*y**2
elif b>0:
    q = (a*b**2-2*math.log2(b**2)+3*(c**3)*(x*y)**0.5)/(math.log2(a)+2*(c**2)+(7*a-1)**0.3)
else:
    q=0
print(q)



# 3
z,a,b,x = list(map(int,input("Elementlarni probel bilan ajratgan holda kiriting>>").split()))

s = (a**0.3)*b**3
s1 = 0
for i in range(5,15):
    s1+=(a*i**2+z)/(2*x+b**2)
print(s*s1)