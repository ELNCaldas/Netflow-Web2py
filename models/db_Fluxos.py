# -*- coding: utf-8 -*-
db.define_table('Fluxos',
    Field('Data_fluxo','date'),
    Field('Tempo_Inicio','time'),
    Field('Tempo_Encerramento','time'),
    Field('Duração','float'),
    Field('Protocolo','string'),
    Field('IP_Origem','string'),
    Field('IP_Destino','string'),
    Field('Porta_Origem','string'),
    Field('Porta_Destino','string'),
    Field('Pacotes','integer'),
    Field('Bytes','integer'),
    Field('Fluxos','integer'),
    Field('Bytes_Por_Segundo','integer'),
    Field('Pacotes_Por_Segundo','integer'),
    Field('Bytes_Por_Pacotes','integer')
)
