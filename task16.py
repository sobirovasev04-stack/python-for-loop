son = int(input('son:'))

min_son = son

for i in range(2,8):
    son = int(input(f'son {i}: '))
    if son < min_son:
        min_son= son

print(min_son)

