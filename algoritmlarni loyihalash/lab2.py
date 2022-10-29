n = int(input())
# ishtirokchilar natijalarini saqlash uchun lugat yaratamiz
results = {}

# ishtirokchilar malumotlarini qabul qilish
for i in range(n):
    # ism, yechilgan masalaalr, jarima vaqti
    name, solved, penalty = input().split()
    solved = int(solved)
    penalty = int(penalty)

    # ishtirokchilar malumotlarini saqlash
    results[name] = (solved, penalty)

# tartiblash
sorted_results = {}


# ekranga chiqarish
for i, (name, (solved, total_time)) in enumerate(sorted_results):
    print(f"{i+1}. {name} {solved} {total_time}")
