import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataSet_Transformation_Lab_02/day02_usage.csv")

app = df[["Chat","Video","Games","Study"]]

apps = ["Chat","Video","Games","Study"]

plt.figure(figsize=(12,8))

plt.plot(df["Day"],app,marker="p",markersize=8,label=apps)
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.legend(loc="upper left")
plt.savefig("DataSet_Transformation_Lab_02/Visuals/chart_upgrade_without_panel.png",dpi=500)
plt.show()

plt.close()

fig, (ax1,ax2) = plt.subplots(2, 1, figsize=(12, 8))
ax1.plot(df["Day"],app,marker="p",markersize=8,label=apps)
ax1.legend()

plt.tight_layout()
plt.savefig("DataSet_Transformation_Lab_02/Visuals/chart_upgrade_with_panel.png",dpi=500)
plt.show()