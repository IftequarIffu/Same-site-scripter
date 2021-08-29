import os,sys
fie=str(sys.argv[0])
f=open("/home/iffu/bountytargets.txt","r")
for i in f:
	t="localhost"+i[1:]
	cmd=f"dig {t}"
	print(os.system(cmd))







