arr = [int(x) for x in input().split()]
m = int(input())
total_sum = 0
count = 0

for element in arr:
    if element > m:
        total_sum += element
        count += 1

if count > 0:
    average = total_sum / count
    print(average)
else:
    print(f"Mavjud emas")
