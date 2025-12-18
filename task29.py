n = int(input('n: '))
s = int(input(''))
total = 0

for i in range(1, n+1):
    daromad = int(input(f'daromad{i}: '))
    total += daromad

print(total/s)
