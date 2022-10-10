#!/usr/bin/python3
import openpyxl

wb = openpyxl.load_workbook("student.xlsx")
ws = wb['Sheet1']

row_id = 1

for row in ws:
	rank=1
	row_id2=1
	if row_id != 1:
		for row in ws:
			if row_id2 != 1:
				a=ws.cell(row = row_id, column=7).value
				b=ws.cell(row = row_id2, column=7).value
				if a < b:
					rank += 1
				ws.cell(row=row_id, column=8).value = rank
			row_id2 += 1
	row_id +=1


row_count=row_id-2
row_id = 1
print(row_count)
print(row_count*0.15)


for row in ws:
	if row_id != 1:
		rank = ws.cell(row=row_id, column=8).value
		if rank <= row_count*0.15:
			print(row_id,"는 A+")
			ws.cell(row=row_id, column=8).value = 'A+'
		elif rank <= row_count*0.3:
			print(row_id,"는 A")
			ws.cell(row=row_id, column=8).value = 'A'
		elif rank <= row_count*0.5:
			print(row_id,"는 B+")
			ws.cell(row=row_id, column=8).value = 'B+'
		elif rank <= row_count*0.7:
			print(row_id,"는 B")
			ws.cell(row=row_id, column=8).value = 'B'
		elif rank <= row_count*0.85:
			print(row_id,"는 C+")
			ws.cell(row=row_id, column=8).value = 'C+'
		else :
			print(row_id,"는 C")
			ws.cell(row=row_id, column=8).value = 'C'
	row_id += 1
			
wb.save("student.xlsx")
