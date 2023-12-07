rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = [int(x) for x in input(f"Введите элементы строки {i+1}, разделенные пробелом: ").split()]
    matrix.append(row)

columns_without_zeros = 0

for j in range(cols):
    has_zero = False
    for i in range(rows):
        if matrix[i][j] == 0:
            has_zero = True
            break

    if not has_zero:
        columns_without_zeros += 1

print(f"Количество столбцов без нулевых элементов: {columns_without_zeros}")
