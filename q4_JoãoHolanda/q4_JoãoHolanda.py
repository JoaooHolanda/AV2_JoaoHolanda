import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root", #O seu nome de usuario certamente eh root
  password="#euamoDeus2" #Aqui voce devera digitar a senha que voce criou ao baixar o MySQL
)

crs = mydb.cursor()

execsqlcmd = lambda cmd, crs: crs.execute (cmd)

execcreatetable = lambda table, attrs, crs : execsqlcmd("CREATE TABLE IF NOT EXISTS  " + table + " (" + attrs + ");\n", crs)
execcreatedatabase = lambda dbname, crs: execsqlcmd("CREATE DATABASE IF NOT EXISTS   " + dbname + ";\n", crs)
execcreatedatabase = lambda dbname, crs: execsqlcmd("CREATE DATABASE IF NOT EXISTS  " + dbname + ";\n", crs)
execdropdatabase = lambda dbname, crs : execsqlcmd ("DROP DATABASE " + dbname + ";\n", crs)
execdroptable = lambda dbname, crs : execsqlcmd ("DROP TABLE " + dbname + ";\n", crs)
execusedatabase = lambda dbname, crs : execsqlcmd ("USE " + dbname + ";\n", crs)
execselectfromwhere = lambda attrs, table, wherecond, crs : execsqlcmd ("SELECT " + attrs + " FROM " + table + " WHERE " + wherecond + ";", crs)
execinsertinto = lambda table, attrs, values, crs : execsqlcmd ("INSERT INTO " + table + " (" + attrs + ")" + " VALUES (" + values + ");", crs)


execcreatedatabase("Joaobase", crs)

#"USE DATABASE mydatabase"
execusedatabase ("Joaobase", crs)

#"CREATE TABLE Usuarios 
execcreatetable ("usuarios", "name VARCHAR (255) , console VARCHAR (255)", crs)
#"CREATE TABLE Jogos 
execcreatetable ("jogos", "name VARCHAR (255) , dt_lanc DATE", crs)

#inseri os usuarios
execinsertinto ("usuarios", "name , console", "'João', 'Xbox 360'", crs)
execinsertinto ("usuarios", "name , console", "'Pedro', 'Xbox One'", crs)
execinsertinto ("usuarios", "name , console", "'Tiago', 'Ps4'", crs)
#inseri os jogos - ano yyyy/mm/dd
execinsertinto ("jogos", "name , dt_lanc", "'Minecraft', '2012/03/15'", crs)
execinsertinto ("jogos", "name , dt_lanc", "'UltilDown', '2013/01/29'", crs)
execinsertinto ("jogos", "name , dt_lanc", "'Lego star', '2013/02/28'", crs)

#CONSULTA A TABELA USUARIOS
execselectfromwhere ("*", "usuarios", "true", crs)


res = crs.fetchall ()
print_result = lambda res : [print (x) for x in res]

print_result (res)

#CONSULTA A TABELA JOGOS
execselectfromwhere ("*", "jogos", "true", crs)
res = crs.fetchall()
print_result(res)



#apaga as tabelas e o database ao final!se voce descomentar qualquer uma ela quebra, tem a opcao de deixar como CREATE TABLE/DATABASE IF NOT EXIST!
execdroptable ("usuarios", crs)
execdroptable ("jogos", crs)
execdropdatabase ("Joaobase", crs)
