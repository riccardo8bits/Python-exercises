produto = float(input('Digite o valor do produto: R$'))
print(12*'-')
print('Aplicando desconto de 5%...')
print(12*'-')

desconto = produto- ((produto*5) / 100)

print('O produto de valor R${:.2f} depois do desconto de 5% vai custar R${:.2f}'.format(produto, desconto))