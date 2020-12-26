import pandas as pd
import numpy as np
import datetime as dt
import random
import csv
import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
mpl.font_manager._rebuild()
#mpl.rcParameters['font.family'] = 'IPAexGothic'





def mean_unmatch(path, K,p,method):
    plt.style.use('ggplot')
    #font = {'family': 'meiryo'}
    #mpl.rc('font', **font)

    df = pd.read_csv(path, sep=",", header=None)
    df_boollist = []
    df_meanlist = []


    for i in range(K):
        mean = df.mean(axis='columns', skipna=True).copy()
        df_meanlist.append([method,p,mean[4]])
        df_bool = (df.iloc[5 * i + 3, :] == 0)
        df_boollist.append([method,p,df_bool.sum()])


    return df_boollist,df_meanlist


def makepath_H(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/10-" + str(a) +"-" + str(b) + "DA-H.txt"
  
  return path

def makepath_H_univ(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/10-" + str(a) +"-" + str(b) + "DA-H_univ.txt"
  
  return path

def makepath_S(a,b):
  a = round(a, 1)
  b = round(b, 2)
  
  path = "/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/10-" + str(a) +"-" + str(b) + "DA-S.txt"
  return path

def makepath_S_univ(a,b):

  a = round(a, 1)
  b = round(b, 2)
  
  path = "/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/10-" + str(a) +"-" + str(b) + "DA-S_univ.txt"
  return path

unmatch_H = []
unmatch_S  = []
tmean_H= []
tmean_S = []
DF_list = [unmatch_H,unmatch_S,tmean_H,tmean_S]

for i in range(11):
  path = makepath_H(0.0 + i*0.1,0.5 + i*0.05)
  a , b = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"H")
  unmatch_H.append(a)
  tmean_H.append(b)

print(unmatch_H)


for i in range(11):
  path = makepath_S(0.0 + i*0.1,0.5 + i*0.05)
  a , b = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"S")
  unmatch_S.append(a)
  tmean_S.append(b)


unmatch_H= list(itertools.chain.from_iterable(unmatch_H))
tmean_H= list(itertools.chain.from_iterable(tmean_H))
unmatch_S = list(itertools.chain.from_iterable(unmatch_S))
tmean_S = list(itertools.chain.from_iterable(tmean_S))

df_unmatch_H= pd.DataFrame(unmatch_H,columns=['meathod', 'prob', 'num'])
df_tmean_H= pd.DataFrame(tmean_H,columns=['meathod', 'prob', 'num'])
df_unmatch_S = pd.DataFrame(unmatch_S,columns=['meathod', 'prob', 'num'])
df_tmean_S = pd.DataFrame(tmean_S,columns=['meathod', 'prob', 'num'])



sns.regplot(x=df_tmean_H['prob'], y=df_tmean_H['num'])
sns.regplot(x=df_unmatch_H['prob'], y=df_unmatch_H['num'])

plt.title("Hard方式", fontname="IPAexGothic")
# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("留年者数/内定志望順位平均", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)

plt.savefig('Hard_UT.pdf')
plt.close()

sns.regplot(x=df_tmean_S['prob'], y=df_tmean_S['num'])
sns.regplot(x=df_unmatch_S['prob'], y=df_unmatch_S['num'])
plt.title("Soft方式", fontname="IPAexGothic")
# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("留年者数/内定志望順位平均", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)


plt.savefig('Soft_UT.pdf')
plt.close()

sns.regplot(x=df_tmean_H['prob'], y=df_tmean_H['num'])
sns.regplot(x=df_tmean_S['prob'], y=df_tmean_S['num'])


plt.title("Hard-Soft内定志望順位平均", fontname="IPAexGothic")
# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("内定志望順位平均", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)

plt.savefig('HS-mean.pdf')
plt.close()

sns.regplot(x=df_unmatch_H['prob'], y=df_unmatch_H['num'])
sns.regplot(x=df_unmatch_S['prob'], y=df_unmatch_S['num'])

plt.title("Hard-Soft留年者数", fontname="IPAexGothic")
# x方向のラベル
plt.xlabel("指定科類枠志望率", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("留年者数", fontname="IPAexGothic")
# グラフの表示範囲(x方向)
plt.xlim(-0.1, 1.1)
plt.savefig('HS-unmatch.pdf')
plt.close()


