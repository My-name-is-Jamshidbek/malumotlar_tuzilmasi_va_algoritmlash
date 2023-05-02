# PYTHON DASTURLASH TILIDA MAP
class Map:
    def __init__(self):
        self.map = {}

    def add(self, key, value):
        self.map[key] = value

    def remove(self, key):
        del self.map[key]

    def get(self, key):
        return self.map.get(key, None)

    def __str__(self):
        return str(self.map)


# O'QIB OLISH
universitetlar = Map()
with open('universitetlar.txt', 'r') as f:
    n = 0
    for line in f:
        n+=1
        universitetlar.add(key=n, value=list(line[:-1].split('|')))

# QIDIRISH
search = input('Qidirilayotgan ma\'lumotni kiriting: ')

results = []
for i in range(n):
    if search in universitetlar.get(i+1):
        results.append(universitetlar.get(i+1))

# NATIJALARNI EKRANGA CHIQARISH
n = 0
for result in results:
    n+=1
    print(f"Natija {n}:\n"
          f"Universitet: {result[0]}\n"
          f"Rektor: {result[1]}\n"
          f"Xodimlar: {result[2]}\n"
          f"Fanlar: {result[3]}\n"
          f"Talabalar: {result[4]}\n"
          f"Professorlar: {result[5]}")