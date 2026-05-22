vet = [0] * 10
for i in range(10):
    vet[i] = int(input("Insira: "))
maior = vet[0]
men = vet[0]
for i in range(10):
    if vet[i] > maior:
        maior = vet[i]
    if vet[i] < men:
        men = vet[i]
print(f"O maior valor é {maior}, e o menor é {men}.")