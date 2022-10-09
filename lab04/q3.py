#!/usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['시트1']

row_id = 1;
for row in ws:
	if row_id != 1:
		sum = ws.cell(row = row_id, column = 3).value
		print(sum)
	row_id += 1

wb.save("student.xlsx")
