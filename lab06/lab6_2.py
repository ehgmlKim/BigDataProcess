#!/usr/bin/python3
import time
import datetime
year = 1994
month = 5
day = 5
tm = (year, month, day, 0,0,0,0,0,0)
output = int((time.time() - time.mktime(tm)) / (24*60*60))
print(output,"days")
