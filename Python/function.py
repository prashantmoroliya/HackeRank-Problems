def is_leap(year):
    if year >= 1900 and year <= 1000000:
        leap = False

        if year % 4 == 0 and year % 100 != 0:
            return True
        elif year % 100 == 0 and year % 400 == 0:
            return True
        else:
            return leap

year = int(input())
print(is_leap(year))
