import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def survey2sql():
    conn = sqlite3.connect('files.db')
    df = pd.read_csv('ewastesurvey.csv', skiprows=lambda x: (x > 0) & (x < 34))
    df.to_sql('survey', conn, if_exists='append')
    conn.close()

#how much all participants are willing to pay
"""
labels = ['Would pay 10-25%', 'Would pay 25-50%', 'Replace regardless', 'Less than 10%']
sizes = [18/36, 4/36, 3/36, 11/36]
colors = ['xkcd:muted blue', 'xkcd:bluey green', 'xkcd:reddish orange', 'xkcd:dull purple']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('willingtopay.png')
"""
#how much people who are somwhat or much more likely to keep phone longer are willing to pay
"""
labels = ['Would pay 10-25%', 'Would pay 25-50%', 'Less than 10%']
sizes = [15/27, 3/27, 9/27]
colors = ['xkcd:muted blue', 'xkcd:bluey green', 'xkcd:dull purple']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('likelywillingtopay.png')
"""
#how much more likely people who have not heard of R2R to keep phone longer
"""
labels = ['Somewhat more likely', 'Much more likely', 'No difference', 'I already keep my devices for a long time']
sizes = [6/29, 14/29, 5/29, 4/29]
colors = ['xkcd:muted blue', 'xkcd:bluey green', 'xkcd:reddish orange', 'xkcd:dull purple']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('notaware.png')
"""
#how much more likely people who have heard of R2R to keep phone longer
"""
labels = ['Somewhat more likely', 'Much more likely']
sizes = [1/7, 6/7]
colors = ['xkcd:muted blue', 'xkcd:bluey green']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('areaware.png')
"""
#how long people who wouldn't keep their phone longer keep their phone
"""
labels = ['Every 2 years', 'Every 3-4 years', 'Every year', 'Only when it stops working']
sizes = [2/9, 1/9, 1/9, 5/9]
colors = ['xkcd:dull purple', 'xkcd:muted blue', 'xkcd:reddish orange', 'xkcd:bluey green']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('agevlike.png')
"""
#how long people who would keep their phone longer keep their phone
"""
labels = ['Every 2 years', 'Every 3-4 years', 'Only when it stops working']
sizes = [1/27, 13/27, 13/27]
colors = ['xkcd:dull purple', 'xkcd:muted blue', 'xkcd:bluey green']

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color':'w'})

plt.savefig('ageandlike1.png')
"""
conn = sqlite3.connect('files.db')
df = pd.read_sql('SELECT * FROM survey', conn)
conn.close()
factors = df['Which of the following factors would most increase your likelihood of repairing your phone instead of replacing it? (Select up to 2)'].str.split(';', expand=True)
df = df[['factor1', 'factor2']] = factors
#print(df['factor2'].value_counts())
#print(df['factor1'].value_counts())

"""
Guaranteed repair quality: 21
Official spare parts: 10
Same day pickup: 10
Easier access: 6
Lower cost: 19
"""
responses = ['Guaranteed Quality', 'Lower Cost', 'Official Parts', 'Same Day Pick-Up', 'Easier Access']
values = [2100/36, 1900/36, 1000/36, 1000/36, 600/36]

fig, ax = plt.subplots(facecolor=(16/255, 25/255, 44/255, 1.0))

bar = ax.barh(responses, values, color='#38bdf8')

ax.tick_params(axis='y', colors='w')
ax.set_facecolor((16/255, 25/255, 44/255, 1.0))
ax.set_xlim(0, 100)
ax.get_xaxis().set_visible(False)
ax.bar_label(bar, fmt='%1.1f%%', color='w')
for spine in ax.spines.values():
    spine.set_edgecolor('w')

plt.tight_layout()
plt.savefig('responses.png')
