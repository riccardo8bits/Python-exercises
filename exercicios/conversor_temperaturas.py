#Fórmula = F=(C×9/5)+32

print('Conversor de celsius para fahrenheit:')

celsius = float(input('Digite a temperatura em Celsius: '))

conversor = (celsius*9/5) + 32

print('A temperatura de {:.1f} em celsius é de {:.1f} fahrenheit '.format(celsius, conversor))