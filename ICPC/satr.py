t = int(input())
x1,y1,z1 = list(map(int,input().split()))
vx1,vy1,vz1 = list(map(int,input().split()))
x2,y2,z2 = list(map(int,input().split()))
vx2,vy2,vz2 = list(map(int,input().split()))
min = 0
if (vx1>vx2 and vy1>vy2 and vz1>vz2) or (vx1<vx2 and vy1<vy2 and vz1<vz2):
	print('0.000000')
for i in range(1,t+1):
	sx1, sy1, sz1 = vx1 * i, vy1 * i, vz1 * i
	sx2, sy2, sz2 = vx2 * i, vy2 * i, vz2 * i
	sx = (sx1-sx2)
	sy = (sy1-sy2)
	sz = (sz1-sz2)
	if (min>(sx+sy+sz)):
		min = sx+sy+sz
print(min)

