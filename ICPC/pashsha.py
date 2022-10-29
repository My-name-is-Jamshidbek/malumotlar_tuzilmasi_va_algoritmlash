t = int(input())
x1,y1,z1 = list(map(float,input().split()))
vx1,vy1,vz1 = list(map(float,input().split()))
x2,y2,z2 = list(map(float,input().split()))
vx2,vy2,vz2 = list(map(float,input().split()))
m=(((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))**0.5
for i in range(10,((t+1)*10),5):
    i = i/10
    x1, y1, z1 = vx1 + x1, vy1 + y1, vz1 + y1
    x2, y2, z2 = vx2 + x2, vy2 + y2, vz2 + y2
    l = (((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2))**0.5
    if m>l:m=l
print("%.6f"%m)

