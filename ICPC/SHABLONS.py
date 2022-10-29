import numpy as np
def f_len():
    a = np.array(42)
    b = np.array([1, 2, 3, 4, 5])
    c = np.array([[1, 2, 3], [4, 5, 6]])
    d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

    print(a.ndim)
    print(b.ndim)
    print(c.ndim)
    print(d.ndim)
def f_last_element_2d_arr():
    import numpy as np

    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print('Last element from 2nd dim: ', arr[0, -1])
def f_indexs():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    print(arr[-3:-1])
    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    print(arr[1:5:2])
    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    print(arr[::2])
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(arr[1, 1:4])
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(arr[0:2, 2])
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(arr[0:2, 1:4])
# print(f_indexs())
def f_datatype():
    arr = np.array([1, 2, 3, 4])

    print(arr.dtype)
    arr = np.array(['apple', 'bannana', 'cherry'])

    print(arr[1].dtype)

    arr = np.array([1, 2, 3, 4], dtype='S')

    print(arr)
    print(arr.dtype)

    arr = np.array([1, 2, 3, 4], dtype='i4')

    print(arr)
    print(arr.dtype)

    arr = np.array([1.1, 2.1, 3.1])

    newarr = arr.astype('i')

    print(newarr)
    print(newarr.dtype)
    arr = np.array([1.1, 2.1, 3.1])

    newarr = arr.astype(int)

    print(newarr)
    print(newarr.dtype)

    arr = np.array([1, 0, 3])

    newarr = arr.astype(bool)

    print(newarr)
    print(newarr.dtype)

def f_copy():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    arr[0] = 42

    print(arr)
    print(x)

    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    arr[0] = 42

    print(arr)
    print(x)

    arr = np.array([1, 2, 3, 4, 5])
    x = arr.view()
    x[0] = 31

    print(arr)
    print(x)

    arr = np.array([1, 2, 3, 4, 5])

    x = arr.copy()
    y = arr.view()

    print(x.base)
    print(y.base)

def f_shape():
    arr = np.array([[1, 2, 3, 4, 5], [5,6, 6, 7, 8]])

    print(arr.shape)

    arr = np.array([1, 2, 3, 4], ndmin=5)

    print(arr)
    print('shape of array :', arr.shape)

def f_reshape():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    newarr = arr.reshape(4, 3)

    print(newarr)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    newarr = arr.reshape(2, 3, 2)

    print(newarr)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    print(arr.reshape(2, 4).base) #ozi ozgarmid faqat nusxa ozgaradi
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    newarr = arr.reshape(2, 2, -1)

    print(newarr)

    arr = np.array([[1, 2, 3,5], [4,5, 5, 6]])

    newarr = arr.reshape(-1)

    print(newarr)

def f_iterating():
    arr = np.array([1, 2, 3])

    # for x in arr:
    #     print(x)
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # for x in arr:
    #     print(x)
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    # for x in arr:
        # for y in x:
            # print(y)

    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    # for x in np.nditer(arr):
    #     print(x)
    arr = np.array([1, 2, 3])

    # for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    #     print(x)
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    # for x in np.nditer(arr[:, ::2]):
    #     print(x)

    arr = np.array([1, 2, 3])

    # for idx, x in np.ndenumerate(arr):
    #     print(idx, x)

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    # for idx, x in np.ndenumerate(arr):
    #     print(idx, x)
    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    arr = np.concatenate((arr1, arr2))

    # print(arr)

    arr1 = np.array([[1, 2], [3, 4]])

    arr2 = np.array([[5, 6], [7, 8]])

    arr = np.concatenate((arr1, arr2), axis=1)

    # print(arr)

    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    arr = np.stack((arr1, arr2), axis=1)

    # print(arr)

    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    arr = np.hstack((arr1, arr2))

    # print(arr)

    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    arr = np.vstack((arr1, arr2))

    # print(arr)
    arr1 = np.array([1, 2, 3])

    arr2 = np.array([4, 5, 6])

    arr = np.dstack((arr1, arr2))  #kasasina qoshadi

    # print(arr)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    newarr = np.array_split(arr, 3)

    # print(newarr) #bo'ladi

    arr = np.array([1, 2, 3, 4, 5, 6])

    newarr = np.array_split(arr, 4) #ajratadi

    # print(newarr)

    arr = np.array([1, 2, 3, 4, 5, 6])

    newarr = np.array_split(arr, 3)

    # print(newarr[0])
    # print(newarr[1])
    # print(newarr[2])

    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

    newarr = np.array_split(arr, 3) #3 ga boladi

    # print(newarr)
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

    newarr = np.array_split(arr, 3, axis=1)

    # print(newarr) #kasasina massivga yingnidi

    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

    newarr = np.hsplit(arr, 3)

    # print(newarr) #kasasina massivlara yingnid

def f_search():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])

    x = np.where(arr == 4)

    # print(x) #4 ni indexlari
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

    x = np.where(arr % 2 == 0)

    # print(x) #toqlarni chiqaradi
    x = np.where(arr % 2 == 1)

    # print(x) #juftlari
    arr = np.array([7, 7, 8, 9])

    x = np.searchsorted(arr, 7)

    # print(x) #faqat bittasini indeksini qaytaradi
    arr = np.array([6, 7, 8, 7])

    x = np.searchsorted(arr, 7, side='right')

    # print(x)
    arr = np.array([1, 3, 5, 7])

    x = np.searchsorted(arr, [4, 4, 6])

    # print(x)
def f_sort():
    arr = np.array([3, 2, 0, 1])

    print(np.sort(arr)) #Bu usul massivning nusxasini qaytaradi va asl massivni o'zgarishsiz qoldiradi.
    arr = np.array(['banana', 'cherry', 'apple'])

    print(np.sort(arr))

    arr = np.array([True, False, True])

    print(np.sort(arr))
    arr = np.array([[3, 2, 4], [5, 0, 1]])

    print(np.sort(arr))
def f_filtr():
    arr = np.array([41, 42, 43, 44])

    x = [True, False, True, False]

    newarr = arr[x]

    print(newarr)

    arr = np.array([41, 42, 43, 44])

    # Create an empty list
    filter_arr = []

    # go through each element in arr
    for element in arr:
        # if the element is higher than 42, set the value to True, otherwise False:
        if element > 42:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)

    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    # Create an empty list
    filter_arr = []

    # go through each element in arr
    for element in arr:
        # if the element is completely divisble by 2, set the value to True, otherwise False
        if element % 2 == 0:
            filter_arr.append(True)
        else:
            filter_arr.append(False)

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)

    arr = np.array([41, 42, 43, 44])

    filter_arr = arr > 42

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr) #uxti girt filtir

    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    filter_arr = arr % 2 == 0

    newarr = arr[filter_arr]

    print(filter_arr)
    print(newarr)
def f_random():
    from numpy import random
    x = random.randint(100)

    # print(x)

    x = random.rand()

    # print(x)

    x = random.randint(100, size=(5))

    # print(x)

    x = random.randint(100, size=(3, 5))

    # print(x)

    x = random.rand(5)

    # print(x)

    x = random.rand(3, 5)

    # print(x)

    x = random.choice([3, 5, 7, 9])

    # print(x)

    x = random.choice([3, 5, 7, 9], size=(3, 5))

    # print(x)

def f_taqsimlash():
    from numpy import random
    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100)) #p bu foiz boshdaqi asa elementlar

    print(x)

    x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

    print(x)
def f_alashtirish():
    from numpy import random
    import numpy as np

    arr = np.array([1, 2, 3, 4, 5])

    random.shuffle(arr)

    print(arr) #aralashtiradi

    arr = np.array([1, 2, 3, 4, 5])

    print(random.permutation(arr))

def f_distplot():
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.distplot([0, 1, 2, 3, 4, 5])

    plt.show()

    sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

    plt.show()
def f_normal_alashtirish():
    from numpy import random

    x = random.normal(size=(2, 3))

    print(x)
    x = random.normal(loc=2, scale=4, size=(2, 4))

    print(x)
    x = random.binomial(n=10, p=0.5, size=10)

    print(x)
    x = random.uniform(size=(2, 3))

    print(x)
def f_func_add():
    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    z = []

    for i, j in zip(x, y):
        z.append(i + j)
    print(z)
    x = [1, 2, 3, 4]
    y = [4, 5, 6, 7]
    z = np.add(x, y)

    print(z)
def f_func_create():
    def myadd(x, y):
        return x + y

    myadd = np.frompyfunc(myadd, 2, 1)

    print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
def f_func_arifmetic():
    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([20, 21, 22, 23, 24, 25])

    newarr = np.subtract(arr1, arr2)

    print(newarr) #arr2-arr1

    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([20, 21, 22, 23, 24, 25])

    newarr = np.multiply(arr1, arr2)

    print(newarr) #arr1*arr2

    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 5, 10, 8, 2, 33])

    newarr = np.divide(arr1, arr2)

    print(newarr) #arr1/arr2
    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 5, 6, 8, 2, 33])

    newarr = np.power(arr1, arr2)

    # print(newarr) #pow

    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 7, 9, 8, 2, 33])

    newarr = np.mod(arr1, arr2)

    print(newarr) #2 ni 1 ga bolib qoldiqni chiqaradi
    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 7, 9, 8, 2, 33])

    newarr = np.remainder(arr1, arr2)

    print(newarr)

    arr1 = np.array([10, 20, 30, 40, 50, 60])
    arr2 = np.array([3, 7, 9, 8, 2, 33])

    newarr = np.divmod(arr1, arr2)

    print(newarr) #boladi qoldiq addeni butun qismi addnni

    arr = np.array([-1, -2, 1, 2, 3, -4])

    newarr = np.absolute(arr)

    print(newarr) #ommaviy modul


def f_func_qisqartirish():
    arr = np.trunc([-3.1666, 3.6667])

    print(arr)

    arr = np.fix([-3.1666, 3.6667])

    print(arr)

    arr = np.around(3.1666, 2)

    print(arr)

    arr = np.floor([-3.1666, 3.6667])

    print(arr)

    arr = np.ceil([-3.1666, 3.6667])

    print(arr)

def f_func_log():
    arr = np.arange(1, 10)

    print(np.log2(arr))

    arr = np.arange(1, 10)

    print(np.log10(arr))

    arr = np.arange(1, 10)

    print(np.log(arr))
def f_func_summ():
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])

    newarr = np.sum([arr1, arr2])

    # print(newarr)

    arr1 = np.array([1, 2, 3])
    arr2 = np.array([1, 2, 3])

    newarr = np.sum([arr1, arr2], axis=1)

    # print(newarr)

    arr = np.array(np.arange(0,100))

    newarr = np.cumsum(arr)

    print(newarr)
def f_func_product():
    arr = np.array([1, 2, 3, 4])

    x = np.prod(arr) #kopaytiradi

    print(x)

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    x = np.prod([arr1, arr2])

    print(x)

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([5, 6, 7, 8])

    newarr = np.prod([arr1, arr2], axis=1)

    print(newarr)

    arr = np.array([5, 6, 7, 8])

    newarr = np.cumprod(arr)

    print(newarr)

def f_func_differences():
    arr = np.array([10, 15, 25, 5])

    newarr = np.diff(arr)

    print(newarr)#n+1 dan n ni ayiradi

    arr = np.array([10, 15, 25, 5])

    newarr = np.diff(arr, n=2)

    print(newarr) #yuqoridaqi 2x
def f_func_finding_lcm():
    """
    ekub
    :return:
    """
    num1 = 4
    num2 = 6

    x = np.lcm(num1, num2)

    print(x)

    arr = np.array([3, 6, 9])

    x = np.lcm.reduce(arr)

    print(x)

    arr = np.arange(1, 11)

    x = np.lcm.reduce(arr)

    print(x)

def f_func_finding_gcd():
    """
    ekuk
    :return:
    """
    num1 = 6
    num2 = 9

    x = np.gcd(num1, num2)

    print(x)

    arr = np.array([20, 8, 32, 36, 16])

    x = np.gcd.reduce(arr)

    print(x)

def f_func_trigonometrik():
    x = np.sin(np.pi / 2)

    print(x)
    arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])

    x = np.sin(arr)

    print(x)

    arr = np.array([90, 180, 270, 360])

    x = np.deg2rad(arr)

    print(x)

def f_func_giper():
    x = np.sinh(np.pi / 2)

    print(x)
    arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])

    x = np.cosh(arr)

    print(x)
    x = np.arcsinh(1.0)

    print(x)

    arr = np.array([0.1, 0.2, 0.5])

    x = np.arctanh(arr)

    print(x)

def f_func_set():
    arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

    x = np.unique(arr)

    print(x)
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])

    newarr = np.union1d(arr1, arr2)

    print(newarr)

    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([3, 4, 5, 6])

    newarr = np.intersect1d(arr1, arr2, assume_unique=True)

    print(newarr)

    set1 = np.array([1, 2, 3, 4])
    set2 = np.array([3, 4, 5, 6])

    newarr = np.setdiff1d(set1, set2, assume_unique=True)

    print(newarr)
    set1 = np.array([1, 2, 3, 4])
    set2 = np.array([3, 4, 5, 6])

    newarr = np.setxor1d(set1, set2, assume_unique=True)

    print(newarr)
f_func_set()