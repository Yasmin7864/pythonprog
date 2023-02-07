import pandas as pd
d={'Team':["India","Austrlia","Pakistan","Srilanka","England"],
   'Rank':[1,2,3,4,5]
   }
df=pd.DataFrame(d)
df.rename(columns={'Rank':'Ranking'})
print(df)
