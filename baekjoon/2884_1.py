a, b = map(int, input().split())
x = a*60+b-45
# 음수 연산
print(x//60 % 24, x % 60)
