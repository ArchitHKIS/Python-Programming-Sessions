stuff = [1, 2, 3, 4, 5, 5]
wrong = [3, 9, 10, 90, 400]
print(stuff)
stuff.append(23)
print(stuff)
stuff.insert(3, 7)
print(stuff)
stuff.extend(wrong)
print(stuff)
sum = 0
for x in stuff:
    sum += x
print(sum)
list = ["larry", "curly", "moe"]
if "curly" in list:
    print("yay")

sum1 = 0
lista = []
for x in range(1,201):
    if x % 3 == 0:
        lista.append(x)
        sum1 += x
    elif x % 4 == 0:
        lista.append(x)
        sum1 += x
print(lista, " sum: ", sum1)
