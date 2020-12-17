import pandas as pd
import numpy as np
import random
import csv
import pprint

#データフレームのダウンロード
df = pd.read_csv(
    '/Users/masato/Desktop/UTTdata/prog/PyProgramming/shinhuri4.csv')

# print(df)
df_col = list(df.columns)[4::]
df_collist = []
for i in range(0, 24, 6):
    df_collist.append(df_col[i:i + 6:])

#Seedのセット。
random.seed(48)
# n:学生数#m:科類の学生数k:学科数
n = 800
m = [100, 120, 150, 300, 110, 20]
k = 80

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

# 選好リストの作成の関数


def make_pre(type):
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
        pre = make_pre(tmp + 1)
        for j in range(k - 1):
            student[i][5 + j] = pre[j]

        if m[tmp] == i:
            tmp += 1

    return student


student = make_stu(n, m)


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
# student(0:学生番号,1科類2点数3内定学科4Time5選好)


def da(student, univ):
    for i in range(1, n + 1):
        if student[i][3] == -1:
            point = student[i][2]
            t = student[i][4]  # student[i][4]はtimes
            applyn = int(student[i][int(5 + t)])  # student[i][5+t]は申し込み学科

            for j in df_collist:
                if univ[j[1]].iloc[applyn] == 0:
                    break
                elif (str(int(student[i][1])) in univ[j[0]].iloc[applyn]) and (
                        univ[j[3]].iloc[applyn] < point):
                    univ[j[2]].iloc[applyn] -= 1
                    student[i][3] = applyn
                    # print(univ[j[4]].iloc[applyn])
                    change_point = np.argmin(univ[j[4]].iloc[applyn])

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


result = []
for i in range(300):
    da(student, univ)
    result.append(len(np.where(student[:, 3] == -1)[0]))
    # 未内定の人数の取得
print(result)
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
