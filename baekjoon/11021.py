import sys

# for문을 사용해서 입력을 받을경우 input()가 아닌 sys.stdin.readline을 이용하기

T = int(input())
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(f"Case #{i+1}: {x+y}")