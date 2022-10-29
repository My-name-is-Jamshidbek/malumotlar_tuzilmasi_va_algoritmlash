def func():
    l1 = [9,9,9,9]
    l2 = [9,9,9,9]
    l1l = len(l1)
    l2l = len(l2)
    if l2l>l1l:
        l1,l2=l2,l1
        l1l,l2l = l2l,l1l
    for i in range(0,l1l):
        try:l1[i]+=l2[i]
        except:pass
        if l1[i]>9:
            if (i+1)<l1l:
                l1[i+1] += l1[i]//10
                l1[i] = l1[i]%10
            else:
                l1.append(l1[i] // 10)
                l1[i] = l1[i] % 10
    return l1


print(type([1,2,3]))
