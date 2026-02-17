salario = float(input('Qual é seu salário: R$'))

print('Parábens, você recebeu um aumento de 15% da empresa')

aumento = salario + ((salario*15) / 100)

print('Seu salário de R${:.2f} depois do aumento ficou de R${:.2f}'.format(salario, aumento))