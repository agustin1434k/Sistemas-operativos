stock_inicial = int(input("ingresa el stock inicial: "))
stock_actual = stock_inicial

while stock_actual > 0:
    vendidos = int(input("cantidad vendida: "))
    if vendidos == 0:
        break
    if vendidos <= stock_actual:
       stock_actual -= vendidos
    else:
        print("no hay suficiente. ")

    if stock_actual < stock_inicial * 0.1:
        print("queda menos del 10% del stock.")
print("stock final:", stock_actual)