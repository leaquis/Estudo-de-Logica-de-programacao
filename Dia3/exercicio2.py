#senhas iguais
#criando um registro de usuario

senha = "12345"
senha_digitada = str(input("Digite sua senha: "))
usuario_bloqueado = False

verificacao_de_senha = senha == senha_digitada

if verificacao_de_senha and not usuario_bloqueado:
    print("Acesso concedido!")
else:
    print("Acesso negado!")

