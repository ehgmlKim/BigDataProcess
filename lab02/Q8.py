#!/usr/bin/python3
def fib_opt(n, F):
	if n<=2:
		return 1
	else:
		if F[n-1] == 0:
			F[n-1] = fib_opt(n-1,F)

		if F[n-2] == 0:
			F[n-2] = fib_opt(n-2,F)
		return F[n-1] + F[n-2]

n = 36
F = [0 for n in range(n)]

print(fib_opt(5,F))
print(fib_opt(10,F))
print(fib_opt(35,F))
