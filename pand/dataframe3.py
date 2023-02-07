import pandas as pd
d={'Team':["India","Australia","pakistan","srilanka","england"],
   'Rank':[1,2,3,4,5],
   'Winper':['60%','70%','80%','90%','50%']
   }
df=pd.DataFrame(d)
df.rename(columns={'Rank':'Ranking'},inplace=True)
print(df)
#df.drop(['Winper'],axis=1,inplace=True)
#print(df.isna().any())
#print(df.isna().sum())