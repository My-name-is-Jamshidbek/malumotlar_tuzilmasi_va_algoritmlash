A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

v = [sum(row) for row in A]

max_element = max(v)
min_element = min(v)

print("Vector v:", v)
print("Katta element:", max_element)
print("Kichik element:", min_element)
