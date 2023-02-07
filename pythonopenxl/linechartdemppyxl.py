from openpyxl.chart import LineChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[["sno","Year","Sales"],
            [1,2010,1000],
            [2,2011,9000],
            [3,2012,20000],
            [4,2013,25000],
            [5,2014,440000],
            [6,2015,78788],
            ]
for row in sales_data:
    sheet.append(row)

chart=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=6,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..//data//line.xlsx")
