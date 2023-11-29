import pandas as pd

df = pd.read_csv('python\pandas\cleaning.csv')

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
#df.drop(x,inplace = True) removes lines 


#df.loc[7, 'Duration'] = 45


print(df.to_string())
