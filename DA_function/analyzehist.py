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
    df_histlist = []



    for i in range(K):
        df_hist = df.iloc[5 * i + 4, :] 
        df_histlist.append([method,p,df_hist ])


    return df_histlist


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






hist_H = []
hist_S  = []

DF_list = [hist_H,hist_S]

for i in range(11):
  path = makepath_H(0.0 + i*0.1,0.5 + i*0.05)
  a = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"H")
  hist_H.append(a)





for i in range(11):
  path = makepath_S(0.0 + i*0.1,0.5 + i*0.05)
  a = mean_unmatch(
     path,
    10 , round(0.0 + i*0.1,2),"S")
  hist_S.append(a)

"""
bins = np.linspace(-1, 90, 50)

for i in range(0,11):
    plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    plt.title("Soft内定志望順位", fontname="IPAexGothic")

    plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    plt.ylabel("度数", fontname="IPAexGothic")
    plt.xlim(-1, 85)
    plt.ylim(0,900)

    plt.legend(loc='upper right')
    plt.savefig("S-0" +str(i) + "hist.pdf")

    plt.close()

bins = np.linspace(-1, 90, 50)
for i in range(0,11):
    plt.hist( hist_H[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    plt.title("Hard内定志望順位", fontname="IPAexGothic")

    plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    plt.ylabel("度数", fontname="IPAexGothic")
    plt.xlim(-1, 85)
    plt.ylim(0,900)

    plt.legend(loc='upper right')
    plt.savefig("H-0" +str(i) + "hist.pdf")

    plt.close()

fig, axes = plt.subplots(2, 5, figsize=(20, 8))
bins = np.linspace(-1, 90, 50)

for i in range(0,10):
    #ab = plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    #axes[i//5, i%5].xlim(-1, 85)
    #axes[i//5, i%5].ylim(0,900)
    
    

    axes[i//5, i%5].hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    axes[i//5, i%5].legend(loc='upper right')
    
    #plt.title("Soft内定志望順位", fontname="IPAexGothic")

    #plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    #plt.ylabel("度数", fontname="IPAexGothic")
    

    

plt.savefig("Shist.pdf")

plt.close()



"""


fig, axes = plt.subplots(2, 5, figsize=(20, 8))
bins = np.linspace(-1, 90, 50)

for i in range(0,10):
    #ab = plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))
    #axes[i//5, i%5].xlim(-1, 85)
    #axes[i//5, i%5].ylim(0,900)
    
    

    axes[i//5, i%5].hist( hist_H[i][0][2::], bins, alpha = 0.5, label='H0'+str(i))
    axes[i//5, i%5].legend(loc='upper right')
    
    #plt.title("Soft内定志望順位", fontname="IPAexGothic")

    #plt.xlabel("内定志望順位", fontname="IPAexGothic")
    # y方向のラベル
    #plt.ylabel("度数", fontname="IPAexGothic")
    

    
plt.title("Hard内定志望順位", fontname="IPAexGothic")
plt.savefig("Hhist.pdf")

plt.close()
"""
bins = np.linspace(-1, 90, 50)
for i in range(0,10,3):
    plt.hist( hist_S[i][0][2::], bins, alpha = 0.5, label='S0'+str(i))

plt.title("Soft内定志望順位", fontname="IPAexGothic")

plt.xlabel("内定志望順位", fontname="IPAexGothic")
# y方向のラベル
plt.ylabel("度数", fontname="IPAexGothic")

plt.legend(loc='upper right')
plt.savefig('S-hist.pdf')

plt.show()
plt.close()




b = np.random.normal(2, 4, 900)

bins = np.linspace(-10, 10, 50)

plt.hist(a, bins, alpha = 0.5, label='a')
plt.hist(b, bins, alpha = 0.5, label='b')
plt.legend(loc='upper left')

plt.show()




bins = np.linspace(-10, 10, 50)

plt.hist(a, bins, alpha = 0.5, label='a')
plt.hist(b, bins, alpha = 0.5, label='b')
plt.legend(loc='upper left')

plt.show()


unmatch_H= list(itertools.chain.from_iterable(unmatch_H))

unmatch_S = list(itertools.chain.from_iterable(unmatch_S))


df_unmatch_H= pd.DataFrame(unmatch_H,columns=['meathod', 'prob', 'num'])

df_unmatch_S = pd.DataFrame(unmatch_S,columns=['meathod', 'prob', 'num'])



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


"""
