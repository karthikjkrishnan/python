# Author:karhik J
# Class:ExampleofOpenpyxl
# Purpose:This class used to write the data into the excel file using Openpyxl
# Date:01/04/19
from openpyexcel import Workbook
class ExampleofOpenpyxl:

    def __init__(self):
        print "***********Workbook**********"

    def openpyxl(self):
        wb = Workbook()
        ws = wb.active
        d = [{'name':'pandukittu', 'age':19, 'salary':2000011},
             {'name':'karthik', 'age':20, 'salary':20000}]
        ws.append(d[0].keys())
        print ws['A1']
        for i in range(0,len(d)):
            ws.append(d[i].values())
        wb.save("sample.xlsx")
obj = ExampleofOpenpyxl()
obj.openpyxl()