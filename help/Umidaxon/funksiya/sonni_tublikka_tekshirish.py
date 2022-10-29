def tekshirish(son):
    for i in range(2,int(son**0.5)):
        if son%i == 0:return False
    return True
def tubsonlar():
    m = []
    for i in range(101,1000,2):
        if tekshirish(son=i):m.append(i)
    return m
def sonni_raqamlar_yigindisi(son):
    son = str(son)
    rs = 0
    for i in son:rs+=int(i)
    return rs
a = 'avs'
a = a[::-1]
print(a)