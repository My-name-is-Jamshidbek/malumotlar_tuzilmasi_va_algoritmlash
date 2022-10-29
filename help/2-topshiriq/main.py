n = int(input())
mass = list(map(int,input().split()))[:n]
m = int(input())
m_mass = []
for i in range(m):
    m1 = int(input())
    m_mass.append(m1)
j = 0
for i in mass:
    if i in m_mass:j+=1
print(j)