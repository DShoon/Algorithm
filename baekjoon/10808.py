# N 개의 숫자를 입력받고 최소, 최대 출력하기

import sys


N = int(input())
arr = []

arr = sys.stdin.readline().split()
arr = [ int(i) for i in arr ]
print(min(arr), max(arr))