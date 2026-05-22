vet = [0] * 5
for i in range(5):
    vet[i] = float(input("Insira: "))
pos_ma = 0
pos_me = 0
for i in range(5):
    if vet[i] > vet[pos_ma]:
        pos_ma = i
    if vet[i] < vet[pos_me]:
        pos_me = i

print(f"Posição do maior valor: {pos_ma}")
print(f"Posição do menor valor: {pos_me}")