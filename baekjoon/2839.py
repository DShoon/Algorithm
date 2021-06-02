n = int(input())
count = 0


if n > 10:
    if n % 10 == 1:
        n = n - 6
        count += n // 5
        count += 2
    elif n % 10 == 4:
        n = n - 9
        count += n // 5
        count += 3
    elif n % 10 == 7:
        count += n // 5
        count += 4

    elif n % 5 == 0:
        count = n // 5

    elif (n % 5) % 3 == 0:
        count += n // 5
        count += (n % 5) // 3

    elif n % 3 == 0:
        count = n // 3

    else:
        count = -1

else:
    if n % 5 == 0:
        count = n // 5

    elif (n % 5) % 3 == 0:
        count += n // 5
        count += (n % 5) // 3

    elif n % 3 == 0:
        count = n // 3

    else:
        count = -1

print(count)
