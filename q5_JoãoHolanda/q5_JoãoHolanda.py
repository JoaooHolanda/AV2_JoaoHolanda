import sys
from flask import Flask, request, render_template

# Redirecione a saída para um arquivo de log
log_file = open('output.log', 'w')
original_stdout = sys.stdout
sys.stdout = log_file

app = Flask(__name__, template_folder='templates_folder')

users = {
    "sam2584": "123",
    "robs61286": "1234"
}

welcome = lambda: f'WELCOME {request.form["username"]}!!'

wrong = lambda: (print(f'Usuario:{request.form["username"]} -Senha: {request.form["password"]}') or 'WRONG PASSWORD!!!!')
invalid = lambda: (print(f'User {request.form["username"]} - {request.form["password"]} does not exist!') or f'usuario:{request.form["username"]} com a senha: {request.form["password"]} does not exist!')

password_matches = lambda dic: dic.get(request.form["username"]) == request.form["password"]
check_password = lambda: welcome() if password_matches(users) else wrong()
check_if_user_exists = lambda: check_password() if request.form["username"] in users else invalid()

reqresp = lambda: check_if_user_exists() if request.method == 'POST' else render_template('index.html')
app.add_url_rule('/', 'index', reqresp, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)

# Restaure a saída padrão após a execução do aplicativo Flask
sys.stdout = original_stdout
log_file.close()
