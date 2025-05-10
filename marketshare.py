import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('os_combined-ww-monthly-200901-202504.csv')

df['others'] = df["Series 40"] + df["SymbianOS"] + df["Unknown"] + df["Samsung"] + df["BlackBerry OS"] + df["Nokia Unknown"] + df["Sony Ericsson"] + df["Linux"] + df["KaiOS"] + df["bada"] + df["Tizen"] + df["LG"] + df["Playstation"] + df["MeeGo"] + df["Nintendo 3DS"] + df["Other"]
df = df.drop(columns=["Series 40","SymbianOS","Unknown","Samsung","BlackBerry OS","Nokia Unknown","Sony Ericsson","Linux","KaiOS","bada","Tizen","LG","Playstation","MeeGo","Nintendo 3DS","Other"])

print(df)
labels = df.iloc[:, 0]
tickvalues = df.index #// or tickvalues = df.index
print(labels)

plt.style.use('dark_background')

df.plot(y=['Android', 'iOS', 'Windows', 'Firefox OS', 'others'])

plt.xticks(ticks = tickvalues, labels = labels, rotation = 'vertical')
plt.xlabel('Dates')
plt.ylim(0, 80)
plt.show()
plt.savefig("fig1.png")