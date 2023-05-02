def __int_list__(m=0,ajratish=' '):
    if m:
        _list = []
        for i in range(m):_list.append(list(map(int,input().split(ajratish))))
    else:_list = list(map(int,input().split(ajratish)))
    return _list
def __float_list__(m=0,ajratish=' '):
    if m:
        _list = []
        for i in range(m):_list.append(list(map(float,input().split(ajratish))))
    else:_list = list(map(float,input().split(ajratish)))
    return _list
def __str_list__(m=0,ajratish=' '):
    if m:
        _list = []
        for i in range(m):_list.append(list(map(str,input().split(ajratish))))
    else:_list = list(map(str,input().split(ajratish)))
    return _list
def __bool_list__(m=0,ajratish=' '):
    if m:
        _list = []
        for i in range(m):_list.append(list(map(bool,input().split(ajratish))))
    else:_list = list(map(bool,input().split(ajratish)))
    return _list
def __str_input__(n=0):
    if n:
        _input = []
        for i in range(n):_input.append(str(input()))
    else:_input = str(input())
    return _input
def __int_input__(n=1):
    if n:
        _input = []
        for i in range(n):_input.append(int(input()))
    else:_input = int(input())
    return _input
def __bool_input__(n=1):
    if n:
        _input = []
        for i in range(n):_input.append(bool(input()))
    else:_input = bool(input())
    return _input
def __float_input__(n=1):
    if n:
        _input = []
        for i in range(n):_input.append(float(input()))
    else:_input = float(input())
    return _input
def __list_to_str__(_list,matritsa=False):
    if matritsa:
        def f(n):return list(map(str,n))
        _list_ = list(map(f,_list))
    else:
        _list_ = list(map(str,_list))
    return _list_

def __list_to_int__(_list,matritsa=False):
    if matritsa:
        def f(n):return list(map(int,n))
        _list_ = list(map(f,_list))
    else:
        _list_ = list(map(int,_list))
    return _list_
def __list_to_float__(_list,matritsa=False):
    if matritsa:
        def f(n):return list(map(float,n))
        _list_ = list(map(f,_list))
    else:
        _list_ = list(map(float,_list))
    return _list_
def __list_to_bool__(_list,matritsa=False):
    if matritsa:
        def f(n):return list(map(bool,n))
        _list_ = list(map(f,_list))
    else:
        _list_ = list(map(bool,_list))
    return _list_
def __ekub__(a,b):
    if a==0 or b==0:return a+b
    if a>b:a = a%b
    else: b = b % a
    return __ekub__(a,b)
def __ekub_list__(a,b):
    _max = (a if a>b else b)
    while True:
        if _max%a==0 and _max%b==0:return _max
        _max+=1
def __to_ascii__(a):return ord(a)
def __ascii_to__(a):return chr(a)
def __sonning_boluvchilari__(son):
    _list = []
    for i in range(1,son+1):
        if son%i == 0:_list.append(i)
    return _list
def __sonning_tub_kopaytuvchilari__(son,dict=False):
    if dict:
        c,_dict = 2,{}
        while (son > 1):
            if (son % c == 0):
                if c in _dict:_dict[c]+=1
                else:_dict[c]=1
                son = son / c
            else:c = c + 1
        return _dict
    else:
        c,_list = 2,[]
        while (son > 1):
            if (son % c == 0):
                _list.append(c)
                son = son / c
            else:c = c + 1
        return _list
def __sonning_boluvchilari_soni__(son):
    c,_dict = 2,{}
    while (son > 1):
        if (son % c == 0):
            if c in _dict:_dict[c]+=1
            else:_dict[c]=1
            son = son / c
        else:c = c + 1
    nbs = 1
    for i in _dict:
        nbs*=_dict[i]+1
    return nbs


def fibonaci(n,f = [0, 1]):
    if n == 0:return sum(f)
    f.append(f[-1] + f[-2])
    return fibonaci(n-1,f)


def fibonacci(n,f = [0, 1]):
    if n == 1:return sum(f)
    f.append(f[-1] + f[-2])
    return fibonacci(n-1,f)

def __ekuk__(a,b,m=0):
    _max = (a if a>b else b)+m
    if _max%a==0 and _max%b==0:return _max
    else:return __ekuk__(a=a,b=b,m=m+1)



def ekub(a,b,c,n=0):
    m = min(a,b,c)
    if a%m==0 and b%m==0 and c%m==0:return m
    else:return ekub(a,b,c,n+1)


def reverse(matn):
    if len(matn) == 1:return matn
    else:return matn[-1]+reverse(matn[:-1])


def prev(son):
    print(son%10,end='')
    if son >= 10:
        prev((son-(son%10))/10)
def fact(n,m=1,s=1):
    if m==n:return s-1
    else:return fact(n,m*s,s+1)



