#!/usr/bin/env python
# coding: utf-8

# In[124]:


mx=list("1.0000101")
my=list("1.0100001")
ex=list("0.1010")
ey=list("0.0111")


# In[125]:


def invert(d):
    if d=="0":
        return "1"
    elif d=="1":
        return "0"
    else:
        return d


# In[126]:


def invertion(ey):
    dey=ey
    ddey=ey[::-1]
    theone=0
    for i in range(len(dey)):
        dey[i]=invert(dey[i])
    for i in range(len(ddey)):
        if ddey[i]=="1":
            theone=i
            break
    dey[-1-theone]="1" 
    return dey


# In[127]:


def _add(ex,ey):
    ez = []
    for i in range(len(ey)-1,-1,-1):
        try:
            iex = int(ex[i])
            iey = int(ey[i])
            ez.append(iex+iey)
        except:
            ez.append(ex[i])
    return ez[::-1]


# In[128]:


def overflow(_ez):
    ez = list([i for i in _ez])
    for i in range(len(ez)):
        if ez[i]==2:
            ez[i]=0
            if i-1 > -1:
                if ez[i-1] == ".":
                    ez[i-2]+=1
                else:
                    ez[i-1]+=1
    return ez


# In[129]:


def add(a,b):
    c = _add(a,b)
    while True:
        c=overflow(c)
        if c.count(1) + c.count(0)+1==len(c):
            break
    return c


# In[130]:


def findD(ez):
    D = "".join([str(i) for i in ez[2:]])
    D = int(D,2)
    if ez[0]:
        D*=-1
    return D


# In[131]:


def offset(md,D):
    d = md[0]
    for i in range(D):
        for j in range(len(md)-1,1,-1):
            md[j]=md[j-1]
    for i in range(D):
        md[2+i] = d
    return md


# In[140]:


dey = invertion(ey)
print("".join(dey))
ez = add(ex,dey)
print("".join([str(i) for i in ez]))
D = findD(ez)
print(D)

if D > 0:
    print("ex",">","ey")
    md = my
    ez=ex
else:
    print("ex","<","ey")
    md = mx
    ez=ey
    D=abs(D)+1
    
md = offset(md,D)
print("md =","".join(md))
mz = add(mx,my)
print("mz =","".join([str(i) for i in mz]))
if mx[0]==my[0]:
    mz = offset(mz,1)
    mz[0] = int(invert(str(mz[0])))
print("mz норм. =","".join([str(i) for i in mz]))
ez1 = add(ez,list("0.0001"))
print("ez =","".join([str(i) for i in ez1]))

