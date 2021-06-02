T = int(input())
a = 0
b = 0
c = 0

if T % 10 != 0:
    c = -1

else:
    if T > 300:
        a = T // 300
        b = (T % 300) // 60
        c = ((T % 300) % 60) // 10
    elif T > 60:
        b = T // 60
        c = (T % 60) // 10
    elif T > 10:
        c = T // 10
if c == -1:
    print(c)
else:
    print(f"{a} {b} {c}")
