users = {
    "João": "12345",
    "Marcos": "lambdaehlegal"
}

getuser = lambda: input("Qual seu nome? ")
getpassword = lambda: input("Qual sua senha? ")
blocked = lambda: print("FRACASSO")
allowed = lambda: print("SUCESSO")
nome = lambda user: users[user]
cond = lambda user, gpassword: not users.get(user) == gpassword
nome_usuario = getuser()
senha_usuario = getpassword()


path = "./q2_JoãoHolanda/q2_JoãoHolanda.txt" 
newlines = [f"Nome:{nome_usuario}", f"Senha:{senha_usuario}", "Erro capturado com sucesso"]
write_on_file = lambda f, newlines: [f.write("\n" + nline) for nline in newlines]


login = lambda users, guser, gpassword, blocked, allowed: (blocked() or  write_on_file (open (path, "w"), newlines)  or users.get(guser))  if cond(guser, gpassword) else (allowed())

usuario_logado = login(users, nome_usuario, senha_usuario, blocked, allowed)