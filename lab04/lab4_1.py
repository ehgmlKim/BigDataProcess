#!/usr/bin/python3
file = input()
text=""
try:
	f=open(file, "rt")
	while True:
		row = f.readline()
		if not row: break
		text += row.upper()
	newf=open("output.txt", "wt")
	newf.write(text)
	newf.close()	
	
except FileNotFoundError:
	print("파알이 없습니다.")
finally:
	f.close()
