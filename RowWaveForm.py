from os import *
from sys import *
from collections import *
from math import *

def rowWaveForm(mat):
  # OPTIMIZED SOL
    a = []
    for i, j in enumerate(mat):
        if i%2==0:
            a.extend(j)
        else:
            a.extend(j[::-1])
    return a


  # BRUTE FORCE
    # x = len(mat)
    # y = len(mat[0])
    # for i in range(x):
    #     if i%2==0:
    #         for j in range(y):
    #             a.append(mat[i][j])
    #     else:
    #         for j in range(y-1,-1,-1):
    #             a.append(mat[i][j])
    # return a
    # Write your code here.
    pass
