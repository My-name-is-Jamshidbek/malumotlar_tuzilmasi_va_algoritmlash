def kamayuvchi_massiv(l):
    """
    massivni kamayuvchiligini tekshiradi
    :param l: list()
    :return:  boolean()
    """
    a = l[0]
    for i in range(1,len(l)):
        if a<=l[i]:
            return False
        a = l[i]
    return True
a = [15,14,3,4,1]
print(kamayuvchi_massiv(a))