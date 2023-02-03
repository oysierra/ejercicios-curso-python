# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def precio_total_factura():
  factura = float(input("indique el importe sin IVA: "))
  impuesto = float(input("indique el impuesto a aplicar: "))
  total_factura = 0

  if factura > 0:
    if impuesto > 0:
      total_factura = factura + (factura * (impuesto/100))
      return total_factura
    else:
      print("Se calcula con el impuesto del 21% ya que el valor ingresado es menor a 0")
      total_factura = factura + (factura * 0.21)
  else:
    print("La factura no puede ser negativa")

print(precio_total_factura())