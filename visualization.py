import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataSet_Transformation_Lab_02/day02_usage.csv")

busiest = df.max(axis=0)
print(busiest.max())

plt.figure(figsize=(12,5))

plt.plot(df["Day"],df["Study"])
plt.plot(df["Day"],df["Games"])
plt.plot(df["Day"],df["Video"])
plt.plot(df["Day"],df["Chat"])

plt.show()
plt.close()

plt.figure(figsize=(12,5))

plt.plot(df["Day"],df["Study"],label="Study",marker="o")
plt.plot(df["Day"],df["Games"],label="Games",marker="s")
plt.plot(df["Day"],df["Video"],label="Video",marker="d")
plt.plot(df["Day"],df["Chat"],label="Chat",marker="p")
plt.title("Visualization of Four Apps")
plt.xlabel("Day")
plt.ylabel("Minutes")


plt.legend()
plt.show()
plt.close()

