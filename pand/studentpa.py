import pandas as pd
import numpy as np
df=pd.read_csv("..//data/pandam.csv")
df['Total']=df.iloc[:].sum(axis=1)
df['avg']=df['Total']/5
d=""
df['Rank']=df['avg'].rank()
df['Result']=np.where((df['M1']>=35) & (df['M2']>=35) & (df['M3']>=35) & (df['M4']>=35) & (df['M5']>=35),"pass","Fail")
print(df.sort_values(by=['Rank']))
#print(df)