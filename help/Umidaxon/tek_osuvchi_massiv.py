def osuvchi_massiv(l):
    """
    massivni osuvchiligini tekshiradi
    :param l: list()
    :return:  boolean()
    """
    a = l[0]
    for i in range(1,len(l)):
        if a>=l[i]:
            return False
        a = l[i]
    return True
print(osuvchi_massiv([0,14,3,4,5]))