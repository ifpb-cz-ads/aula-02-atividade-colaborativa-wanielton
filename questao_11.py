# Questão 11:

preco = float(input('Informe o preço total:'))
desconto = float(input('Informe o desconto:'))

val_desconto = preco * desconto / 100
novo_preco = preco - val_desconto

print ('O valor do desconto é:', val_desconto)
print('E o valor total com o desconto é:', novo_preco)
