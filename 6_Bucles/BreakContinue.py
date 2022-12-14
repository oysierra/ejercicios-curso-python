# Break detiene de inmediato el bucle si se  cumple una determinada condición
for i in range(1 , 11):
    if i == 5:
        break
    print(i)


# Continue omite la condición y continua
for j in range(1 , 11):
    if j == 6:
        continue
    print(j)
