import pandas as pd
import numpy as np
import datetime as dt
import random
import csv
import pprint
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
from google.colab import files

def analyze(path, K,p,method):
    plt.style.use('ggplot')
    font = {'family': 'meiryo'}
    matplotlib.rc('font', **font)

    df = pd.read_csv(path, sep=",", header=None)
    df_boollist = []
    df_meanlist = []


    for i in range(K):
        mean = df.mean(axis='columns', skipna=True).copy()
        df_meanlist.append([method,p,mean[4]])
        df_bool = (df.iloc[5 * i + 3, 1::] == 0)
        df_boollist.append([method,p,df_bool.sum()])
        #print(df_bool.sum())
        #print((df.iloc[5 * K + 4, 1::] == 1).sum())

    return df_boollist,df_meanlist

    #dftest.plot.bar(alpha=0.6, figsize=(12, 3), bins=2, kind='hist')
    #plt.title(u'普通の棒グラフ', size=16)

def makepath_Q(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "/content/drive/MyDrive/便利用/colab/Mavo-master/Result/10-" + str(a) +"-" + str(b) + "DA-Q.txt"
  return path

def makepath_S(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "/content/drive/MyDrive/便利用/colab/Mavo-master/Result/10-" + str(a) +"-" + str(b) + "DA-S.txt"
  return path

unmatch_Q  = []
unmatch_S  = []
tmean_Q = []
tmean_S = []
DF_list = [unmatch_Q,unmatch_S,tmean_Q,tmean_S]
for i in range(10):
  path = makepath_Q(0.0 + i*0.1,0.5 + i*0.05)
  a , b = analyze(
     path,
    10 , round(0.0 + i*0.1,2),"Q")
  unmatch_Q.append(a)
  tmean_Q.append(b)

for i in range(10):
  path = makepath_S(0.0 + i*0.1,0.5 + i*0.05)
  a , b = analyze(
     path,
    10 , round(0.0 + i*0.1,2),"S")
  unmatch_S.append(a)
  tmean_S.append(b)
  unmatch_Q = list(itertools.chain.from_iterable(unmatch_Q))
tmean_Q = list(itertools.chain.from_iterable(tmean_Q))
unmatch_S = list(itertools.chain.from_iterable(unmatch_S))
tmean_S = list(itertools.chain.from_iterable(tmean_S))

df_unmatch_Q = pd.DataFrame(unmatch_Q,columns=['meathod', 'prob', 'num'])
df_tmean_Q = pd.DataFrame(tmean_Q,columns=['meathod', 'prob', 'num'])
df_unmatch_S = pd.DataFrame(unmatch_S,columns=['meathod', 'prob', 'num'])
df_tmean_S = pd.DataFrame(tmean_S,columns=['meathod', 'prob', 'num'])

print(df_unmatch_S)
print(df_unmatch_Q)
"""
sns.regplot(x=df_tmean_Q['prob'], y=df_tmean_Q['num'])
sns.regplot(x=df_unmatch_Q['prob'], y=df_unmatch_Q['num'])
plt.savefig('Hardut.pdf')
files.download("Hardut.pdf")
sns.regplot(x=df_tmean_S['prob'], y=df_tmean_S['num'])
sns.regplot(x=df_unmatch_S['prob'], y=df_unmatch_S['num'])
plt.savefig('Softut.pdf')
files.download("Softut.pdf")
sns.regplot(x=df_tmean_Q['prob'], y=df_tmean_Q['num'])

sns.regplot(x=df_tmean_S['prob'], y=df_tmean_S['num'])
plt.savefig('HS-mean.pdf')
files.download("HS-mean.pdf")
sns.regplot(x=df_unmatch_Q['prob'], y=df_unmatch_Q['num'])

sns.regplot(x=df_unmatch_S['prob'], y=df_unmatch_S['num'])
plt.savefig('HS-unmatch.pdf')
files.download("HS-unmatch.pdf")

"""
