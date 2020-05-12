import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])

print(s)

dates = pd.date_range('20200405',periods=13)

print(dates)

df = pd.DataFrame(np.random.randn(13, 4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20200405'),
    'C':pd.Series(1, index=list(range(4)),dtype='float32'),
    'D':np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test','train','test','train']),
    'F':'foo'})

print(df2)

print(df2.dtypes)

print(df.head())

print(df.tail(3))

print(df.index)
print(df.columns)

print(df.to_numpy())

print(df2.to_numpy())

print(df.describe())

print(df.T)

print(df.sort_index(axis=1, ascending=False))

print(df.sort_values(by='B'))