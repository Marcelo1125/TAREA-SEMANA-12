def calcular_descuento(monto_total, porcentaje_descuento=10):
   monto_descuento = monto_total * (porcentaje_descuento /100)
   total_a_pagar = monto_total - monto_descuento
   return monto_descuento, total_a_pagar
# primera llamada solo con el monto total
monto1 =15200
descuento1, total1 =calcular_descuento(monto1)
print(f"compra 1 - monto: ${monto1: .2f}")
print(f"descuento (10%): ${descuento1: .2f}")
print(f"total a pagar: ${total1: .2f}\n")
# segunda llamada: con monto total y porcentaje de descuento
monto2 =25600
porcentaje2 = 15
descuento2, total2 =calcular_descuento(monto2, porcentaje2)
print(f"compra 2 - monto: ${monto2: .2f}")
print(f"descuento ({porcentaje2}%): ${descuento2: .2f}")
print(f"total a pagar: ${total2: .2f}")