# 2.	Matnli faylda nechta “a” va “.” qatnashayotganligini aniqlovchi dastur tuzing.
with open("fayl.txt") as f:
    m = f.read()
    f.close()

a = 0
n = 0
for i in m:
    if i == "a":
        a+=1
    elif i == ".":
        n+=1
print(f"Fayldagi a lar soni {a} . lar soni {n}")