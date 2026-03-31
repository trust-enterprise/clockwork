import pandas as pd
import csv

data = [
    ["name", "age"],
    ["aman", 12],
    ["shrija", 11],
    ["tooba", 24]
]

data2 = {
    "name": ["aman", "shrija", "tooba"],
    "age": [12, 11, 24]
}

df2 = pd.DataFrame(data2)
for index, row in df2.iterrows():
    print(f"\nindex: {index}")
    print(f"name: {row["name"]}")
    print(f"age: {row["age"]}")
    print(f"_____________\n")

print(type(df2["name"]))




# df = pd.DataFrame(data[1:], columns = data[0])
# print(f"Dataframe:\n{df}\n")
# print(f"Statistical Summary:\n{df.describe(include='all')}\n")

with open("temp.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open("temp.csv", "r") as f:
    df = pd.read_csv(f, header=None)
    # print(f"using pd.read_csv:\n{df}")
    # print(f.read())
    
# better way; nos get converted into str
with open("temp.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        pass