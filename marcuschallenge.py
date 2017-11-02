import random
lista = []
x = random.randint(1, 10)
y = 0 + x
while 0 <= x:
    lista.append(random.randint(1,10))
    x = x - 1
print(lista)
lista.sort()
print(lista)