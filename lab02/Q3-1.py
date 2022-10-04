#!/usr/bin/python3
for i in range(1,11):
	if i%2!=0:
		for k in range(11, i,-1):
			print(' ', end='')
		for k in range(i*2-1):
			print('*', end='')
		print()

	else:
		for k in range(11, i, -1):
			print(' ', end='')
		for k in range(i):
			print('*', end='')
		print()
