import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="lucas2003",
            database="vsprog"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

# Função para criar a tabela TAREFAS se não existir
def criar_tabela_users(conexao):
    try:
        cursor = conexao.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS USUARIOS(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            console VARCHAR(255) NOT NULL
        )
        """
        cursor.execute(sql)
        print("Tabela USUARIOS criada ou já existente.")
    except mysql.connector.Error as erro:
        print(f"Erro ao criar tabela Usuarios: {erro}")


def criar_tabela_jogos(conexao):
    try:
        cursor = conexao.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS JOGOS(
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            data_lanc DATE NOT NULL
        )
        """
        cursor.execute(sql)
        print("Tabela USUARIOS criada ou já existente.")
    except mysql.connector.Error as erro:
        print(f"Erro ao criar tabela Jogos: {erro}")

# Função para inserir uma nova tarefa na tabela TAREFAS
def inserir_usuario(conexao, nome, console):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO USUARIOS (nome, console) VALUES (%s, %s)"
        val = (nome, console)
        cursor.execute(sql, val)
        conexao.commit()
        print("Tarefa inserida com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir tarefa: {erro}")
        
def inserir_jogo(conexao, nome, data_lanc):
    try:
        cursor = conexao.cursor()
        sql1 = "INSERT INTO JOGOS (nome, data_lanc) VALUES (%s, %s)"
        val = (nome, data_lanc)
        cursor.execute(sql1, val)
        conexao.commit()
        print("Tarefa inserida com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir tarefa: {erro}")

# Função para remover uma tarefa da tabela TAREFAS pelo ID
def remover_usuario(conexao, id_tarefa):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM USUARIOS WHERE id = %s"
        val = (id_tarefa,)
        cursor.execute(sql, val)
        conexao.commit()
        print("Tarefa removida com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao remover tarefa: {erro}")
def remover_Jogos(conexao, id_tarefa):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM JOGOS WHERE id = %s"
        val = (id_tarefa,)
        cursor.execute(sql, val)
        conexao.commit()
        print("Tarefa removida com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao remover tarefa: {erro}")


# Função para consultar todas as tarefas na tabela TAREFAS
def consultar_Usuarios(conexao):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM USUARIOS"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]},Console: {resultado[2]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar Usuario: {erro}")
def consultar_Jogos(conexao):
    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM JOGOS"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"ID: {resultado[0]}, Nome: {resultado[1]},Console: {resultado[2]}")
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar jogos: {erro}")

# Função principal
def main():
    conexao = conectar_bd()
    if conexao:
        criar_tabela_users(conexao)
        criar_tabela_jogos(conexao)
        while True:
            print("\nOpções:")
            print("1. Inserir Usuario")
            print("2. Inserir Jogos")
            print("3. Remover Usuario")
            print("4. Remover Jogo")
            print("5. Consultar Usuario")
            print("6. Consultar Jogos")
            print("7. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Digite o nome do Usuario: ")
                console = input("Digite a console do usuario: ")
                inserir_usuario(conexao, nome, console)
            elif escolha == "2":
                nome_j = input("Digite o nome do Jogo: ")
                data = input("Digite a data de lancamento do Jogo: ")
                inserir_jogo(conexao, nome_j, data)
            elif escolha == "3":
                id_tarefa = int(input("Digite o ID do usuario a ser removido: "))
                remover_usuario(conexao, id_tarefa)
            elif escolha == "4":
                id_tarefa = int(input("Digite o ID do jogo a ser removido: "))
                remover_Jogos(conexao, id_tarefa)
            elif escolha == "5":
                consultar_Usuarios(conexao)
            elif escolha == "6":
                consultar_Jogos(conexao)
            elif escolha == "7":
                break
            else:
                print("Opção inválida.")

        conexao.close()
        print("Conexão com o banco de dados encerrada.")

if __name__ == "__main__":
    main()
