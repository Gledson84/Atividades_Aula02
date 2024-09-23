usuario = input('Digite seu usuário: ').lower()
senha = input('digite sua senha: ')
if usuario == 'admin' and senha == '1234':
    print('Login efetuado com sucesso!')
elif usuario == 'admin' and 'senha' != '1234':
    print('Senha Incorreta!')
elif usuario != 'admin' and senha == '1234':
    print('Usuário inválido')
else:
    print('Usuário e Senha incorretos!')