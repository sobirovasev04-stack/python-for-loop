son = input("Sonni kiriting: ")

teskari = ""
for i in range(len(son)-1, -1, -1):
    teskari += son[i]

print(teskari)
