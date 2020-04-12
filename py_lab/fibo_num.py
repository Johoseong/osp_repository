#!/usr/bin/python
n = int(input("fibonacci number? "))
F1 = 1
F2 = 1
if (n==1):
	print(F1)
	print("F1 = 1")
elif (n==2):
	print(F1, F1, sep=", ")
	print("F2 = 1")
else:
	print(F1,F2,sep=", ", end='')
	for i in range(n-2):
		F3 = int(F1 + F2)
		print(",", F3, end = '')
		F1 = F2
		F2 = F3
	print()
	print("F%d = %d"%(n, F3))
