users = {
    "João": {"senha": "12345", "saldo": 1000},
    "Marcos": {"senha": "lambdaehlegal", "saldo": 500},
    "Paulo": {"senha": "maybe", "saldo": 1500},
}

getuser = lambda: input("Qual seu nome? ")
getpassword = lambda: input("Qual sua senha? ")
blocked = lambda: print("Acesso bloqueado. Usuário não existente ou senha inválida")
allowed = lambda: print("Acesso Permitido")
# Obtenha o nome do usuário uma vez e armazene em uma variável
nome_do_usuario = getuser()

# Obtenha a senha do usuário uma vez e armazene em uma variável
senha_do_usuario = getpassword()

nome = lambda nome_u: nome_u
# Verifica se o usuário existe no dicionário usando uma função lambda
cond = lambda user, gpassword: users.get(user, {}).get("senha") == gpassword

Tela = lambda user: print(f"Olá, {nome(user)}! Escolha qual opção você deseja:\n1. Extrato Bancário\n2. Saque Bancário\n3. Depósito Bancário\nDigite 'Sim' para selecionar uma opção ou 'Não' para sair: ")

# Faça o login e obtenha o usuário
login = lambda users, guser, gpassword, Tela, blocked, allowed: (allowed() or Tela(guser) or users.get(guser))  if cond(guser, gpassword) else blocked()

usuario_logado = login(users, nome_do_usuario, senha_do_usuario, Tela, blocked, allowed)

# Lambda para saque
sacar = lambda usuario: (
    valor := float(input("Quanto você deseja Sacar? R$ ")),
    print(f"Você selecionou Saque Bancário. Executando ação..."),
    (print('Saldo Insuficiente para saque!') if valor > usuario['saldo']
     else (
         (lambda: usuario.__setitem__('saldo', usuario['saldo'] - valor))(),
         print(f"{nome_do_usuario} Valor de R$ {valor:.2f} sacado com sucesso\nSeu novo Extrato é de R$ {usuario['saldo']:.2f}")
     ))[1] if valor > 0 else print("Valor de saque inválido.")
)

# Lambda para depósito
depositar = lambda usuario: (
    valor := float(input("Quanto você deseja Depositar? R$ ")),
    print(f"Você selecionou Depósito Bancário. Executando ação..."),
    (print("Valor de depósito inválido.") if valor <= 0
     else (
         (lambda: usuario.__setitem__('saldo', usuario['saldo'] + valor))(),
         print(f"{nome_do_usuario} Valor de R$ {valor:.2f} depositado com sucesso\nSeu novo Extrato é de R$ {usuario['saldo']:.2f}")
     ))[1] if valor > 0 else print("Valor de depósito inválido.")
)

# Lambda para sair
sair = lambda usuario: (
    choose := input("Deseja sair? (Sim/Não): ").strip().lower(),
    (exit() if choose == "sim" else None) if choose == "sim" else None
)



while usuario_logado:
    # Após o login bem-sucedido, obtenha a escolha do usuário
    opcao = input("Escolha uma opção (1, 2 ou 3) ou deseja sair (digitar sair): ").strip().lower()
    
    # Usando list comprehension para mapear opções para funções correspondentes
    acoes = {
        '1': (lambda: print(f"{nome_do_usuario} Você possui: R$ {usuario_logado['saldo']:.2f}"), "Extrato Bancário"),
        '2': (lambda: sacar(usuario_logado), "Saque Bancário"),
        '3': (lambda: depositar(usuario_logado), "Depósito Bancário"),
        'sair': (lambda: sair(usuario_logado), "Sair"),
    }

    # Executa a ação correspondente à opção ou imprime "Opção inválida"
    acao = acoes.get(opcao)
    if acao:
        acao[0]()  # Chama a função correspondente
        print(f"Você selecionou {acao[1]}. Executando ação...")
    else:
        print("Opção inválida.")