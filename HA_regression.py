import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
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

def get_multiple_regression(params):
    df = get_data()

    model = LinearRegression()
    model.fit(df[params], df['logcount'])
    score = model.score(df[params], df['logcount'])
    values = model.get_params()

    print(f'Coefficient of determination: {score}\nEquation: ln(count) = ({model.coef_[0]})population + ({model.coef_[1]})ln(price) + ({model.intercept_})')

def plot_prediction():
    df = get_data()

    xs = df[['population', 'logprice']]
    ys = df['logcount']

    model = LinearRegression()
    model.fit(xs, ys)
    ypred = model.predict(xs)

    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    sns.kdeplot(ys, ax=ax1)
    sns.kdeplot(ypred, ax=ax2)

    ax1.set_xlim(-2.0, 12.0)
    ax2.set_xlim(-2.0, 12.0)
    ax2.set_ylabel('')
    ax2.set_xlabel('predicted count')

    plt.savefig('distribution.png')
