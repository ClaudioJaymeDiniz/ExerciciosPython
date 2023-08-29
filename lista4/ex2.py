from random import sample
numeros = sample(range(100), 20)
pares = []
impares = []
for x in range (len(numeros)-1):
    if numeros[x] % 2 == 0:
        pares.append(numeros[x])
    else:
        impares.append(numeros[x])

print('Lista')
print(numeros)
print('Pares')
print(pares)
print('Impares')
print(impares)

