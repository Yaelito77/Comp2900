array = [15, 66, 19, 66, 93, 66, 15]

count_element = 15

counter = 0

for element in array:
    if element == count_element:
        counter += 1

print(f"El elemento {count_element} aparece {counter} veces en el arreglo.")