import os

src = input("src? .")
what = input("what? ")
to = input("to? ")

for i in os.listdir():
	ctx=i[-len(src):]
	if(ctx==src):
		with open(i, 'r') as f:
			lines = f.readlines()
		lines = [line.replace(what,to) for line in lines]
		with open(i, 'w') as f:
			f.writelines(lines)