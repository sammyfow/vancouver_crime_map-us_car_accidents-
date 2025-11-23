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

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('willingtopay.png')
"""
#how much people who are somwhat or much more likely to keep phone longer are willing to pay
"""
labels = ['Would pay 10-25%', 'Would pay 25-50%', 'Less than 10%']
sizes = [15/27, 3/27, 9/27]
colors = ['xkcd:muted blue', 'xkcd:bluey green', 'xkcd:dull purple']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('likelywillingtopay.png')
"""
#how much more likely people who have not heard of R2R to keep phone longer
"""
labels = ['Somewhat more likely', 'Much more likely', 'No difference', 'I already keep my devices for a long time']
sizes = [6/29, 14/29, 5/29, 4/29]
colors = ['xkcd:muted blue', 'xkcd:bluey green', 'xkcd:reddish orange', 'xkcd:dull purple']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('notaware.png')
"""
#how much more likely people who have heard of R2R to keep phone longer
"""
labels = ['Somewhat more likely', 'Much more likely']
sizes = [1/7, 6/7]
colors = ['xkcd:muted blue', 'xkcd:bluey green']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('areaware.png')
"""
#how long people who wouldn't keep their phone longer keep their phone
"""
labels = ['Every 2 years', 'Every 3-4 years', 'Every year', 'Only when it stops working']
sizes = [2/9, 1/9, 1/9, 5/9]
colors = ['xkcd:dull purple', 'xkcd:muted blue', 'xkcd:reddish orange', 'xkcd:bluey green']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('agevlike.png')
"""
#how long people who would keep their phone longer keep their phone

labels = ['Every 2 years', 'Every 3-4 years', 'Only when it stops working']
sizes = [1/27, 13/27, 13/27]
colors = ['xkcd:dull purple', 'xkcd:muted blue', 'xkcd:bluey green']

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')

plt.savefig('ageandlike.png')