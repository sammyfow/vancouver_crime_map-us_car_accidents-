import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt

def survey2sql():
    conn = sqlite3.connect('files.db')
    df = pd.read_csv('ewastesurvey.csv')
    df.to_sql('survey', conn, if_exists='append')
    conn.close()

labels = ['Much more likely', 'Somewhat more likely']
sizes = [5/6, 1/6]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels)

plt.savefig('areaware.png')