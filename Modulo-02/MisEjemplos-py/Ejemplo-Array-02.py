import array
aNumber = array.array('i')

for i in range(1, 4): # from 1 to 3
    number = int(input("Enter a number: "))
    aNumber.append(number)

print("")

for i in range(3): # from 0 to 2
    print(f"Indice {i} - Valor {aNumber[i]}")

print("")

for n in aNumber: 
    print(f"Vaor {n}")

print("")

for i in range(len(aNumber)): # from 0 to 2
    print(f"Indice {i} - Valor {aNumber[i]}")