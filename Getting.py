import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])


dates = pd.date_range('20200405',periods=13)



df = pd.DataFrame(np.random.randn(13, 4), index=dates, columns=list('ABCD'))


df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20200405'),
    'C':pd.Series(1, index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test','train','test','train']),
    'F':'foo'})

print(df['A'])

print(df[0:3])

print(df['20200405':'20200410'])

print(df.loc[dates[5]])

print(df.loc[:,['A','B']])

print(df.loc['20200405':'20200412',['A','B']])

print(df.loc['20200409',['A','B']])

print(df.loc[dates[5],'A'])

print(df.at[dates[0], 'A'])