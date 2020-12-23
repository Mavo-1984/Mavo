import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake
import dafunc_H
import dafunc_S


#cnt:シュミレーション の実行回数 a :Aの確率b:Bの確率,rand = seedの決定
def simulation(cnt, a, b, rand):
    df, df_collist = datamake.make_df(
        '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/csvdata/sinhuri2018.csv'
    )
    n, m, k = datamake.stu_num()
    df_stu = np.zeros((1, n + 1))
    df_univ = np.zeros((1, k))

    for j in range(cnt):
        random.seed(rand + j)
        student = datamake.make_stu(n, m, k, a, b)
        #print(df_collist)
        univ = datamake.univ_make(df, df_collist)

        for i in range(300):
            dafunc_H.da_H(student, univ, df_collist)

        df_stuadd = student[:, 0:5].T.copy()
        df_stu = np.vstack((df_stu, df_stuadd))
        naitei_num = []
        point_list = ["指定1点数", "指定2点数", "指定3点数", "指定4点数"]
        for d_list in point_list:
            for p in univ[d_list]:
                stu_num = 0
                for h in p:
                    if 10 < h < 999:
                        stu_num += 1
                naitei_num.append(stu_num)

        naitei = np.array(naitei_num).reshape((4, k))
        df_univ = np.vstack((df_univ, naitei))
        naitei_sum = np.sum(naitei, axis=0)
        df_univ = np.vstack((df_univ, naitei_sum))

    url = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-H.txt'

    np.savetxt(url, df_stu, delimiter=',', fmt='%d')

    url_univ = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-H_univ.txt'

    np.savetxt(url_univ, df_univ, delimiter=',', fmt='%d')

    return df_stu


#cnt:シュミレーション の実行回数 a :Aの確率b:Bの確率,rand = seedの決定
def simulation_s(cnt, a, b, rand):

    n, m, k = datamake.stu_num()
    df_stu = np.zeros((1, n + 1))
    df_univ = np.zeros((1, k))

    for j in range(cnt):
        random.seed(rand + j)
        df, df_collist = datamake.make_df(
            '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/csvdata/sinhuri2018.csv'
        )
        student = datamake.make_stu(n, m, k, a, b)
        #print(df_collist)
        univ_s = datamake.univ_make_s(df, df_collist)

        for i in range(200):
            dafunc_S.da_s(student, univ_s, df_collist)

        df_stuadd = student[:, 0:5].T.copy()
        df_stu = np.vstack((df_stu, df_stuadd))

        naitei_num = []
        point_list = ["指定1点数", "指定2点数", "指定3点数", "指定4点数"]
        for d_list in point_list:
            for p in univ_s[d_list]:
                stu_num = 0
                for h in p:
                    if 10 < h < 999:
                        stu_num += 1
                naitei_num.append(stu_num)

        naitei = np.array(naitei_num).reshape((4, k))

        df_univ = np.vstack((df_univ, naitei))
        naitei_sum = np.sum(naitei, axis=0)
        df_univ = np.vstack((df_univ, naitei_sum))

    url = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-S.txt'

    np.savetxt(url, df_stu, delimiter=',', fmt='%d')

    url_univ = '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/Result/' + str(
        cnt) + "-" + str(a) + "-" + str(b) + 'DA-S_univ.txt'

    np.savetxt(url_univ, df_univ, delimiter=',', fmt='%d')

    return df_stu


#def stu_summary(df_stu):

res0 = simulation_s(10, 0.8, 0.9, 100)
#res0 = simulation(1, 0.8, 0.9, 100)

#def do_simulation():

print("HI")
