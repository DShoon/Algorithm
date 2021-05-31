H, M = input().split()
H = int(H)
M = int(M)
if M >= 45:
    M = M - 45
else:
    M = 60 - (45 - M)
    if H == 0:
        H = 23
    else:
        H = H - 1
print(f"{H} {M}")
