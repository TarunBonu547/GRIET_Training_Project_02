import pandas as pd
import numpy as np

df = pd.read_csv("DataSet_Transformation_Lab_02/day02_usage.csv")

a = df[["Chat","Video","Study","Games"]].to_numpy()

# It can be done like this
# apps = list(df.columns)

# arr = df[apps].to_numpy()
# print(arr)


print(a.shape)

total_per_day = a.sum(axis=1)

print("\nTotal per day")

for i in range(len(total_per_day)):
    print(f"Day {i+1} : {total_per_day[i]}")

total_per_app = a.sum(axis=0)

print("\nTotal per app")
app = np.array(df.columns) #Here days are also adding so we should do "+1".....

for i in range(len(total_per_app)):
    print(f"{app[i]} : {total_per_app[i]}")

m = (a.argmax(axis=1)+1)
winners = app[m]

print(winners)

names,values = np.unique(winners,return_counts=True)

print(dict(zip(names,values.tolist())))

print(f"Max of all values : {a.max()}")

shares = (a/total_per_day[:,None])*100
print(np.round(shares,2))

a = df["Day"].to_numpy()

mask = (a%6 == 0) | (a%7 == 0)

print(mask)

print(~mask)

busy = total_per_day.argmax()

print(f"Busiest Day : {busy}")

print(f"Minutes held : {total_per_day[busy]}")