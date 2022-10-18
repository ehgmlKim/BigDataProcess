#!/usr/bin/python3
price = [10000, 8000, 7500, 12000, 25000]

def sale(e):
	return e*0.8

for e in map(sale, price):
	print(e, end=", ")
print("\n")
