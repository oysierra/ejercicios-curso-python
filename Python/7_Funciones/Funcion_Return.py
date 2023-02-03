# return es un valor que envía la función

def entero():
  print("este es un dato entero: ")
  return 10

def decimal():
  print("Este es un dato decimal: ")
  return 90.99

def frase():
  return "Mi nombre es Omar Sierra"

def asignacion():
  return 1 , 2 , 3 , 4 , 5 # Al retornar con las comas, cada valor equivale a una variable diferente

print(entero()) # debe hacerse a través de un print para que muestre el valor retornado
print(decimal()) # debe hacerse a través de un print para que muestre el valor retornado
print(frase())

a , b , c , d , e = asignacion()
print(a , b , c , d , e)