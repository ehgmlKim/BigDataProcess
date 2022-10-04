#!/usr/bin/python3
def max(*int_arr):
	max_val = int_arr[0]

	for num in int_arr:
		if max_val < num:
			max_val = num
	return max_val

print(max(1,4,6))
print(max(10,5,87,57,38))
print(max(4,3,2,1))
