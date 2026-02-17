print("Pintando parede...")

largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))

area = largura*altura

print("Sua parede tem a dimensão de {}X{} e sua área é de {}m²".format(largura, altura, area))
print('Para pintar essa parede, você precisara de {:.2f}l de tinta'.format(area / 2))