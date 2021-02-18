def add(x, y):
    return bin(int(x, 2) + int(y, 2))
def sub(x, y):
    return bin(int(x, 2) - int(y, 2))
def mult(x, y):
    return bin(int(x, 2) * int(y, 2))
def div(x, y):
    return bin(int(x, 2) / int(y, 2))
def _invert(x):
    return bin(~int(x, 2) ^ 0xF)

def dinvert(d):
    if d == "0":
        return "1"
    elif d == "1":
        return "0"
    else:
        return d


def invert(x):
    znak = ""
    if x[0] == "0":
        znak = "-"
        l = list(x)[2:]
    else:
        l = list(x)[3:]
    for i in range(0, "".join(l).rindex("1")):
        l[i] = dinvert(l[i])
    return znak + "0b" + "".join(l)


def sdvig(x, D):
    a = x
    a = a.replace("-0", "1")
    a = list(a)
    for _ in range(D):
        a.insert(2, a[0])
        a.pop()
    if a[0] == "1":
        a[0] = "-"
        a.insert(1, "0")
    return "".join(a)


def lsdvig(x):
    a = x
    if a[0] == "0":
        r = "0"
        _r = r
        ri = 2
    else:
        r = "1"
        _r = "-0"
        ri = 3
    c = 0
    l = list(a)[ri:]
    for i in l:
        if i == r:
            c += 1
        else:
            break
    for i in range(c):
        l.pop(0)
        l.append("0")
    return _r + "b" + "".join(l), c


# In[469]:


def asdn1(mx, my, ex, ey, uslovie="+"):
    if ex[0] == "-":
        D = sub(ex, invert(ey))
    else:
        D = sub(ex, (ey))
    print("D=", D)
    _D = int(D, 2)
    print("D=", _D)

    if _D > 0:
        print("D > 0")
        my = sdvig(my, _D)
        print("sdvig=", my)
    elif _D < 0:
        print("D < 0")
        D2 = invert(D)
        if D2[0] != D[0]:
            if D2[0] == "-":
                D2.replace("-0", "0", 1)
            else:
                D2.replace("0", "-0", 1)
        D = D2
        _D = int(D, 2)
        print("-D=", D, "->", _D)
        mx = sdvig(mx, _D)
        print("sdvig=", mx)

    if uslovie == "+":
        mz = add(mx, invert(my))
    else:
        mz = sub(mx, invert(my))
    if mz[0] == "-":
        mz = mz.replace("-0", "0", 1)
    else:
        mz = mz.replace("0", "-0", 1)
    print("Mz=", mz)

    if ex > ey:
        ez = ex
    elif ey > ex:
        ez = ey
    print("ez=", ez)

    if (mx[0] == "-" and my[0] == "-" and mz[0] == "0") or (mx[0] == "0" and my[0] == "0" and mz[0] == "-"):
        mz = sdvig(mz, 1)
        if mx[0] == "-":
            mz = mz.replace("0", "-0", 1)
        else:
            mz = mz.replace("-0", "0", 1)
        ez = add(ez, bin(1))
        print("ez+1=", ez)
    elif mz[0] == "0" and mz[0] == mz[2] or mz[0] == "-" and mz[3] == "1":
        mz, cc = lsdvig(mz)
        ez = sub(ez, bin(cc))
        print(f"ez-{cc}=", ez)
    print("Mz=", mz)



mx = "-0b0001110"
my = "-0b0111011"
ex = "0b1010"
ey = "0b1000"

asdn1(mx, my, ex, ey, "+")