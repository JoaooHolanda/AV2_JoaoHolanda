import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="seu_host",
            user="seu_usuario",
            password="sua_senha",
            database="nome_do_banco_de_dados"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

# Função para inserir um novo usuário na tabela USUARIOS
def inserir_usuario(conexao, nome, console):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO USUARIOS (nome, console) VALUES (%s, %s)"
        val = (nome, console)
        cursor.execute(sql, val)
        conexao.commit()
        print("Usuário inserido com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir usuário: {erro}")

# Função para remover um usuário da tabela USUARIOS pelo ID
def remover_usuario(conexao, id_usuario):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM USUARIOS WHERE id = %s"
        val = (id_usuario,)
        cursor.execute(sql, val)
        conexao.commit()
        print("Usuário removido com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao remover usuário: {erro}")

# Função para consultar todos os usuários na tabela USUARIOS
def consultar_usuarios(conexao):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM USUARIOS"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]}, Console: {resultado[2]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar usuários: {erro}")

# Função principal
def main():
    conexao = conectar_bd()
    if conexao:
        while True:
            print("\nOpções:")
            print("1. Inserir Usuário")
            print("2. Remover Usuário")
            print("3. Consultar Usuários")
            print("4. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Digite o nome do usuário: ")
                console = input("Digite o console: ")
                inserir_usuario(conexao, nome, console)
            elif escolha == "2":
                id_usuario = int(input("Digite o ID do usuário a ser removido: "))
                remover_usuario(conexao, id_usuario)
            elif escolha == "3":
                consultar_usuarios(conexao)
            elif escolha == "4":
                break
            else:
                print("Opção inválida.")

        conexao.close()
        print("Conexão com o banco de dados encerrada.")

if __name__ == "__main__":
    main()
