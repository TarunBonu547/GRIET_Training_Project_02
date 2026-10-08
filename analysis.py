import pandas as pd
import numpy as np

df = pd.read_csv("day02_usage.csv")

chat = df["Chat"].to_numpy()
video = df["Video"].to_numpy()
study = df["Study"].to_numpy()
games = df["Games"].to_numpy()

b,c,d,e = chat.sum(),video.sum(),study.sum(),games.sum()

print(f"Chat : {b}\nVideo : {c}\nStudy : {d}\nGames : {e}\n")

print(f"Chat : {round(chat.mean(),1)}\nVideo : {round(video.mean(),1)}\nStudy : {round(study.mean(),1)}\nGames : {round(games.mean(),1)}\n")

c = study - games

print(f"Indices of Best Value : {int(c.argmax())+1}\nWorst Value : {int(c.argmin())+1}\n")

# D1. Which app won each day?

# You need thirty answers, one per day. Your arrays are stored per app, so you will have to walk through positions with an index, rebuild each day's four values by hand, find the largest of the four, and translate that position back into an app name.

# Write it. Do not shortcut it. Count the lines when you are done.

apps = ["Chat","Video","Study","Games"]
win = []

for i in range(len(chat)):
    daily = np.array([
        chat[i],video[i],study[i],games[i]
    ])

    position = np.argmax(daily)
    app = apps[position]
    print(f"D{i+1} : {app}")
    # best = 0

    # for j in range(1,4):
    #     if daily[j] > daily[best]:
    #         best = j
    # win.append(apps[best])

    # print(f"D{i+1} : {win[i]}")
    

# D2. What share of each day did each app take?

# Add the four arrays together to get each day's total. Then divide each app's array by that day total and multiply by 100.

# Write all four lines. Then answer one question honestly: if we added a fifth app tomorrow, how many of your lines change?

total = chat + video + games + study

b1,c1,d1,e1 = ((b/total)*100,(c/total)*100,(d/total)*100,(e/total)*100)


for i in range(len(chat)):
    print(f"Day {i+1} Share :")
    print(f"Chat : {round(b1[i],2)}\nVideo : {round(c1[i],2)}\nGames : {round(d1[i],2)}\nStudy : {round(e1[i],2)}\n")