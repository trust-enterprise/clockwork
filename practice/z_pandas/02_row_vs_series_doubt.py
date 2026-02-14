import pandas as pd
import csv

data = {
    "name": ['aman', 'shruti', 'tooba'],
    "age": [12, 15, 23]
}

df = pd.DataFrame(data)
print(df.loc[df["age"] > 12, ["name", "age"]])

# print(df[df['age']>13])
# print(f"\nNAME series: {df["name"]}")
# print(f"\nAGE series: {df["age"]}\n")
# print(df)
# print(df.iloc[0])
# print(df.loc[0,['name', 'age']])
# print(df.iloc[0, 0:2])
# print(df.iloc[[0], 0:2]) #returns in dataframe format