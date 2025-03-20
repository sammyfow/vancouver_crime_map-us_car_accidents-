import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sqlite3
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from scipy import stats

def get_data():
    conn = sqlite3.connect('files.db')

    accidents = pd.read_sql('select count(*), substr(Zipcode, 1, 5) as ZC from `us-accidents` group by ZC', conn)

    housing = pd.read_sql('select avg(price), zip_code from housing group by zip_code', conn)
    housing = housing.rename(columns={'zip_code': 'ZC'})

    population = pd.read_sql('select * from ZCTA', conn)

    conn.close()

    df = accidents.merge(housing, on='ZC')
    df = df.merge(population, on='ZC')
    df = df.drop(columns=['index', 'Geography', 'Unnamed: 3'])

    df['logprice'] = np.log(df['avg(price)'])
    df['logcount'] = np.log(df['count(*)'])
    return df

def get_lin_regression(params):
    df = get_data()

    model = LinearRegression()
    model.fit(df[[params[0]]], df[params[1]])
    score = model.score(df[[params[0]]], df[params[1]])
    pc, pv = stats.pearsonr(df[params[0]], df[params[1]])

    print(f'Coefficient of determination: {score}\nPearson coefficient: {pc}\nP value: {pv}\nEquation: y = ({model.coef_[0]})x + ({model.intercept_})')

    