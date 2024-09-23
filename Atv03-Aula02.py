# idade = int(input('Digite sua idade: '))
# cnh = input('Você é habilitado? (Sim ou Não): ').lower()
# if idade >= 18 and cnh == 'sim':
#    print('Você possui maior idade e é habilitado')
# elif idade >= 18 and cnh == 'não':
#     print('Você possui maior idade, mas não é habilitado')
# elif idade < 18 and cnh == 'sim':
#     print('Você possui menor idade e portanto não pode ser habilitado')
# else:
#     print('Você possui menor idade e não é habilitado ')

idade = int(input('Digite sua idade: '))
cnh = input('Você é habilitado? (Sim ou Não): ').lower()

print(idade >= 18 and cnh == 'sim')
    