# En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
# a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:[20, 50, "Curso", 'Python', 3.14]

lista = [20, 50, "Curso", 'Python', 3.14]
print(lista)

elemento = input("Digite un elemento númerico, letra o palabra: ")

lista[0] = elemento

elemento = input("Digite otro elemento númerico, letra o palabra: ")

lista[1] = elemento

print(lista)
