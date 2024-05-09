import tkinter as tk
import sqlite3 as sql
import colorama as color
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk
# from ABA_CADASTRO import aba_cadastro
from APK2 import aba_camera
import FUNCOES_APK as fun
# from APK2 import inicio


class APK():
    
    def __init__(self):
        self.janela_menu = tk.Tk()
        self.tela()
        self.frames_da_tela()
        self.componentes_frame1()
        self.janela_menu.mainloop()
    
    def tela(self): # {=======================Configuração de tela=========================}
        self.janela_menu.title("Where Register Lances (WRL)")
        self.janela_menu.configure(background= '#9BCD9B')
        self.janela_menu.geometry("1280x700")
        self.janela_menu.resizable(False, False) #se quiser impedir que amplie ou diminua a tela, altere para False
        # self.janela_menu.maxsize(width=1920, height=1080) #limite máximo da tela
        self.janela_menu.minsize(width=700, height=450) #limite minimo da tela
        
    def abinha(self):
        return (aba_cadastro(self.janela_menu))
    
    def abinha2(self):
        return (aba_camera(self.janela_menu))
    
    # def camera(self):
    #     return (inicio(self))

    def frames_da_tela(self): 
        self.frame_1 = fun.CRIAR_FRAME(self.janela_menu, '#B4FF9A', '#668B8B')
        self.frame_1.place(relx=0.01, rely=0.02,relwidth=0.98, relheight=0.96)
    
   
    def componentes_frame1(self):
        # {=======================Título=========================}
        self.titulo = fun.CRIAR_LABEL(self.frame_1, "Seja bem-vindo", '#B4FF9A', "#005200", 'arial', '25', 'bold')
        self.titulo.place(relx=0.21, rely=0.2)

        # {=======================Botões de Cadastro=========================}
        # inp_frame, inp_texto, inp_bg, inp_fg, inp_borda = NONE,inp_tamanho= NONE, inp_style = NONE, inp_cursor = NONE, inp_comando = NONE
        self.bt_cadastro_lanca = fun.CRIAR_BOTAO(self.frame_1,'Cadastrar Bico','#258D19', '#005200',3,'32','bold',"hand2", self.abinha )
        self.bt_cadastro_lanca.place(relx=0.07, rely=0.46, relwidth=0.4, relheight=0.2)

        self.bt_cadastro_funcionario = fun.CRIAR_BOTAO(self.frame_1,'Cadastrar Usina','#4EA93B','#005200',3,'32','bold',"hand2")
        self.bt_cadastro_funcionario.place(relx=0.07, rely=0.71, relwidth=0.4, relheight=0.2)

        # {=======================Botões de Visualização=========================}
        self.bt_visualizar_tabela = fun.CRIAR_BOTAO(self.frame_1,'Ultimos Registros','#258D19','#005200',4,'32','bold',"hand2")
        self.bt_visualizar_tabela.place(relx=0.5, rely=0.06, relwidth=0.4, relheight=0.2)
        
        self.bt_visualizar_site = fun.CRIAR_BOTAO(self.frame_1,'SITE COF','#4EA93B','#005200',4,'32','bold',"hand2")
        self.bt_visualizar_site.place(relx=0.5, rely=0.31, relwidth=0.4, relheight=0.2)
        
        # {=======================Botão Iniciar Inspecção=========================}
        self.bt_iniciar_camera = fun.CRIAR_BOTAO(self.frame_1,'Iniciar Inspecção','#71C55B','#005200',4,'32','bold',"circle", self.abinha2)
        self.bt_iniciar_camera.place(relx=0.5, rely=0.56, relwidth=0.4, relheight=0.35)

        # # {=======================Imagem IFES=========================}
        # self.img1_pg1 = tk.PhotoImage(file = 'ifes.png')
        # self.img1_pg1 = self.img1_pg1.subsample(5, 5)

        # self.fotoimg1_pg1 = tk.Label(self.frame_1,
        #                               bg= '#B4FF9A',
        #                               bd =0,
        #                               image = self.img1_pg1)
        # self.fotoimg1_pg1.place(relx=0.1, rely=0.23, anchor=CENTER)

print("\n\n", color.Fore.GREEN + "Iniciando o código - Tela do Menu" + color.Style.RESET_ALL)
APK() 
print(color.Fore.RED + "Finalizando o código - Tela do Menu" + color.Style.RESET_ALL, "\n")
