produto_preco = float(input('Informe o preço do produto: '))
quantidade_comprada = int(input('Informe a quantidade comprada: '))
preco_total = produto_preco * quantidade_comprada
desconto = produto_preco * 10 / 100
if quantidade_comprada >= 10:
    print(preco_total - (desconto * quantidade_comprada))
else:
    print(f'O preço total sem desconto é: {preco_total}')