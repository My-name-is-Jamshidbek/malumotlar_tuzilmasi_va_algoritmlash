a1,b1,c1,a2,b2,c2,m1,m2,ind1,ind2 = 0,0,0,0,0,0,0,0,0,0
m=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    m[i] = list(map(int,input().split()))
if (m[0][0]+m[1][1]+m[2][2])==(m[2][0]+m[2][1]+m[3][2]) and (sum(m[0])==sum(m[1])==sum(m[2])):
    pass