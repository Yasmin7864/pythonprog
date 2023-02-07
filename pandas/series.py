import pandas as pd
d={'Team':["India","Austrlia","Pakistan","Srilanka","England"],
   'Rank':[1,2,3,4,5]}
Team=["India","Austrlia","Pakistan","Srilanka","England"]

m=pd.Series(Team,index=['a','b','c','d','e'])
print(m)