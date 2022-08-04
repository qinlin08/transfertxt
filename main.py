import pandas as pd
df1 = pd.read_csv('data.txt',sep=' ')
df2 = pd.read_csv('new.txt')

print(df2.values[:,0])
df1.values[:,0] = df2.values[:,0]
df1.to_csv('test.txt',sep=' ',index=0,header=0)
print(1)