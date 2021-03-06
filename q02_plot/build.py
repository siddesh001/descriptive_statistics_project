# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


def plot():
    plt.figure(figsize=(16,10))
    plt.hist(sale_price)
    plt.axvline(np.mean(sale_price),color='Red')
    plt.axvline(np.median(sale_price),color='Yellow')

    (_, idx, counts) = np.unique(sale_price, return_index=True, return_counts=True)
    index = idx[np.argmax(counts)]
    mode = sale_price[index]
    plt.axvline(mode,color='pink')

    plt.show()



