ballar = []

for i in range(10):
    ball = int(input(f"{i+1}-talabaning ballini kiriting: "))
    ballar.append(ball)

umumiy_ball = 0
for ball in ballar:
    umumiy_ball += ball

print("Umumiy ball:", umumiy_ball)
