#coding:utf-8
import csv
import pymysql
import os
import csv
import os.path
from datetime import datetime
from time import time

inicio_execucao = time()

#Parametros da conexão###
host = '127.0.0.1'
user = 'sgs'
password = 'tamandua'
db = 'Netflow'
port = 3306
##########################

wd = '/home/sleifer/Documentos/scripts_netflow' # recebe o caminho do diretorio em que o script esta sendo executado
conexao = pymysql.connect(host,user,password,db,port) #cria a conexão com o BD
cursor = conexao.cursor() #cria um objeto para manipular o banco atraves do python
lista_arquivos = [] #lista para armazenar todos os arquivos na pasta escopo

for caminho, diretorio, arquivo in os.walk(wd+'/Parseados/Escopo/'):
        for nome in arquivo:
                lista_arquivos.append(nome)
lista_arquivos = sorted(lista_arquivos)

if os.path.isfile(wd+'/Parseados/log_inseridos.txt') == False: #Condição para 1ª execução do script

    with open(wd+'/Parseados/log_inseridos.txt','w') as logfile: #somente cria o arquivo de log.
        logfile.close()

    for arquivo in lista_arquivos:
        escopo = open(wd+'/Parseados/Escopo/' + arquivo) 
        sumario = open(wd+'/Parseados/Sumario/' + arquivo)
        try:
            reader_escopo = csv.reader(escopo)
            for linha in reader_escopo:
                valores = (linha[0],linha[1],linha[3],
                    linha[4],linha[5],linha[6],linha[7],
                    linha[8],linha[9],linha[10],linha[11],
                    linha[12],linha[13],linha[14],linha[15])
                
                cursor.execute('insert into Fluxos ('
                    'Data_fluxo,'
                    'Tempo_Inicio,'
                    'Tempo_Encerramento,'
                    'Duração,'
                    'Protocolo,'
                    'IP_Origem,'
                    'IP_Destino,'
                    'Porta_Origem,'
                    'Porta_Destino,'
                    'Pacotes,'
                    'Bytes,'
                    'Fluxos,'
                    'Bytes_Por_Segundo,'
                    'Pacotes_Por_Segundo,'
                    'Bytes_Por_Pacotes)'
                f'values {valores}')
            conexao.commit()
            valores = 0
            
            reader_sumario = csv.reader(sumario)
            for linha in reader_sumario:
                valores = (arquivo.strip('.csv'),linha[0],
                    linha[1],linha[2],linha[3],linha[4],linha[5])
                
                cursor.execute('insert into Lista_Fluxos ('
                    'Nome_arquivo_de_Fluxo,'
                    'Numero_total_de_fluxos,'
                    'Numero_total_de_bytes,'
                    'Numero_total_de_pacotes,'
                    'Media_de_bytes_por_segundo,'
                    'Media_de_pacotes_por_segundo,'
                    'Media_de_bytes_por_pacotes) '
                f'values {valores}')
            conexao.commit()
            valores = 0
            
            with open(wd+'/Parseados/log_inseridos.txt','a') as logfile:
                logfile.write(arquivo+','+str(datetime.now())+'\n')

        finally:
            escopo.close()
            sumario.close()
            logfile.close()
    cursor.close()
    conexao.close()
    
    fim_execucao = time()
    print(f'{fim_execucao - inicio_execucao} segundos')

else:
    lista_inseridos = {}
    with open(wd+'/Parseados/log_inseridos.txt') as logfile:
            for linha in logfile:
                    linha_separada = linha.split(',')
                    lista_inseridos[linha_separada[0].strip('.csv')] = True
    logfile.close()
    
    for pos in range(len(lista_arquivos)):
        nome_arquivo = lista_arquivos[pos].strip('.csv')               
                
        if nome_arquivo not in lista_inseridos:
            escopo = open(wd+'/Parseados/Escopo/' + lista_arquivos[pos]) 
            sumario = open(wd+'/Parseados/Sumario/' + lista_arquivos[pos])
                    
            try:
                reader_escopo = csv.reader(escopo)
                for linha in reader_escopo:
                    valores = (linha[0],linha[1],linha[3],
                        linha[4],linha[5],linha[6],linha[7],
                        linha[8],linha[9],linha[10],linha[11],
                        linha[12],linha[13],linha[14],linha[15])
                        
                    cursor.execute('insert into Fluxos ('
                        'Data_fluxo,'
                        'Tempo_Inicio,'
                        'Tempo_Encerramento,'
                        'Duração,'
                        'Protocolo,'
                        'IP_Origem,'
                        'IP_Destino,'
                        'Porta_Origem,'
                        'Porta_Destino,'
                        'Pacotes,'
                        'Bytes,'
                        'Fluxos,'
                        'Bytes_Por_Segundo,'
                        'Pacotes_Por_Segundo,'
                        'Bytes_Por_Pacotes)'
                    f'values {valores}')
                conexao.commit()
                valores = 0
                    
                reader_sumario = csv.reader(sumario)
                for linha in reader_sumario:
                    valores = (nome_arquivo,linha[0],
                        linha[1],linha[2],linha[3],linha[4],linha[5])
                    
                    cursor.execute('insert into Lista_Fluxos ('
                            'Nome_arquivo_de_Fluxo,'
                            'Numero_total_de_fluxos,'
                            'Numero_total_de_bytes,'
                            'Numero_total_de_pacotes,'
                            'Media_de_bytes_por_segundo,'
                            'Media_de_pacotes_por_segundo,'
                            'Media_de_bytes_por_pacotes) '
                        f'values {valores}')
                    conexao.commit()
                    valores = 0
                    
                with open(wd+'/Parseados/log_inseridos.txt','a') as logfile:
                    logfile.write(lista_arquivos[pos]+','+str(datetime.now())+'\n')

            finally:
                escopo.close()
                sumario.close()
                logfile.close()
            
    cursor.close()
    conexao.close()
    
    fim_execucao = time()
    print(f'{fim_execucao - inicio_execucao} segundos')    


