# 두 정수 A와 B를 입력받고, A+B를 출력 (while문) 
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)