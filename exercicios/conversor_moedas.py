valor = float(input("Quanto dinheiro você tem na carteira? R$ "))

conversor = valor / 5.22

print("Com {:.2f} você pode comprar US${:.2f}".format(valor, conversor))