import pandas as pd
import numpy as np
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        return self.df
    def total_df(self):
        self.df['total']=self.df.iloc[:,2:].sum(axis=1)
        return self.df
    def avg_df(self):
        self.df['avg']=self.df['total']/5
        return self.df
obj = Readcsv()
df=pd.read_csv('..//data/pandam.csv')
print(obj.create_df(df))
print(obj.total_df())
print(obj.avg_df())


