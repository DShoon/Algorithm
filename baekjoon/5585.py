cash = int(input())
change = 1000 - cash
count = 0

count += change // 500
count += (change % 500) // 100
count += ((change % 500) % 100) // 50
count += (((change % 500) % 100) % 50) // 10
count += ((((change % 500) % 100) % 50) % 10) // 5
count += (((((change % 500) % 100) % 50) % 10) % 5)

print(count)
