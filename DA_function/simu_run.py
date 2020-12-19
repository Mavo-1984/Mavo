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


run_simulation(1, [[0.95, 0.97]], 100)
