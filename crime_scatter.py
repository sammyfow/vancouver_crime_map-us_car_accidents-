#!/home/codespace/.python/current/bin/python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('crime_data.csv')
df = df[df['X'] > 400000.0]
df = df.dropna(subset=['NEIGHBOURHOOD'])
x = df['X']
y = df['Y']
fig, ax = plt.subplots(figsize=(15, 15))
sns.scatterplot(x=x, y=y, hue=df['TYPE'], palette='tab20', s=5, ax=ax, alpha=0.05)
plt.xlim([482500.0, 500000.0])
plt.ylim([5447500.0, 5465000.0])
plt.savefig('crime_scatter.png')