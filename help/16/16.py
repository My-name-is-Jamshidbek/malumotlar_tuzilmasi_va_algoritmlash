with open('matn.txt','r') as file:
    text = file.read()
    file.close()
a = input('a harfini kiriting>>')
a1 = 0
for i in text:
    if i == a:a1+=1
print(f"Matnda {a} harfi {a1} marta qatnashgan.")