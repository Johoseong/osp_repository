#!/usr/bin/python
n = int(input("How many numbers will you enter? : "))
mysum = 0
for i in range(n):
	x = int(input())
	mysum = x + mysum
average = mysum / n
print(average)
