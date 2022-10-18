

import pandas as pd
data = pd.read_csv("C:/Users/saite/Downloads/data.csv")
data.head()
data.describe()
data = data.fillna(data.mean())
print(data[['Maxpulse','Calories']].agg(['min','max','mean','count']))
print(data[(data.Calories < 1000) & (data.Calories > 500)])
print(data[(data.Calories>500) & (data.Pulse < 100)])
df_modified = pd.DataFrame(data, columns = ['Duration', 'Pulse', 'Calories'])
print(df_modified.head())
del data['Maxpulse']
print(data.head())
data['Calories'] = data['Calories'].astype("int")
print(data['Calories'].dtypes)
data.plot.scatter(x = 'Duration', y= 'Calories')