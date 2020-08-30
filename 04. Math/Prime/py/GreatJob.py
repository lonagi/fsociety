from scipy.interpolate import CubicSpline

import sys
sys.path.append('/home/tardis/jup')
from jupmain import *
setup_theme()

N=101

def DO234FDT34F(n):
    df=[i for i in range(1,n**2+1)]
    df=np.array(df,dtype=object)
    df=np.reshape(df,(-1,n))
    df=df.tolist()
    df=np.array(df)

    x=[] #lj
    y=[] #k
    
    mins=[]

    for k in range(1,((n-1)//2)+1):
        #print("k=",k)
        print("")
        y.append(k)
        a=n-k*((n-1)//k)
        i=0
        l1=k
        xt=[]
        
        nom=[]
             
        while(i<a+1):
            print(l1," #",end=" ")
            xt.append(l1)
            for c in range(1,(l1//a) + 1):
                lj=l1-c*a
                print(lj,end=", ")
                if(len(x)-1==len(xt)-1):
                #if(k==lj):
                    #print("lk=",lj)
                    pass
                if(len(x)-1==len(xt)-1 and lj!=l1):
                    if(lj <= a):
                        mins.append(lj)
                    else:
                        pass
                        #nom.append(lj)
                xt.append(lj)
            l1+=k-a*(l1//a)
            i+=1
            lj=l1
        if(mins):
            pass
            #print("k= ",k," kmins=",mins)
        if(nom):
            pass
            #print("k= ",k," knom=",nom)
        x.append(xt)
        #print("\n")
        #print("k= ",k," kmins=",mins)

for i in [N]:
    DO234FDT34F(i)


df=pd.read_csv("../c"+str(N)+".csv").apply(np.int64)
#df=pd.read_csv("../c"+str(N)+".csv")
#df=df.diff(axis=1).apply(np.int64)

dfnp=df.to_numpy(dtype="object").tolist()
dfnp2=df.to_numpy(dtype="object").tolist()

for i in range(len(dfnp2)):
    a=0
    for j in range(len(dfnp2[i])):
        if( ((N-1)//(i+1))-1>1 and dfnp2[i][j]-dfnp2[i][j-1]<0):
            for k in range(((N-1)//(i+1))-2):
                dfnp[i].insert(j+a,"-0")
                a+=1

for i in range(len(dfnp)):
    dfnp[i][i]=str(dfnp[i][i])+"_*"


df=pd.DataFrame(dfnp)


df=df.style.applymap(negmapdig)
df=df.render()
df=df.replace("\n","")
df=df.replace("-9223372036854775808","*")
display.HTML(df)


with open("cl2_"+str(N)+".html","w") as f:
    #f.write(df)
    pass

df=np.array(df,dtype=object)
# for i in range(len(df)):
#     if(df[i]%2==0 or df[i]%3==0 or df[i]%5==0):
#         df[i]=''
df=np.reshape(df,(-1,n))
df=df.tolist()
# for i in range(len(df)):
#     for j in range(len(df[i])):
#         if j%7==0:
#             df[i][j-1]='     '
df=np.array(df)

for k in range(1,((n-1)//2)+1):
    print("k=",k,end=" : ")
    a=n-k*((n-1)//k)
    i=0
    l1=k
    while(i<a):
        l1+=k-a*(l1//a)
        i+=1
        print(l1,end=", ")
    print("")

x=[] #lj
y=[] #k

for k in range(1,((n-1)//2)+1):
    print("k=",k)
    y.append(k)
    a=n-k*((n-1)//k)
    i=0
    l1=k
    xt=[]
    while(i<a+1):
        print(l1," #",end=" ")
        xt.append(l1)
        for c in range(1,(l1//a) + 1):
            lj=l1-c*a
            print(lj,end=", ")
            xt.append(lj)
        l1+=k-a*(l1//a)
        i+=1
        lj=l1
    x.append(xt)
    print("\n")

x2=[]
for i in range(len(x)):
    for j in range(len(x[i])):
        if(j==i):
            x2.append(x[i][j])

x = np.array([2,4,5,6,9,10,11,12,13,14,16,18,19,20,23,25,27,28,29,31,32,33,34,37,39,40,41,45,46,48,49,50])
y = np.array([1,1,1,3,4,1,4,8,8,9,4,5,11,1,17,1,24,19,24,25,25,4,17,25,33,14,1,9,26,25,9,1])

# calculate natural cubic spline polynomials
cs = CubicSpline(x,y,bc_type='natural')

xs = np.arange(-0.5, 9.6, 0.1)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, cs(xs), label="S")
ax.set_xlim(-0.5, 9.5)
plt.show()