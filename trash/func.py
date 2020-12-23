import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake


#df_collist =[['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号'], ['第二段階指定2科類', '第二段階指定2枠数', '指定2残席', '指定2底点', '指定2点数', '指定2学籍番号'], ['第二段階指定3科類', '第二段階指定3枠数', '指定3残席', '指定3底点', '指定3点数', '指定3学籍番号'], ['第二段階指定4科類', '第二段階指定4科類.1', '指定4残席', '指定4底点', '指定4点数', '指定4学籍番号']]
def da(student, univ, df_collist):
    n, m, k = datamake.stu_num()
    #上から処理を実行
    for i in range(1, n + 1):
        #もし未内定だったら
        if student[i][3] == -1:
            point = student[i][2]  # student[i][2]は点数
            t = student[i][4]  # student[i][4]はtimes
            applyn = int(
                student[i][int(5 +
                               t)])  # student[i][5+t]は申し込み学科。applyn は申し込み学科

            #j = ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
            for j in df_collist:
                if univ[j[1]].iloc[applyn] == 0:
                    continue  # 申し込み学科に枠がなかったらおわち

                elif (str(int(student[i][1])) in univ[j[0]].iloc[applyn]) and (
                        univ[j[3]].iloc[applyn] <
                        point):  # 申し込み学科に枠があり、そこ点がiより高い場合
                    univ[j[2]].iloc[applyn] -= 1
                    #iを仮内定処理
                    student[i][3] = applyn
                    # print(univ[j[4]].iloc[applyn])
                    # 申し込み学科から追い出される学生の処理
                    # change_point:申し込み学科から追い出される学生の学籍番号の場所
                    change_point = np.argmin(univ[j[4]].iloc[applyn])
                    # change_stu:申し込み学科から追い出される学生の学籍番号

                    change_stu = univ[j[5]].iloc[applyn]

                    if change_stu[change_point] != 0 and univ[
                            j[2]].iloc[applyn] == 0:
                        student[change_stu[change_point]][3] = -1
                    univ[j[4]].iloc[applyn][change_point] = student[i][2]
                    univ[j[5]].iloc[applyn][change_point] = student[i][0]
                    univ[j[3]].iloc[applyn] = np.amin(univ[j[4]].iloc[applyn])
                    break

            student[i][4] = t + 1

    return student, univ


def simulation(cnt):
    result = []
    df, df_collist = datamake.make_df(
        '/Users/masato/Desktop/UTTdata/prog/PyProgramming/DA_algorithm/Mavo/sinhuri2018.csv'
    )
    n, m, k = datamake.stu_num()

    for j in range(cnt):
        random.seed(48 + j)
        student = datamake.make_stu(n, m, k)
        print(df_collist)
        univ = datamake.univ_make(df, df_collist)

        for i in range(150):
            da(student, univ, df_collist)
            result.append(len(np.where(student[:, 3] == 0)[0]))

    resultnp = np.array(result)
    resultnp.reshape(cnt, 150)
    print(student[400:600])

    return resultnp


kekka = simulation(3)
print(kekka)
