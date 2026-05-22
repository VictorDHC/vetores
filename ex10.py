vet = [0] * 5
for i in range(5):
    vet[i] = float(input("Insira: "))
maior = vet[0]
menor = vet[0]
som = 0
for v in vet:
    if v > maior:
        maior = v
    if v < menor:
        menor = v
    som += v
media = som / 5
print(f"Valores inseridos: {vet}")
print("Maior: {maior}")
print("Menor: {menor}")
print("Média: {media}")