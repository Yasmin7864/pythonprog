from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class People():
    name:str
    num:int
    age:int=0
    #age:int=0
#p=People('yasmin',1,22)
P=[People('Steve',1,23),People('Raju',2,45),People('Rahul',3,78)]
data=[[p.name,p.num,p.age]for p in P]
data=[['Name','Num','Age']]+data
#print(P)
for d in data:
    sheet.append(d)
wb.save("..//data//dtclassdemo.xlsx")