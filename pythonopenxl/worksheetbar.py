from openpyxl.chart import BarChart,Reference
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sales_data=[["Product","Online","Sales"],
            [1,34,78],
            [2,45,67],
            [3,54,56],
            [4,56,67],
            [5,67,65],
            [6,78,89],
            [7,90,93]
            ]
for row in sales_data:
    sheet.append(row)

chart=BarChart()
data=Reference(worksheet=sheet,min_row=1,max_row=8,min_col=2,max_col=3)
chart.add_data(data,titles_from_data=True)
sheet.add_chart(chart,"E2")
wb.save("..//data//chart.xlsx")
