# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
def selectionSort(a, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if a[j] < a[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (a[ind], a[min_index]) = (a[min_index], a[ind])


a = ['f','s','u','g','o','n','i','w','l','x','m','b','r','p','a','e','d','t','c','q','h','y','j','z','v']
size = len(a)
selectionSort(a, size)
print(a)