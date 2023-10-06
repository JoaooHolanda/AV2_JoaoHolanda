users = {
    "João": {"senha": "12345", "saldo": 1000},
    "Marcos": {"senha": "lambdaehlegal", "saldo": 500},
    "Paulo": {"senha": "maybe", "saldo": 1500},
}

getuser = lambda: input("Qual seu nome? ")
getpassword = lambda: input("Qual sua senha? ")
blocked = lambda: print("Acesso bloqueado. Usuário não existente ou senha inválida")
allowed = lambda: print("Acesso Permitido")
nome = lambda user: user
cond = lambda user, gpassword: user["senha"] == gpassword
Tela = lambda user: print(f"Olá, {nome(user)}! Escolha qual opção você deseja:\n1. Extrato Bancário\n2. Saque Bancário\n3. Depósito Bancário\nDigite 'Sim' para selecionar uma opção ou 'Não' para sair: ")

# Obtenha o nome do usuário uma vez e armazene em uma variável
nome_do_usuario = getuser()

# Obtenha a senha do usuário uma vez e armazene em uma variável
senha_do_usuario = getpassword()

# Faça o login e obtenha o usuário
login = lambda users, guser, gpassword, Tela, blocked, allowed: users.get(guser) if cond(users.get(guser), gpassword) else None

usuario_logado = login(users, nome_do_usuario, senha_do_usuario, Tela, blocked, allowed)

while usuario_logado:
    # Após o login bem-sucedido, obter a escolha do usuário
    opcao = input("Escolha uma opção (1, 2 ou 3) ou deseja sair (digitar sair): ").strip().lower()
    
    if opcao == "1":
        print("Você selecionou Extrato Bancário. Executando ação...")
        print(f"{nome_do_usuario} Você possui: R$ {usuario_logado['saldo']:.2f}")
    elif opcao == "2":
        print("Você selecionou Saque Bancário. Executando ação...")
        valor = float(input("Quanto você deseja Sacar? R$ "))
        # Verifica saldo
        if valor > usuario_logado['saldo']:
            print('Saldo Insuficiente para saque!')
        else:
            usuario_logado['saldo'] -= valor
            print(f"{nome_do_usuario} Valor de R$ {valor:.2f} sacado com sucesso\nSeu novo Extrato é de R$ {usuario_logado['saldo']:.2f}")   
    elif opcao == "3":
        print("Você selecionou Depósito Bancário. Executando ação...")
        valor = float(input("Quanto você deseja Depositar? R$ "))
        if valor <= 0:
            print("Valor de depósito inválido.")
        else:
            usuario_logado['saldo'] += valor
            print(f"{nome_do_usuario} Valor de R$ {valor:.2f} depositado com sucesso\nSeu novo Extrato é de R$ {usuario_logado['saldo']:.2f}")
    elif opcao == "sair":
        choose = input("Deseja sair? (Sim/Não): ").strip().lower()
        if choose == "sim":
            break
    else:
        print("Opção inválida.")
