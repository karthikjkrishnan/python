
import xlsxwriter

workbook = xlsxwriter.Workbook('data7.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

d = [{'name':'karthika', 'age':19, 'salary':2000011},
     {'name':'karthik', 'age':20, 'salary':20000}]
for col,title in enumerate(d[0].keys()):
    worksheet.write(0,col,title)
row = 1
col = 0
for i in d:
    for value in i.values():
        worksheet.write(row,col,value)
        col += 1
    col = 0
    row += 1