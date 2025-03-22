# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Primera llamada:
monto1 = float(input("Ingrese el monto total de la primera compra: $"))
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

print(f"\nPrimera compra:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")

# Segunda llamada:
monto2 = float(input("\nIngrese el monto total de la segunda compra: $"))
porcentaje2 = float(input("Ingrese el porcentaje de descuento para la segunda compra: "))
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2

print(f"\nSegunda compra:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")
