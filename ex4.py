vet = [0] * 8

for i in range(8):
    vet[i] = int(input("digite: "))

print(vet)
a = int(input("posição X: "))
b = int(input("posição Y: "))
c = vet[a] + vet[b]
print(c)