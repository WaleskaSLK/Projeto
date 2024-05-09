# from tkinter import ttk
import tkinter as tk
# import sqlite3 as sql
# import colorama as color
from customtkinter import *
# from PIL import Image, ImageTk

import FUNCOES_APK as fun

def tela(inp_janela):
    inp_janela.title("Where Register Lances (WRL)")
    inp_janela.configure(background= '#9BCD9B')
    inp_janela.geometry("900x500")
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
    titulo.place(relx=0.4, rely=0.05) 

    # {=======================Dados à inserir=========================}
    # -->Usina(país e regiao), site, Furos, ID, Posição?, carro?, convertedor
    # mostrar os existentes no frame 2

    # {=======================USINA=========================}
    label_usina = fun.CRIAR_LABEL(inp_frame, "Usina/Grupo: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_usina.place(relx=0.05, rely=0.2)

    input_usina = tk.Entry(inp_frame)
    input_usina.place(relx=0.047, rely=0.26, relwidth=0.3, relheight=0.05)

    # {=======================SITE=========================}
    label_site = fun.CRIAR_LABEL(inp_frame, "Site: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_site.place(relx=0.55, rely=0.2)

    # input_site = tk.Entry(inp_frame)
    # input_site.place(relx=0.15, rely=0.35, relwidth=0.8, relheight=0.05)

    # {=======================ID - Tipo=========================}
    label_furos = fun.CRIAR_LABEL(inp_frame, "ID - Tipo: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_furos.place(relx=0.05, rely=0.4)

    # input_furos = tk.Entry(inp_frame)
    # input_furos.place(relx=0.18, rely=0.5, relwidth=0.27, relheight=0.05)
    
    # {=======================VIDA=========================}
    label_furos = fun.CRIAR_LABEL(inp_frame, "Vida: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_furos.place(relx=0.55, rely=0.4)

    # input_furos = tk.Entry(inp_frame)
    # input_furos.place(relx=0.6, rely=0.5, relwidth=0.35, relheight=0.05)

    # {=======================Usuário=========================}
    label_ID = fun.CRIAR_LABEL(inp_frame, "Usuário: ", '#B4FF9A', "#1C1C1C", 'arial', '20', 'bold')
    label_ID.place(relx=0.05, rely=0.6)

    # input_ID = tk.Entry(inp_frame)
    # input_ID.place(relx=0.11, rely=0.65, relwidth=0.85, relheight=0.05)

    # {=======================Botão Voltar e Continuar=========================}
    bt_voltar = fun.CRIAR_BOTAO(inp_frame, "MENU",'#258D19', 'white',3,'20','',"hand2",)
    bt_voltar.place(relx=0.05, rely=0.89, relwidth=0.2, relheight=0.08)

    bt_continuar = fun.CRIAR_BOTAO(inp_frame, "CONTINUAR",'#258D19', 'white',3,'20','',"hand2",)
    bt_continuar.place(relx=0.75, rely=0.89, relwidth=0.2, relheight=0.08)


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


aba_cadastro() #AVISO ->tirar esta linha
