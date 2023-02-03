# Errores y Excepciones
while True:
  try: # En el try se ponen los argumentos del código a realizar
    edad = int(input("Ingresa tu edad: "))
    print("Tu edad es: ", edad)
    break # siempre es recomendable en los casos del while usar el break para que no se convierta en un ciclo infinito
  except:
    print("Ingresaste un valor erroneo, debe ser numeros")
  finally:
    print("La ejecución ha terminado")