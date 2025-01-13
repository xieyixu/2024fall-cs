from copy import deepcopy
from itertools import product

rmap={0:1,1:0}
matrix=[[0]*8]+[[0,*map(int,input().split()),0]for _ in range(5)]+[[0]*8]
for test in product(range(2),repeat=6):
    matrix_1=deepcopy(matrix)
    triggers=[list(test)]
    for i in range(1,6):
        for j in range(1,7):
            if triggers[i-1][j-1]:
                matrix_1[i][j]=rmap[matrix_1[i][j]]
                matrix_1[i-1][j]=rmap[matrix_1[i-1][j]]
                matrix_1[i+1][j]=rmap[matrix_1[i+1][j]]
                matrix_1[i][j-1]=rmap[matrix_1[i][j-1]]
                matrix_1[i][j+1]=rmap[matrix_1[i][j+1]]
        triggers.append(matrix_1[i][1:7])
    if matrix_1[5][1:7]==[0,0,0,0,0,0]:
        for trigger in triggers[:-1]:
            print(' '.join(map(str,trigger)))