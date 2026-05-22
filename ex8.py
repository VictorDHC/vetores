vet = [0] * 15
for i in range(15):
    vet[i] = int(input("Insira: "))
soma = 0
for vetor in vet:
    soma += vetor
a = soma / 15
print(a)
