#!/usr/bin/python3
sum = 0.0
count = 0

with open("mbox-short.txt", "rt") as fp:
	for line in fp:
		if line.startswith("X-DSPAM-Confidence: "):
			str_arr = line.split()
			sum += float(str_arr[1])
			count += 1
print(sum/count)

