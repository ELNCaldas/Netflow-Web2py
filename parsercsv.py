#!/usr/bin/python3
#coding: utf-8
#Scrip para parseamento de arquivos dump para csv.

import os #https://docs.python.org/3/library/os.html#module-os
import subprocess #https://docs.python.org/3/library/subprocess.html#module-subprocess
import csv #https://docs.python.org/3/library/csv.html?highlight=csv
import os.path #https://docs.python.org/3/library/os.path.html
from datetime import datetime #https://docs.python.org/3/library/datetime.html?highlight=datetime#module-datetime
from time import time

inicio_execucao = time()

wd = '/home/sleifer/Documentos/scripts_netflow'
lista_arquivos = [] #cria uma lista para receber o todos os arquivo que forem encontrados no diretorio.

dir_arquivos_de_fluxo = '/home/sleifer/Documentos/sgsFlow/'

#cria uma lista contendo o caminho completo + o nome dos arquivos dentro do diretorio
for caminho, diretorio, arquivo in os.walk(dir_arquivos_de_fluxo):
        for nome in arquivo:
                if 'nfcapd' in nome and 'current' not in nome:
                        lista_arquivos.append(os.path.join(caminho,nome))
lista_arquivos = sorted(lista_arquivos)

if os.path.isfile(wd+'/Parseados/log_parseados.txt') == False: #Condição para 1ª execução do script
        
        with open(wd+'/Parseados/log_parseados.txt','w') as logfile: #somente cria o arquivo de log.
                logfile.close()
        
        for pos in range(len(lista_arquivos)):
                nome_arquivo = lista_arquivos[pos].split('.') #cria uma variavel que guarda o nome de cada arquivo sendo lindo.
                escopo = subprocess.getoutput('nfdump -r '+lista_arquivos[pos]+' -o "fmt:%ts %te %td %pr %sa %da %sp %dp %pkt %byt %fl %bps %pps %bpp"' + ' -q'+' -N') #le o arquivo de dump atraves de um subprocedo do terminal.
                sumario = subprocess.getoutput('nfdump -r '+lista_arquivos[pos]+' -o csv'+' | tail -n 1')       

                #grava em um arquivo de txt a leitura do arquivo de dump
                try:
                        with open(wd+'/Parseados/em_parseamento.txt','w') as temp:
                                temp.write(escopo)   
                finally:
                        temp.close()

                #Transformando o arquivo txt em um arquivo csv
                try:
                        with open(wd+'/Parseados/em_parseamento.txt') as nao_parseado:
                                linhas = nao_parseado.readlines()
                                novaslinhas = []
                                for linha in linhas:
                                        nova_linha = linha.strip('\n').split()
                                        novaslinhas.append(nova_linha)
                

                        with open(wd+'/Parseados/Escopo/'+nome_arquivo[1]+'.csv', 'w') as parseado:
                                file_writer = csv.writer(parseado)
                                file_writer.writerows(novaslinhas)
                                
                        with open(wd+'/Parseados/Sumario/'+nome_arquivo[1]+'.csv', 'w') as sumario_parseado:
                                sumario_parseado.write(sumario)        

                        with open(wd+'/Parseados/log_parseados.txt','a') as logfile: 
                                logfile.write(nome_arquivo[1]+','+str(datetime.now())+'\n')
                        
                finally:
                        nao_parseado.close()
                        parseado.close()
                        sumario_parseado.close()
                        logfile.close()
                        os.remove(wd+'/Parseados/em_parseamento.txt') # Ao final do parseamento remover o arquivo em_parseamento.
        fim_execucao = time()
        print(f'{fim_execucao - inicio_execucao} segundos')

else: #Condição para execuções subsequentes.
        lista_parseados = {}
        with open(wd+'/Parseados/log_parseados.txt') as logfile:
                for linha in logfile:
                        linha_separada = linha.split(',')
                        lista_parseados[linha_separada[0]] = True
        logfile.close()
        
        for pos in range(len(lista_arquivos)):
                nome_arquivo = lista_arquivos[pos].split('.')               
                
                if nome_arquivo[1] not in lista_parseados:
                        escopo = subprocess.getoutput('nfdump -r '+lista_arquivos[pos]+' -o "fmt:%ts %te %td %pr %sa %da %sp %dp %pkt %byt %fl %bps %pps %bpp"' + ' -q'+' -N') #le o arquivo de dump atraves de um subprocedo do terminal.
                        sumario = subprocess.getoutput('nfdump -r '+lista_arquivos[pos]+' -o csv'+' | tail -n 1')       

                #grava em um arquivo de txt a leitura do arquivo de dump
                        try:
                                with open(wd+'/Parseados/em_parseamento.txt','w') as temp:
                                        temp.write(escopo)   
                        finally:
                                temp.close()

                #Transformando o arquivo txt em um arquivo csv
                        try:
                                with open(wd+'/Parseados/em_parseamento.txt') as nao_parseado:
                                        linhas = nao_parseado.readlines()
                                        novaslinhas = []
                                        for linha in linhas:
                                                nova_linha = linha.strip('\n').split()
                                                novaslinhas.append(nova_linha)

                                with open(wd+'/Parseados/Escopo/'+nome_arquivo[1]+'.csv', 'w') as parseado:
                                        file_writer = csv.writer(parseado)
                                        file_writer.writerows(novaslinhas)
                                        
                                with open(wd+'/Parseados/Sumario/'+nome_arquivo[1]+'.csv', 'w') as sumario_parseado:
                                        sumario_parseado.write(sumario)        

                                with open(wd+'/Parseados/log_parseados.txt','a') as logfile: 
                                        logfile.write(nome_arquivo[1]+','+str(datetime.now())+'\n')
                        
                        finally:
                                nao_parseado.close()
                                parseado.close()
                                sumario_parseado.close()
                                logfile.close()
                                os.remove(wd+'/Parseados/em_parseamento.txt') # Ao final do parseamento remover o arquivo em_parseamento.
        fim_execucao = time()                
        print(f'{fim_execucao - inicio_execucao} segundos')