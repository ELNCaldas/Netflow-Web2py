#coding: utf-8
#Script para a criação das tabelas do banco

import pymysql #https://pymysql.readthedocs.io/en/latest/index.html


#Parametros da conexão###
host = '127.0.0.1'
user = 'sgs'
password = 'tamandua'
db = 'Netflow'
port = 3306
##########################

conexao = pymysql.connect(host,user,password,db,port) #cria a conexão com o BD

cursor = conexao.cursor() #cria um objeto para manipular o banco atraves do python
#Date first seen/Date last seen/Duration/Proto/Src IP Addr/Dst IP Addr/Src Pt/Dst Pt/Packets/Bytes/Flows/bps/pps/Bpp
try:
    cursor.execute('create table if not exists Fluxos (' #executa o comando em sql
        'id int not null auto_increment,'
        'Data_fluxo date not null,'
        'Tempo_Inicio time not null,'
        'Tempo_Encerramento time not null,'
        'Duração float not null,'
        'Protocolo varchar(10) not null,'
        'IP_Origem varchar(30) not null,'
        'IP_Destino varchar(30) not null,'
        'Porta_Origem varchar(30) not null,'
        'Porta_Destino varchar(30) not null,'
        'Pacotes int not null,'
        'Bytes int not null,'
        'Fluxos int not null,'
        'Bytes_Por_Segundo int not null,'
        'Pacotes_Por_Segundo int not null,'
        'Bytes_Por_Pacotes int not null,'
        'primary key(id))')

    cursor.execute('create table if not exists Lista_Fluxos (' #executa o comando em sql
        'id int not null auto_increment,'
        'Nome_arquivo_de_Fluxo varchar(30) not null,'
        'Numero_total_de_fluxos int not null,'
        'Numero_total_de_bytes int not null,'
        'Numero_total_de_pacotes int not null,'
        'Media_de_bytes_por_segundo float not null,'
        'Media_de_pacotes_por_segundo float not null,'
        'Media_de_bytes_por_pacotes float not null,'
        'primary key(id))')
    '''
    cursor.execute('create table if not exists Flow_Raw (' #executa o comando em sql
        'id int not null auto_increment,'
        'Flags int not null,'
        'Export_sysid int not null,'
        'Size int not null,'
        'fist int not null,'
        'last int not null,'
        'msec_first int not null,'
        'msec_last int not null,'
        'src_addr int not null,'
        'dst_addr int not null,'
        'src_port int not null,'
        'dst_port int not null,'
        'fwd_status int not null,'
        'tcp_flag int not null,'
        'proto int not null,'
        'src_tos int not null,'
        'in_packtes int not null,'
        'in_bytes int not null,'
        'input int not null,'
        'output int not null,'
        'src_as int not null,'
        'dst_as int not null,'
        'src_mask int not null,'
        'dst_mask int not null,'
        'dst_tos int not null,'
        'direction int not null,'
        'ip_next_hop int not null,'
        'ip_router int not null,'
        'engine_type int not null,'
        'engine_ID int not null,'
        'primary key(id))')
    '''
finally:
    conexao.close()
    print('Tabelas Criadas com Sucesso!')
