import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#run download_accidents.sh to download accident data

def get_state(state):
    chunks = pd.read_csv('US_Accidents_March23.csv', chunksize=100000)
    collected = []
    for df in chunks:
        locs = df.loc[df['State'] == state, ['Start_Lat', 'Start_Lng', 'Severity']]
        collected.append(locs)
    return pd.concat(collected)

def get_locations():
    chunks = pd.read_csv('US_Accidents_March23.csv', chunksize=100000)
    collected = []
    for df in chunks:
        locs = df[['Start_Lat', 'Start_Lng', 'Severity']]
        collected.append(locs)
    return pd.concat(collected)

def plot_state(state):
    #use the two letter abbreviation in capital letters
    df = get_state(state).rename(columns={'Start_Lat': 'lat', 'Start_Lng': 'lon'})
    df['lat'] = np.deg2rad(df['lat'])
    df['lon'] = np.deg2rad(df['lon'])
    df['x'] = np.cos(df['lat']) * np.cos(df['lon'])
    df['y'] = np.cos(df['lat']) * np.sin(df['lon']) 
    df = df.dropna()
    fig, ax = plt.subplots(figsize=(15, 15)) 
    sns.scatterplot(x=df['x'], y=df['y'], hue=df['Severity'], palette='tab10', s=5, ax=ax)
    ax.set_aspect('equal')
    plt.savefig(f'{state}.png')

def plot_country():
    df = get_locations().rename(columns={'Start_Lat': 'lat', 'Start_Lng': 'lon'})
    df['lat'] = np.deg2rad(df['lat'])
    df['lon'] = np.deg2rad(df['lon'])
    df['x'] = np.cos(df['lat']) * np.cos(df['lon'])
    df['y'] = np.cos(df['lat']) * np.sin(df['lon']) 
    df = df.dropna()
    fig, ax = plt.subplots(figsize=(15, 15)) 
    sns.scatterplot(x=df['x'], y=df['y'], hue=df['Severity'], palette='tab10', s=3, ax=ax)
    ax.set_aspect('equal')
    plt.savefig('accidents.png')