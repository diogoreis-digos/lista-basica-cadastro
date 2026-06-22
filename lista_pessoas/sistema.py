from lista_pessoas.lib.arquivo import *
from time import sleep

arq ='listadedados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo:
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar nova pessoa:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta ==3 :
        #Opção de sair do sistema:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO: DIGITE UMA OPÇÃO VÁLIDA\033[m')
    sleep(2)


