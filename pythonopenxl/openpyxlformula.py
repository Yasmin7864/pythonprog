import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook("..//data//dataformula.xlsx")
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save("..//data//newsheet.xlsx")