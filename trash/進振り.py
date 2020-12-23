import pandas as pd
import numpy as np
import random
import csv
import pprint

#データフレームのダウンロード
df = pd.read_csv(
    '/Users/masato/Desktop/UTTdata/prog/PyProgramming/sinhuri2018.csv')

# print(df)
df_col = list(df.columns)[4::]
df_collist = []
for i in range(0, 24, 6):
    df_collist.append(df_col[i:i + 6:])

#Seedのセット。

# n:学生数#m:科類の学生数k:学科数

n = 1076
m = [113, 151, 150, 443, 190, 29]
k = 79

# 選好リストの作成の関数

#typeは科類、aは指定科類枠方、Bは同じ文理枠内
pre_l_1a = [1]
pre_l_1b = list(range(2, 21))
pre_l_1c = list(range(21, 79))
pre_l_1 = [pre_l_1a, pre_l_1b, pre_l_1c]

pre_l_2a = [2]
pre_l_2b = [1] + list(range(3, 21))
pre_l_2c = list(range(21, 79))
pre_l_2 = [pre_l_2a, pre_l_2b, pre_l_2c]

pre_l_3a = list(range(3, 18))
pre_l_3b = [1, 2] + list(range(18, 21))
pre_l_3c = list(range(21, 79))
pre_l_3 = [pre_l_3a, pre_l_3b, pre_l_3c]

pre_s_1a = list(range(46, 79))
pre_s_1b = list(range(21, 27)) + list(range(29, 46))
pre_s_1c = list(range(1, 21))
pre_s_1 = [pre_s_1a, pre_s_1b, pre_s_1c]

pre_s_2a = list(range(69, 79)) + list(range(29, 46))
pre_s_2b = list(range(21, 27)) + list(range(46, 69))
pre_s_2c = list(range(1, 21))
pre_s_2 = [pre_s_2a, pre_s_2b, pre_s_2c]

pre_s_3a = [30]
pre_s_3b = [29] + list(range(31, 78))
pre_s_3c = list(range(1, 29))
pre_s_3 = [pre_s_3a, pre_s_3b, pre_s_3c]
pre = [pre_l_1, pre_l_2, pre_l_3, pre_s_1, pre_s_2, pre_s_3]


def make_pre(type, a, b):
    tmp = random.random()
    if tmp < a / 2:
        key = [0, 1, 2]
    elif a / 2 <= tmp < a:
        key = [0, 2, 1]
    elif a <= tmp < (a + b) / 2:
        key = [1, 0, 2]
    elif (a + b) / 2 <= tmp < b:
        key = [1, 2, 0]
    elif b / 2 <= tmp < (1 + b) / 2:
        key = [2, 0, 1]
    elif (1 + b) / 2 <= tmp < 1:
        key = [2, 1, 0]

    pre_result = []
    for i in key:
        random.shuffle(pre[type][i])
        pre_result.extend(pre[type][i])
        #ここバグってる
    while len(pre_result) < 80:
        pre_result.extend([0])

    return pre_result


# 学生のデータの作成。
# # student(0:学生番号,1科類2点数3内定学科4Time5選好)


def make_stu(n, m):
    tmp = 0
    tmp_2 = ["1", "2", "3", "4", "5", "6"]

    student = np.zeros((n + 1, k + 5))
    for i in range(1, n + 1):
        #0には学生番号、2には点数、3には内定学科（最初は-1）を入れる
        student[i][0] = i
        student[i][2] = random.randrange(35, 90, 1)
        student[i][3] = -1
        # make_prefを使う
        student[i][1] = str(tmp_2[tmp])
        pre = make_pre(tmp + 1, 0.9, 0.95)
        for j in range(k - 1):
            student[i][5 + j] = pre[j]

        if m == i:
            tmp += 1

    return student


#student = make_stu(n, m)


# 大学のデータの作成。
# ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
def univ_make(df):
    for j in df_collist:
        df[j[0]] = df[j[0]].astype('str')
        df[j[2]] = df[j[1]]
        df[j[4]] = df[j[1]].apply(lambda x: np.zeros((x)))
        df[j[5]] = df[j[1]].apply(lambda x: np.zeros((x)))

    # ['第二段階指定1科類', '第二段階指定1枠数', '指定1残席', '指定1底点', '指定1点数', '指定1学籍番号']
    return df


univ = univ_make(df)
#print(univ)
# student(0:学生番号,1科類2点数3内定学科4Time5選好)


def da(student, univ):
    for i in range(1, n + 1):
        if student[i][3] == -1:
            point = student[i][2]  # student[i][2]は点数
            t = student[i][4]  # student[i][4]はtimes
            applyn = int(
                student[i][int(5 +
                               t)])  # student[i][5+t]は申し込み学科。applyn は申し込み学科

            for j in df_collist:
                if univ[j[1]].iloc[applyn] == 0:
                    continue  # 申し込み学科に枠がなかったらおわち
                elif (str(int(student[i][1])) in univ[j[0]].iloc[applyn]) and (
                        univ[j[3]].iloc[applyn] <
                        point):  # 申し込み学科に枠があり、そこ点がiより高い場合
                    univ[j[2]].iloc[applyn] -= 1
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


def simulation(m):
    result = []
    for j in range(m):
        random.seed(48 + j)
        student = make_stu(n, m)
        univ = univ_make(df)

        for i in range(150):
            da(student, univ)
            result.append(len(np.where(student[:, 3] == 0)[0]))
    resultnp = np.array(result)
    resultnp.reshape(m, 150)

    return resultnp

    # 未内定の人数の取得


print(simulation(5))
"""


def da(student, univ):
    for i in range(n):

        t = int(student[i][4])

        if student[i][3] == -1 and student[i][5+t] != 0:
            a = np.where(univ[:, 1] == student[i][5+t])
            for l in a[0]:
                if 0 == univ[l][3]:
                    univ[l][3] = student[i][2]
                    univ[l][4] = student[i][0]
                    student[i][4] += 1
                    student[i][3] = univ[l][0]
                    break
                elif student[i][2] < univ[l][3]:
                    continue
                else:
                    student[int(univ[l][4]), 3] = -1
                    univ[l][3] = student[i][2]
                    univ[l][4] = student[i][0]
                    student[i][4] += 1
                    student[i][3] = univ[l][0]
                    break

            else:
                student[i][4] += 1
        elif student[i][3] == -1 and student[i][5+t] == 0:
            student[i][3] = 0


while student.min(axis=0)[3] == -1:
    da(student, univ)
else:
    print(student)
"""
"""
print(student)


for i in range(n):
    student[i][0] = i
    student[i][1] = random.randrange(1, 6, 1)
    student[i][2] = random.randrange(1, 99, 1)
    student[i][3] = -1
    random.shuffle(p)
    for j in range(k-1):
        student[i][5+j] = p[j]

# print(student)
# print(student[0][1])
for i in range(n):
    univ[i][0] = i
    univ[i][1] = i//3 + 1
# print(univ)


def univ_make(df):
    for i in range(k):
        for j in df_collist:
            print(j[2])
                    df[j[1]] = df[j[1]].astype('int64')
        df[j[2]] = df[j[2]].astype('int64')
        df[j[3]] = df[j[3]].astype('int64')
        df[j[4]] = df[j[4]].astype('int64')
        df[j[5]] = df[j[5]].astype('int64')
            df.loc[i, j[2]] = df.loc[i, j[1]]
            df.loc[i, j[4]] = np.zeros((1, df.loc[i, j[1]]))
            df.loc[i, j[5]] = np.zeros((1, df.loc[i, j[1]]))
    return df
    """
"""
# 学科の作成と選好リストの作成
p = list(range(k))
pre_law = [1]
pre_econ = [2]
pre_let = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pre_edu = list(range(13, 18))
pre_med = [18]
pre_medi = [19, 20]
pre_cul = list(range(21, 32))
pre_agr = list(range(32, 46))
pre_tec = list(range(46, 70))
pre_the = list(range(70, 80))
pre_l = list(range(1, 18))
pre_s = list(range(19, 80))
"""
"""


def make_pre(type,a,b):
    random.random()

    random.shuffle(pre_tec)
    random.shuffle(p)
    random.shuffle(pre_l)
    random.shuffle(pre_s)
    if type == 1:
        if random.random() < 0.85:
            pre = pre_law + p[2::] + [0]
        else:
            pre = pre_l + [0] + pre_s
    elif type == 2:
        if random.random() < 0.85:
            pre = pre_econ + pre_law + p[3::] + [0]
        else:
            pre = pre_l + [0] + pre_s
    elif type == 3:
        if random.random() < 0.65:
            pre = pre_l + [0] + pre_s
        else:
            pre = p
    elif type == 4:
        random.shuffle(pre_tec)
        random.shuffle(pre_s)
        if random.random() < 0.85:
            pre = pre_tec + [0] + pre_s + pre_l
        else:
            pre = pre_s + [0] + pre_l
    elif type == 5:
        random.shuffle(pre_s)
        if random.random() < 0.85:
            pre = pre_s + [0] + pre_l
        else:
            pre = pre_s + pre_l + [0]
    elif type == 6:
        random.shuffle(pre_s)
        if random.random() < 0.8:
            pre = pre_medi + pre_med + pre_tec + + \
                pre_agr + pre_the + pre_cul + pre_l + [0]
        else:
            pre = pre_s + [0] + pre_l
    return pre

"""
