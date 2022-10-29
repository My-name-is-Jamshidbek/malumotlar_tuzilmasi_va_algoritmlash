q1 = int(input())
q2 = int(input())
q3 = int(input())
q = int(input())

for j in range(3*(q-1)+1,3*q+1):print(j)
for j in range(((3*q1)+(3*(q-1))+1),((3*q1)+(3*q)+1)):print(j)
for j in range(((3*q2)+(3*q1)+(3*(q-1))+1),((3*q1)+(3*q2)+(3*q)+1)):print(j)