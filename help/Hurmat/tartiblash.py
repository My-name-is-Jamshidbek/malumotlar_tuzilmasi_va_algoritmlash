def selectionSort(a, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if a[j] < a[min_index]:
                min_index = j
        (a[ind], a[min_index]) = (a[min_index], a[ind])


massiv = list(map(int,input('malumotlarni probel bilan ajratgan holda kiritin>>').split()))
selectionSort(massiv,len(massiv))
for i in massiv:print(i)
