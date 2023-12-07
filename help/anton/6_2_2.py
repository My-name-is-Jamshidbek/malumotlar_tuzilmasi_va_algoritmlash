# 2.	Bir o`lchamli sonli massivni juft qiymatli elementlarini o`rtacha qiymati hisoblansin

uzunligi = int(input("Massiv uzunligi>>"))
massiv = []
for i in range(uzunligi):
    son = int(input(f"{i+1} - son>>"))
    massiv.append(son)

yigindi = 0
soni = 0

for i in massiv:
    if i%2 == 0:
        yigindi += i
        soni += 1

print(f"Juft sonlarning o'rtacha qiymati>> {yigindi/soni}")