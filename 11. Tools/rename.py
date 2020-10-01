import os
src = input("src? ")
dist = input("dist? ")
for i in os.listdir():
    file=i[:-len(src)]
    ctx=i[-len(src):]
    
    if(ctx==src):
        os.rename(i,file+dist)