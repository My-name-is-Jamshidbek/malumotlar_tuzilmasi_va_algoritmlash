with open('matn.txt','r') as file:
    text = file.read()
    file.close()
raqamlar = []
print('Simvollar>> ')
for i in text:
    if i.isdigit():
        raqamlar.append(i)
    print(i,end='')
print('\nRaqamlar>> ')
for i in raqamlar:print(i,end='')

