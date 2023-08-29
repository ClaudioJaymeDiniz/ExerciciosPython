from random import sample
numeros = sample(range(100), 10)
min = numeros[0]
max = numeros[0]
for x in range (len(numeros)-1):
    if x < min:
        min = numeros[x]
    if x > max:
        max = numeros[x]
print(numeros)

print(f' {min} é o menor numero')
print(f' {max} é o maior numero')
