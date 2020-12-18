import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake
import dafunc
import dafunc_S


def simulation(cnt, a, b):
    df, df_collist = datamake.make_df(
        '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/csvdata/sinhuri2018.csv'
    )
    n, m, k = datamake.stu_num()
    df_stu = np.zeros((1, n + 1))

    for j in range(cnt):
        random.seed(48 + j)
        student = datamake.make_stu(n, m, k, a, b)
        #print(df_collist)
        univ = datamake.univ_make(df, df_collist)

        for i in range(200):
            dafunc.da(student, univ, df_collist)

        if j == 0:
            df_stu = student[:, 0:5].T.copy()

        else:
            df_stuadd = student[:, 0:5].T.copy()
            df_stu = np.vstack((df_stu, df_stuadd))

    url = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-Q.txt'

    np.savetxt(url, df_stu, delimiter=',', fmt='%d')

    return df_stu


def simulation_s(cnt, a, b):

    n, m, k = datamake.stu_num()
    df_stu = np.zeros((1, n + 1))

    for j in range(cnt):
        random.seed(48 + j)
        df, df_collist = datamake.make_df(
            '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/csvdata/sinhuri2018.csv'
        )
        student = datamake.make_stu(n, m, k, a, b)
        #print(df_collist)
        univ_s = datamake.univ_make_s(df, df_collist)

        for i in range(200):
            dafunc_S.da_s(student, univ_s, df_collist)

        if j == 0:
            df_stu = student[:, 0:5].T.copy()

        else:
            df_stuadd = student[:, 0:5].T.copy()
            df_stu = np.vstack((df_stu, df_stuadd))

    url = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-S.txt'

    np.savetxt(url, df_stu, delimiter=',', fmt='%d')

    return df_stu


#def stu_summary(df_stu):

res0 = simulation_s(1, 0.8, 0.9)

#def do_simulation():

print(res0)
