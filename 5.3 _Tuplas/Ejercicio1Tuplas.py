# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

meses_anio = ("Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre")

numero_mes_anio = int(input("Ingrese el numero del mes del año: "))

if numero_mes_anio >= 1 and numero_mes_anio <= 12:
    numero_mes_anio -= 1
    print(meses_anio[numero_mes_anio])
else:
    print("Numero de mes incorrecto")