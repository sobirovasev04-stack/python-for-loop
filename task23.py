narxlar = [305, 500, 615, 250, 770]

yigindi = 0

for narx in narxlar:
    if narx % 5 == 0:
        yigindi += narx

print(yigindi)
