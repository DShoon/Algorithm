year = int(input())
leap_year = (year % 4 == 0 and year % 100 != 0) or (
    year % 4 == 0 and year % 400 == 0)
print(int(leap_year))
