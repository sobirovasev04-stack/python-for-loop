n = int(input('n: '))

yigindi =0

for son in range(1, n+1):
    if son % 2 == 0:
        yigindi += son

print(f'Juft: {yigindi}')
