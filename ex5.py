vet = [0] * 10
cnt = 0
for i in range(10):
    vet[i] = int(input("digite: "))
    if vet[i] % 2 == 0:
        cnt += 1 
print(f"O vetor possui {cnt} números pares.")    