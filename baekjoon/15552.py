# for문을 사용할 경우 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간 초과가 날 수 있음
# input 대신 sys.stdin.readLine
# readLine을 사용하면 \n 개행문자까지 함께 입력받으므로 .rstrip()을 해주는게 좋음

import sys

T = int(input()) # Test Case
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)