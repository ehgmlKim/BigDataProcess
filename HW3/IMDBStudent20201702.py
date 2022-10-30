#!/usr/bin/python3
import sys
gen = dict()
file = sys.argv[1]
out = sys.argv[2]
with open(file, "rt") as f:
	for line in f:
		str_arr = line.split('::')
		gen_arr = list(map(lambda x:x.strip(), str_arr[2].split('|')))
		for e in gen_arr:
			if e not in gen:
				gen[e] = 1
			else:
				gen[e] += 1
				
				
with open(out, "wt") as fp:
	for key, value in gen.items():
		s = key+" "+str(value)+"\n"
		fp.write(s)
