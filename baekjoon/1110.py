N = int(input())
count = 0
if N < 10:
    x = f'{N}'+'0'
else:
    x = f'{N}'


while True:
    if N < 10 and count == 0:
        a = x[0]
    else:
        a = x[1]
    b = int(x[0]) + int(x[1])
    b = str(b)[-1]
    c = a + b
    count += 1
    if int(c) == int(N):
        break
    else:
        x = c

print(count)

