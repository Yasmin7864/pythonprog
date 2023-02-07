import pandas as pd
exldata1=pd.read_excel("..//data/Book1.xlsx",sheet_name='Sheet2')
print(exldata1)
exldata2=pd.read_excel("..//data/Book1.xlsx",sheet_name="Sheet3")
print(exldata2)
