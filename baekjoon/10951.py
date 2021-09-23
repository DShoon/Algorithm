# A와 B를 입력받고 A + B를 출력
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        if a > 0 and b < 10:
            print(a + b)
    except:
        break