# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------
from datetime import datetime
from matplotlib import pyplot
# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))
'''
def teste():
    querry = db(db.Lista_Fluxos).select()

    x = []
    y1 = []
    y2 = []
    y3 = []

    for row in querry:
        
        x.append(datetime.strptime(row['Nome_arquivo_de_Fluxo'],'%Y%m%d%H%M'))
        y1.append(row['Numero_total_de_fluxos'])
        y2.append(row['Numero_total_de_bytes'])
        y3.append(row['Numero_total_de_pacotes'])


    figura = pyplot.figure()
    rect = figura.patch
    rect.set_facecolor('white')

    ax1 = figura.add_subplot(3,1,1)
    ax1.plot_date(x,y1,ls='-',marker=None,color='b')
    ax1.set_title('Exemplo')
    #ax1.set_xlabel('Tempo')
    ax1.set_ylabel('Total de Fluxos')
    ax1.grid(True)
    ax1.autoscale(True,'both',True)

    ax2 = figura.add_subplot(3,1,2)
    ax2.plot_date(x,y2,ls='-',marker=None,color='b')
    #ax2.set_title('Exemplo')
    #ax2.set_xlabel('Tempo')
    ax2.set_ylabel('Total de Bytes')
    ax2.grid(True)
    ax2.autoscale(True,'both',True)

    ax3 = figura.add_subplot(3,1,3)
    ax3.plot_date(x,y3,ls='-',marker=None,color='b')
    #ax3.set_title('Exemplo')
    ax3.set_xlabel('Tempo')
    ax3.set_ylabel('Total de Pacotes')
    ax3.grid(True)
    ax3.autoscale(True,'both',True)
    
    agora = str(datetime.now())
    nome_arquivo = 'applications/teste/static/images/grafico/graficoteste'
    nome_full = ("%s.%s.png"%(nome_arquivo,agora))
    
    pyplot.savefig('applications/teste2/static/images/grafico.png')
    
    return locals()
'''
def teste():
    querry = db(db.Lista_Fluxos).select()
    eixoX = []
    eixoY1 = [] #grafico de total de fluxos
    eixoY2 = [] #grafico de total de bytes
    eixoY3 = [] #grafico de total de pacotes

    for row in querry:
        #eixoX.append(datetime.strptime(row['Nome_arquivo_de_Fluxo'],'%Y%m%d%H%M'))
        eixoX.append(row['Nome_arquivo_de_Fluxo'])
        eixoY1.append(row['Numero_total_de_fluxos'])
        eixoY2.append(row['Numero_total_de_bytes'])
        eixoY3.append(row['Numero_total_de_pacotes'])
    return dict(x = eixoX, y1 = eixoY1, y2 = eixoY2, y3 = eixoY3)



# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
