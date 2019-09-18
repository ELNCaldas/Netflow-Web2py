# -*- coding: utf-8 -*-
db.define_table('Lista_Fluxos',
    Field('Nome_arquivo_de_Fluxo','string'),
    Field('Numero_total_de_fluxos','integer'),
    Field('Numero_total_de_bytes','integer'),
    Field('Numero_total_de_pacotes','integer'),
    Field('Media_de_bytes_por_segundo','float'),
    Field('Media_de_pacotes_por_segundo','float'),
    Field('Media_de_bytes_por_pacotes','float')
)
