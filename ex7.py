vet = [0] * 10
for i in range(10):
    vet[i] = int(input("Insira: "))
maior = vet[0]
count = 0 
for i in range(10):
    if vet[i] > maior:
        maior = vet[i]
        count += 1
print(f"Vetor: {vet}")
print(f"Maior: {maior}")
print(f"posição: {count}")