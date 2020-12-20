import pandas as pd
import numpy as np
import random
import csv
import pprint
import datamake
import dafunc
import dafunc_S
import simulation


def run_simulation(N, interval_list, rand):
    K = len(interval_list)
    for i in range(K):
        simulation.simulation(N, interval_list[i][0], interval_list[i][1],
                              rand)


def run_simulation_s(N, interval_list, rand):
    K = len(interval_list)
    for i in range(K):
        simulation.simulation_s(N, interval_list[i][0], interval_list[i][1],
                                rand)


#a =start ,b=finish ,c間隔
def make_interval(a, b, c):
    d = int((b - a) / c)
    inter = []
    for i in range(d):
        inter.append([a + i * c, 1 / 2 + (a + i * c) / 2])

    return inter


interval = make_interval(0.0, 1.0, 0.1)

#run_simulation(10, interval, 100)
run_simulation_s(10, interval, 100)
