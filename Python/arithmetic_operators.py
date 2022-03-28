a = int(input())
b = int(input())

if a >= 1 and a <= 100000000000:
    if b >= 1 and b <= 10000000000:
        print(a + b)
        print(a - b)
        print(a * b)

else:
    print("Value out of range")
