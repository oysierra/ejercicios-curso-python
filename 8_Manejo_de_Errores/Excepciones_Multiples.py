# Excepciones Multiple
while True:
  try:
    num1 = int(input("Digite un numero: "))
    resultado = 100/num1
    print(resultado)
    break
  except ZeroDivisionError: # se usa para indicar que no se puede dividir entre 0
    print("No se puede dividir entre cero")

while True:
  try:
    edad = int(input("Ingresa tu edad: "))
    print("Tu edad es: ", edad)
    break
  except ValueError:
    print("No se puede dividir entre cero")

while True:
  try:
    edad = int(input("Ingresa tu edad: "))
    print("Tu edad es: ", edad)
    break
  except KeyboardInterrupt:
    print("\nHas interrumpido la ejecucion")
    break