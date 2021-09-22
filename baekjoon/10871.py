# [1, 2, 3, 4, 5] X 

import sys

N, X = map(int, input().split())

arr = sys.stdin.readline().rstrip().split()

for i in arr:
    if int(i) < X:
        print(i, end=' ')
