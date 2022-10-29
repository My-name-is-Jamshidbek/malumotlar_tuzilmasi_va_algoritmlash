"""
Butun massiv numsva butun son berilgan bo‘lsa, pastki qator elementlarining eng kichik umumiy karrali bo‘lgan pastki qatorlar soninik qaytaring .numsk

Quyi massiv - massiv ichidagi elementlarning qo'shni bo'sh bo'lmagan ketma-ketligi.

Massivning eng kichik umumiy karrali massivning barcha elementlariga bo‘linadigan eng kichik musbat sondir.
"""


class Solution:
    def subarrayLCM(self, nums: list[int], k: int) -> int:
        m = ''
        k1 = k
        for i in nums:m+=str(i)
        k = str(k)
        n = 0
        while len(k)<=len(m):
            print(k, m)
            if k in m:
                print(k,m)
                n+=1
            k = str(int(k)+k1)
        return n
# a = Solution()
# print(a.subarrayLCM(nums = [3,6,2,7,1], k = 6))

#royxatni n-chi elementi o'chirilsin
m = list(map(int,input("Ro'yxat elementlarini probel bilan ajratgan holda kiriting>>").split()))
n = int(input("N sonini kiriting>>"))
m.pop(n-1)
print("natija>> ",end="")
for i in m:print(i,end=" ")

#royxat boshiga element qoshish
m = list(map(int,input("Ro'yxat elementlarini probel bilan ajratgan holda kiriting>>").split()))
n = int(input("boshiga qo'shiladigan elementni kiriting>>"))
m.insert(0,n)
print("natija>> ",end="")
for i in m:print(i,end=" ")

#n - chi elementdan keyin element qoshish
m = list(map(int,input("Ro'yxat elementlarini probel bilan ajratgan holda kiriting>>").split()))
q = int(input("boshiga qo'shiladigan elementni kiriting>>"))
n = int(input("N sonini kiriting>>"))
m.insert(n,q)
print("natija>> ",end="")
for i in m:print(i,end=" ")
