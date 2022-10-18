#!/usr/bin/python3
str = input("숫자 두 개를 입력하세요 : ")
int_arr = list(map(lambda x:int(x), str.split()))
try:
	print(int_arr[0]/int_arr[1])
except ZeroDivisionError:
	print("division by zero")
