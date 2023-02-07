from openpyxl import load_workbook
from openpyxl.drawing.image import Image
#Let's use the hello_world  spreadsheet since it has less data
workbook = load_workbook(filename="..//data//dataformula.xlsx")
sheet = workbook.active

logo = Image("..//data//hcllogo.png")
# A bit of resizing to not fill the whole spreadsheet with the logo
logo.height = 150
logo.width = 150
sheet.add_image(logo,"D10")
workbook.save(filename="..//data//hcllogo.xlsx")