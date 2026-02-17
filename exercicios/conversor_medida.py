medida = float(input("Digite sua medida em metros para converter em centímetros: "))

conversor_cm = medida * 100
conversor_mm = medida * 1000

print("O valor em centímetros é {:.2f}".format(conversor_cm))
print("O valor em milímetros é {:.2f}".format(conversor_mm))
