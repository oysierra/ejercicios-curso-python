# Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, 
# conociendo las notas de: tres prácticas, el examen parcial y el examen final.

prueba_1 = float(input("Ingrese la nota de la primer prueba: ")) # ingresa el valor de la prueba 1
prueba_2 = float(input("Ingrese la nota de la segunda prueba: ")) # ingresa el valor de la prueba 2
prueba_3 = float(input("Ingrese la nota de la tercer prueba: ")) # ingresa el valor de la prueba 3

examen_parcial = float(input("Ingrese la nota del examen parcial: ")) # ingresa el valor del examen parcial
examen_final = float(input("Ingrese la nota del examen final: ")) # ingresa el valor del examen final

promedio_prueba = (prueba_1 + prueba_2 + prueba_3) / 3

promedio_final = (promedio_prueba + (2 * examen_parcial) + (3 * examen_final))/6

print("El promedio de la practica es: ", promedio_prueba , " y el promedio final es: ", promedio_final)

