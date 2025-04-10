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


def northvan_accidents():
    conn = sqlite3.connect('files.db')
    df = pd.read_sql('select * from northvan', conn)
    conn.close()

    fig, ax = plt.subplots(figsize=(50, 50))
    ax.scatter(x=df['Longitude'], y=df['Latitude'], s=30, color='xkcd:nice blue')
    ax.scatter(x=df['Longitude'], y=df['Latitude'], s=30, color='xkcd:mango', alpha=0.2)
    ax.set_aspect('equal')
    ax.set_facecolor('xkcd:light grey')

    plt.savefig('northvan.png')


NVpop = 146288
NVprice = 910690.30

def predict_NV():
    conn = sqlite3.connect('files.db')
    df = pd.read_sql('SELECT Municipality, Year, SUM(CrashCount) FROM northvan GROUP BY Year', conn)
    conn.close()
    df.loc[5] = [df['Municipality'][0], 'Total', sum(df['SUM(CrashCount)'])]
    return df



from scipy.stats import poisson

def goodness_of_fit(people):
    conn = sqlite3.connect('files.db')
    accidents = conn.execute('SELECT SUM(CrashCount) FROM northvan').fetchall()[0][0]
    conn.close()
    
    lambda_0 = (people * accidents) / NVpop
    expected = lambda_0 * 6
    x = 2

    p_lower = 1 - poisson.cdf(x - 1, expected)
    p_upper = poisson.cdf(x, expected)

    p_actual = min(p_lower, p_upper) * 2
    return -1 * p_actual

from scipy.optimize import minimize

def num_people():
    res = minimize(goodness_of_fit, x0=1)
    print(f"Number of People Involved: {res.x[0]} \nTwo Tailed P-value: {-0.5 * goodness_of_fit(res.x[0])}")
    return res.x[0]

def plot_poisson():
    xs = np.linspace(1, 10, 100)
    ys = [-1 * goodness_of_fit(x) for x in xs]

    fig, ax = plt.subplots()

    ax.plot(xs, ys, color='xkcd:nice blue')
    ax.plot([num_people() for i in range(10)], np.linspace(0, 1.5, 10), color='xkcd:mango')
    ax.set_ylabel('Two-tailed P-value')
    ax.set_xlabel('Number of People per Accident')
    ax.set_ylim(0, 1.3)
    plt.savefig('poisson.png')