#!/usr/bin/python3
a = [1,2,3,4,5,6,7,8,9,10]

def powf(e):
	return e ** 2
b=[]
for e in map(powf, a):
	b.append(e)

dict={}
for i in range(len(a)):
	dict[a[i]]=b[i]

print(dict[6])

