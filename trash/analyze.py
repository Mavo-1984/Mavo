import pandas as pd
import numpy as np
import datetime as dt
import random
import csv
import pprint
import datamake
import dafunc_H
import dafunc_S
import simulation
import simu_run
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import itertools


def analyze(path, K):
    #plt.style.use('ggplot')
    #font = {'family': 'meiryo'}
    #matplotlib.rc('font', **font)

    df = pd.read_csv(path, sep=",", header=None)
    for i in range(K):
        mean = df.iloc[:, 1::].mean(axis='columns', skipna=True).copy()
        df_bool = (df.iloc[5 * i + 3, 1::] == 0)
        print(df_bool.sum())
        #print((df.iloc[5 * K + 4, 1::] == 1).sum())

    print(mean)

    #dftest.plot.bar(alpha=0.6, figsize=(12, 3), bins=2, kind='hist')
    #plt.title(u'普通の棒グラフ', size=16)


#analyze(
#    "/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/1-0.95-0.97DA-H.txt",
#    1)

#print("Hallo")
x = np.array([1,2,3,4])
y = np.array([2,3,4,5])

# グラフを描画
plt.plot(x, y)
plt.show()
