import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")

a = df[["Chat","Video","Study","Games"]].to_numpy()

# It can be done like this
# apps = list(df.columns)

# arr = df[apps].to_numpy()
# print(arr)

print(a)

print(a.shape)

total_per_day = a.sum(axis=1)

print("\nTotal per day")

for i in range(len(total_per_day)):
    print(f"Day {i+1} : {total_per_day[i]}")

total_per_app = a.sum(axis=0)

print("\nTotal per app")
app = np.array(df.columns)

for i in range(len(total_per_app)):
    print(f"{app[i]} : {total_per_app[i]}")

m = (a.argmax(axis=1)+1)
print(m)
winners = app[m]

print(winners)

names,values = np.unique(m,return_counts=True)

for i in range(len(names)):
    print(f"{app[i]} : {values[i]}")

print(f"Max of all values : {a.max()}")