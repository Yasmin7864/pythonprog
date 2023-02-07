import pandas as pd
d={'Team':["India","Australia","pakistan","srilanka","england"],
   'rank':[1,2,3,4,5],
   'Winper':['60%','70%','80%','90%','50%']
   }
df=pd.DataFrame(d)
df.rename(columns={'Rank':'Ranking'},inplace=True)
print(df.iloc [[0,1],:])
print(df.iloc[:3,-1])
print(df)