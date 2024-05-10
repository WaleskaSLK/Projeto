# from tkinter import ttk
import tkinter as tk
# import sqlite3 as sql
# import colorama as color
from customtkinter import *
# from PIL import Image, ImageTk
import sqlite3 as sql
import FUNCOES_APK as fun

def USINAS():
    caminho = r"C:\Users\20221CECA0402\Documents\Projeto_WRL\BD_WRL\REGISTROS_WRL.db"
    conn, cursor = fun.CONECTA_BD(caminho)
    comando = f"SELECT Grupo FROM DADOS_EMPRESAS "
    cursor.execute(comando)
    dados_banco = cursor.fetchall()
    fun.DESCONECTA_BD(conn)
    
    dados_filtrados = list(set(item[0] for item in dados_banco))
    return dados_filtrados

def SITE():
    caminho = r"C:\Users\20221CECA0402\Documents\Projeto_WRL\BD_WRL\REGISTROS_WRL.db"
    conn, cursor = fun.CONECTA_BD(caminho)
    comando = f"SELECT Site FROM DADOS_EMPRESAS "
    cursor.execute(comando)
    dados_banco = cursor.fetchall()
    fun.DESCONECTA_BD(conn)
    
    dados_filtrados = list(set(item[0] for item in dados_banco))
    return dados_filtrados

def FUROS_ID():
    caminho = r"C:\Users\20221CECA0402\Documents\Projeto_WRL\BD_WRL\REGISTROS_WRL.db"
    
    conn, cursor = fun.CONECTA_BD(caminho)
    ID = f"SELECT ID FROM DADOS_EMPRESAS "
    cursor.execute(ID)
    dados_ID = cursor.fetchall()
    
    FUROS = f"SELECT FUROS FROM DADOS_EMPRESAS "
    cursor.execute(FUROS)
    dados_FUROS = cursor.fetchall()
    fun.DESCONECTA_BD(conn)
    
    dados_filtrados = [f"{furos[0]} - {id[0]}" for furos, id in zip(dados_FUROS, dados_ID)]
    return dados_filtrados

def TIPO():
    caminho = r"C:\Users\20221CECA0402\Documents\Projeto_WRL\BD_WRL\REGISTROS_WRL.db"
    conn, cursor = fun.CONECTA_BD(caminho)
    comando = f"SELECT TIPO FROM DADOS_EMPRESAS "
    cursor.execute(comando)
    dados_banco = cursor.fetchall()
    fun.DESCONECTA_BD(conn)
    
    dados_filtrados = list(set(item[0] for item in dados_banco))
    return dados_filtrados

def ENTRY_INT(inp_text):
    if inp_text == "": return True
    try:
        value = int(inp_text)
    except ValueError: return False
    
    return 0 <= value <= 100000000000 #Qual a vida máxima geralmente?

def ENTRY_STRING(inp_text):
    if inp_text == "": return True
    try:
        value = str(inp_text)
    except ValueError: return False

def validador(input):
    comando = (input.register(ENTRY_INT), "%P") 
    return comando


    
def tela(inp_janela):
    inp_janela.title("Where Register Lances (WRL)")
    inp_janela.configure(background= '#9BCD9B')
    inp_janela.geometry("1000x600")
    inp_janela.resizable(True, True) #se quiser impedir que amplie ou diminua a tela, altere para False
    # janela.maxsize(width=1920, height=1080) #limite máximo da tela
    inp_janela.minsize(width=700, height=450) #limite minimo da tela

def frames_da_tela(inp_janela): 
        global frame_1
        
        frame_1 = tk.Frame(inp_janela,
                            bg= '#B4FF9A',
                            highlightbackground= '#668B8B')
        frame_1.place(relx=0.01, rely=0.02,relwidth=0.98, relheight=0.96)
        
        return frame_1

def componentes_frame1(inp_frame):
    
    # {=======================Título=========================}
    titulo = fun.CRIAR_LABEL(inp_frame, "Selecionar Bico", '#B4FF9A', "#005200", 'arial', '25', 'bold')
    titulo.place(relx=0.38, rely=0.04) 

    # {=======================Dados à inserir=========================
    # Filtrar os dados
    # Nome permitir só string
    # dar Função ao botão voltar e continuar
    # aumentar a fonte
 
    # {=======================USINA=========================}
    label_usina = fun.CRIAR_LABEL(inp_frame, "Usina/Grupo: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_usina.place(relx=0.05, rely=0.2)

    Var_Usina = tk.StringVar(inp_frame)
    
    Menu_Usina = tk.OptionMenu(inp_frame, Var_Usina, *USINAS())
    Menu_Usina.place(relx=0.05, rely=0.27, relwidth=0.35, relheight=0.06)

    # {=======================SITE=========================}
    label_site = fun.CRIAR_LABEL(inp_frame, "Site: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_site.place(relx=0.55, rely=0.2)

    Var_site = tk.StringVar(inp_frame)
    
    Menu_site = tk.OptionMenu(inp_frame, Var_site, *SITE())
    Menu_site.place(relx=0.55, rely=0.27, relwidth=0.35, relheight=0.06)

    # {=======================BOF _ ID=========================}
    label_IDTipo = fun.CRIAR_LABEL(inp_frame, "FUROS - ID: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_IDTipo.place(relx=0.05, rely=0.4)

    Var_IDTipo = tk.StringVar(inp_frame)
    """Var_IDTipo.set(FUROS_ID()[0])"""
    
    Menu_IDTipo = tk.OptionMenu(inp_frame, Var_IDTipo, *FUROS_ID())
    Menu_IDTipo.place(relx=0.05, rely=0.47, relwidth=0.27, relheight=0.06)
    
    # {=======================TIPO=========================}
    label_tipo = fun.CRIAR_LABEL(inp_frame, "Tipo: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_tipo.place(relx=0.35, rely=0.4)

    Var_tipo = tk.StringVar(inp_frame)
    
    Menu_tipo = tk.OptionMenu(inp_frame, Var_tipo, *TIPO())
    Menu_tipo.place(relx=0.35, rely=0.47, relwidth=0.27, relheight=0.06)
    
    # {=======================VIDA=========================}
    label_vida = fun.CRIAR_LABEL(inp_frame, "Vida: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_vida.place(relx=0.65, rely=0.4)

    input_vida = tk.Entry(inp_frame, validate= "key", validatecommand= validador(inp_frame) )
    input_vida.place(relx=0.65, rely=0.47, relwidth=0.27, relheight=0.06)

    # {=======================Usuário=========================}
    label_usuario = fun.CRIAR_LABEL(inp_frame, "Usuário: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_usuario.place(relx=0.05, rely=0.6)

    input_usuario = tk.Entry(inp_frame, validate= "key", validatecommand= ENTRY_STRING(inp_frame))
    input_usuario.place(relx=0.05, rely=0.67, relwidth=0.85, relheight=0.06)

    # {=======================Botão Voltar e Continuar=========================}
    bt_voltar = fun.CRIAR_BOTAO(inp_frame, "MENU",'#258D19', 'white',3,'20','',"hand2",)
    bt_voltar.place(relx=0.05, rely=0.88, relwidth=0.2, relheight=0.08)

    bt_continuar = fun.CRIAR_BOTAO(inp_frame, "CONTINUAR",'#258D19', 'white',3,'20','',"hand2",)
    bt_continuar.place(relx=0.75, rely=0.88, relwidth=0.2, relheight=0.08)


def aba_cadastro(): # AVISO -> passar a variavel "inp_janela" dentro dos ()
    # janela_dois = tk.Toplevel()
    janela_dois = tk.Tk() #AVISO ->tirar esta linha e manter a de cima
    tela(janela_dois)
    frames_da_tela(janela_dois)
    componentes_frame1(frame_1)
    # janela_dois.transient(inp_janela)
    # janela_dois.focus_force() #era pra janela ser o foco
    # janela_dois.janela_dois.grab_set()
    janela_dois.mainloop() #AVISO ->tirar esta linha

print(FUROS_ID())
aba_cadastro() #AVISO ->tirar esta linha
