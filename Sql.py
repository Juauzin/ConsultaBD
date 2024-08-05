
import pyodbc
from tkinter import *
def consultaSQl():
            # Define os parâmetros de conexão ao banco de dados: Inclui o driver, servidor, nome do banco de dados e informações de autenticação (neste caso, autenticação do Windows).
           
            dados_conexao = (
                "Driver={SQL Server};"
                "Server=JOAO\\EXPRESS;"
                "Database=BDTEST;"
                "Trusted_Connection=yes;"   
            )
            # Tenta estabelecer a conexão com o banco de dados:

            try:
                conexao = pyodbc.connect(dados_conexao)
                print("Conexão bem-sucedida!")
            except pyodbc.Error as ex:
                print("Erro na conexão:", ex)
            # Cria um cursor: Um cursor é um objeto que permite a execução de comandos SQL e a recuperação de dados do banco de dados.
            cursor = conexao.cursor()
            # Consultas
            consulta_sql = "SELECT  * FROM dbo.Tbl_Test  WHERe idade = 22"
            # Executa a consulta SQL: Envia a consulta para o banco de dados para ser executada.
            cursor.execute(consulta_sql)
            # Recupera todos os resultados da consulta: Armazena todos os registros retornados pela consulta em rows.

            rows = cursor.fetchall()
            # Itera sobre os resultados: Imprime cada linha dos resultados da consulta.
            resultado_texto = ""
            for row in rows:
             resultado_texto += " | ".join(map(str, row)) + "\n"

            texto_consultas["text"] = resultado_texto

            # Fecha o cursor: Libera os recursos associados ao cursor.

            cursor.close()
            
            # # Fecha a conexão com o banco de dados: Libera os recursos associados à conexão.
            conexao.close()
                       
janela = Tk()
janela.title("Consulta em Banco de Dados")

texto_inicial = Label(janela, text= "Clique no botão para fazer uma consulta")
# Indica a posição do texto
texto_inicial.grid(column=0, row=0)

texto_botao = Label(janela, text="Clique para consultar")
texto_botao.grid(column=0, row=1)
# Comand serve para executar a consulta
botao = Button(janela,text="FAZER CONSULTA", command=consultaSQl)
botao.grid(column=0,row=2)

texto_consultas = Label(janela, text="")
texto_consultas.grid(column=0, row= 3)

janela.mainloop()


