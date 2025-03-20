import pandas as pd
import sqlite3
import numpy as np

R = 6378

def housing_to_sql():
    chunks = pd.read_csv('realtor-data.zip.csv', dtype={'zip_code': 'str'}, chunksize=10000)
    conn = sqlite3.connect('files.db')
    for df in chunks:
        cleaned = df.dropna(subset=['zip_code'])
        cleaned.to_sql('housing', conn, if_exists='append')
    conn.close()

def us_accidents_to_sql():
    chunks = pd.read_csv('US_Accidents_March23.csv', chunksize=100000)
    conn = sqlite3.connect('files.db')
    for df in chunks:
        df = df.rename(columns={'Start_Lat': 'lat', 'Start_Lng': 'lon'})
        df['lat'] = np.deg2rad(df['lat'])
        df['lon'] = np.deg2rad(df['lon'])
        df['x'] = R * df['lon']
        df['y'] = R * np.log(np.tan((np.pi / 4) + (df['lat'] / 2)))
        df.dropna(subset=['x', 'y'])
        df.to_sql('us-accidents', conn, if_exists='append')
    conn.close()

def ZC_to_sql():
    conn = sqlite3.connect('files.db')
    df = pd.read_csv('ZCTA.csv', skiprows=1)
    df['ZC'] = df['Geographic Area Name'].str.extract(r'(\d{5})')
    df = df.rename(columns={' !!Total': 'population'})
    df = df.drop(columns=['Geographic Area Name'])
    df.to_sql('ZCTA', conn, if_exists='append')
    conn.close()