
N = int(input("N sonini kiriting: "))

juft_yigindi = 0
toq_yigindi = 0

for son in range(1, N+1):
    if son % 2 == 0:     
        juft_yigindi += son
    else:     
        toq_yigindi += son

print(f"Juft: {juft_yigindi}, Toq: {toq_yigindi}")
