#!/usr/bin/python3
from datetime import datetime, date
def what_day(date):
	days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
	day = date.weekday()
	return (days[day])

result=dict()
file, out = input().split()
with open(file, "rt") as f:
	for line in f:
		str_arr = list(map(lambda x:x.strip(), line.split(',')))
		date_arr = list(map(lambda x:int(x), str_arr[1].split('/')))
		region_day = str_arr[0]+","+what_day(date(date_arr[2], date_arr[0], date_arr[1]))

		if region_day not in result:
			result[region_day] = [int(str_arr[2]), int(str_arr[3])]
		else:
			result[region_day][0] += int(str_arr[2])
			result[region_day][1] += int(str_arr[3])


with open(out, "wt") as fp:
	for key, value in sorted(result.items()):
		s = key+" "+str(value[0])+","+str(value[1])+"\n"
		fp.write(s)
