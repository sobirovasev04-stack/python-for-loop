ball = int(input(f'ball 1:'))
max_ball = ball
min_ball = ball

for i in range(2,6):
    ball = int(input(f'ball{i}: '))
    if ball > max_ball:
        max_ball = ball
    if ball < max_ball:
        min_ball = ball

print(f'eng yuqori: {max_ball}, eng pasr: {min_ball}')
