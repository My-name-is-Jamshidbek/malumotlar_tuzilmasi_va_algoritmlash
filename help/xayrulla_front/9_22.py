array = list(map(int, input().split()))

if len(array) != 12:
    print("Ошибка: Введите ровно 12 символов.")
else:
    doubled_codes = [char * 2 for char in array]

    print("Исходные символы:", array)
    print("Удвоенные коды символов:", doubled_codes)
