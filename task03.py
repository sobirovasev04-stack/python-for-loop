n = int(input('n:'))

if n <= 15:
    for i in  range(n, 16):
        print(i)
else:
    for i in range(15, n -1, -1):
        print(i)
    