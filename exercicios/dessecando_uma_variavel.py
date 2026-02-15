algo = input("Digite algo: ")

# Todo valor que está dentro do input se torna string


print("O tipo primitivo desse valor é ", type(algo)) #Type verifica o tipo primitivo desse valor
print("Só tem espaços? ",algo.isspace()) #só tem espaços
print("É um número? ", algo.isnumeric()) #só tem numeros
print("É alfabético? ", algo.isalpha()) # só tem letras
print("É alfanumérico", algo.isalnum()) # tem numeros e texto juntos
print("Está em maiúsculo", algo.isupper()) # Está em maiúscula
print("Está em minúsculo", algo.islower()) # Está em minúsulo
print("Está capitalizada? ", algo.istitle()) # Está em maiúscula e minúscula
