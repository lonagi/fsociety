import os
src = input("src? .")
lines = int(input("lines? "))
for i in os.listdir():
    ctx=i[-len(src):]
    if(ctx==src):
    	with open(i,"r") as f:
    		a=f.read().splitlines(True)
    	with open(i,"w") as fout:
    		fout.writelines(a[lines:])