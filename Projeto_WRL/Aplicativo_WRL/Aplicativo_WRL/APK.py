from tkinter import ttk
import tkinter as tk
import sqlite3 as sql
import colorama as color
from customtkinter import *
from PIL import Image, ImageTk

"""Linha de raciocinio:
Antes de tirar a foto o funcionaria já informou o ID, que nele já esta contido Furos,
Grupo, SIte e BOF. Sendo assim, nesta aba, o Grupo, site e bof estão com seu ID, e os 
Registros estarão vindo do banco de dados.
"""
janela = tk.Tk()
pasta = r'C:\Users\20221CECA0402\Documents'
class Tabela_DADOS_EMPRESA: # {=======================Comando para o Banco de Dados=========================}
    def conecta_bd(self):
            self.conn = sql.connect(r"C:\Users\20221CECA0402\Documents\Projeto_WRL\BD_WRL\REGISTROS_WRL.db")
            self.cursor = self.conn.cursor(); print("Conectando ao banco de dados\n")
    
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    
    def selecao(self): # {=========Leitura Grupo, SIte, BOF e ID(FRAME 1)=========}
        self.conecta_bd()
        self.cursor.execute("SELECT * FROM DADOS_EMPRESAS WHERE ID = '001' ")
        self.dados = self.cursor.fetchone()
        self.desconecta_bd()
        
        grupo_completo = self.dados[0]
        lista_grupo = grupo_completo.split('/')
        
        self.grupo = lista_grupo[0]
        self.site = self.dados[1]
        self.BOF = self.dados[2]
        self.tipo = self.dados[3]
        self.ID = self.dados[4]

class Tabela_REGISTROS_MEDICOES():
    def conecta_bd(self):
        self.conn = sql.connect(fr"{pasta}\Projeto_WRL\BD_WRL.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados\n")
    
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando do banco de dados")
    
    
    def tabela(self): # {=========Informações da tabela(FRAME 2)=========}
        self.conecta_bd()
        comando = f"SELECT * FROM B6 WHERE ID = '{self.ID}' "
        self.cursor.execute(comando)
        self.dados2 = self.cursor.fetchone()
        self.desconecta_bd()
        
        self.usuario = self.dados2[0]
        self.vida = self.dados2[1]
        self.registro_foto = self.dados2[4]
        self.data_foto = self.dados2[5]
        self.hora_foto = self.dados2[6]
        self.medidas_foto = self.dados2[7:]
        # self.dados2_filtrados = [resultado[2:] for resultado in self.dados2]
    
    def imagens(self):  # {=========Informações para imagens(FRAME 2)=========}
        self.endereco_pastafotos = fr"{pasta}\Projeto_WRL\Aplicativo_WRL\fotos"
        self.endereco_pastaguias = fr"{pasta}\Projeto_WRL\Aplicativo_WRL\guias"
        self.local_image = '\\'+ self.registro_foto
        #self.local_image = '\\'+ self.dados2[0][2] #+'.png'   (esta linha caso for usar '.fetchall' no 'def tabela' assim fazendo uma tupla e não uma lista)
            
        self.arquivofoto = self.endereco_pastafotos +'\\' +self.local_image
        self.arquivoguia = self.endereco_pastaguias +'\\' +self.local_image
        print(self.arquivofoto)
class APK(Tabela_DADOS_EMPRESA,Tabela_REGISTROS_MEDICOES):
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames_da_tela()
        self.selecao()
        self.tabela()
        self.imagens()
        self.componentes_frame1()
        self.componentes_frame2()
        janela.mainloop()
    
    def tela(self): # {=======================Configuração de tela=========================}
        self.janela.title("Where Register Lances (WRL)")
        self.janela.configure(background= '#9BCD9B')
        self.janela.geometry("1280x700")
        self.janela.resizable(True, True) #se quiser impedir que amplie ou diminua a tela, altere para False
        # self.janela.maxsize(width=1920, height=1080) #limite máximo da tela
        self.janela.minsize(width=700, height=450) #limite minimo da tela
    
    def frames_da_tela(self): 
        # {=======================Frame da Direita=========================}
        self.frame_1 = tk.Frame(self.janela, bd=2,
                                bg= '#B4EEB4',
                                highlightbackground= '#668B8B', 
                                highlightthickness=1)
        self.frame_1.place(relx=0.4, rely=0.02,relwidth=0.59, relheight=0.96)
        
        # {=======================Frame da Esquerda=========================}
        self.frame_2 = tk.Frame(self.janela, bd=2,
                                bg= '#B4EEB4',
                                highlightbackground= '#668B8B', 
                                highlightthickness=1)
        self.frame_2.place(relx=0.01, rely=0.02,relwidth=0.38, relheight=0.96)

    def componentes_frame1(self):
        # {=======================Título=========================}
        self.titulo1_pg1 = tk.Label(self.frame_1,
                                    text="Dados do Bico",
                                    font=('arial', '25', 'bold'),
                                    bg= '#B4EEB4',
                                    fg="#2F4F4F")
        self.titulo1_pg1.place(relx=0.32, rely=0.03)
        
        # {=======================Grupo=========================}
        self.grupo_pg1 = tk.Label(self.frame_1,
                                    text="Grupo:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.grupo_pg1.place(relx=0.05, rely=0.15)

        self.grupo_pg1 = tk.Label(self.frame_1,
                                    text=self.grupo,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.grupo_pg1.place(relx=0.2, rely=0.15)

        # {=======================Site=========================}
        self.site_pg1 = tk.Label(self.frame_1,
                                    text="Site:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.site_pg1.place(relx=0.05, rely=0.25)

        self.site_pg1 = tk.Label(self.frame_1,
                                    text=self.site,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.site_pg1.place(relx=0.15, rely=0.25)

        # {=======================BOF=========================}
        self.BOF_pg1 = tk.Label(self.frame_1,
                                    text="BOF:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.BOF_pg1.place(relx=0.05, rely=0.35)

        self.site_pg1 = tk.Label(self.frame_1,
                                    text=self.BOF,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.site_pg1.place(relx=0.15, rely=0.35)
        
        # {=======================ID=========================}
        self.ID_pg1 = tk.Label(self.frame_1,
                                    text="ID:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_pg1.place(relx=0.05, rely=0.45)

        self.ID_informado_pg1 = tk.Label(self.frame_1,
                                    text = self.ID,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_informado_pg1.place(relx=0.12, rely=0.45)
        
        # {=======================Data=========================}
        self.ID_pg1 = tk.Label(self.frame_1,
                                    text="Data:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_pg1.place(relx=0.05, rely=0.55)

        self.ID_informado_pg1 = tk.Label(self.frame_1,
                                    text = self.data_foto,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_informado_pg1.place(relx=0.17, rely=0.55)
        
        # {=======================Hora=========================}
        self.ID_pg1 = tk.Label(self.frame_1,
                                    text="Hora:",
                                    font=('verdana', '20','bold'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_pg1.place(relx=0.05, rely=0.65)

        self.ID_informado_pg1 = tk.Label(self.frame_1,
                                    text = self.hora_foto,
                                    font=('verdana', '20'),
                                    bg= '#B4EEB4',
                                    fg="#1C1C1C")
        self.ID_informado_pg1.place(relx=0.17, rely=0.65)
        
        # {=======================Registros=========================}

        self.tabela_pg1 = ttk.Treeview(self.frame_1, height=10,column=("col1", "col2"),style="mystyle.Treeview")

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Verdana', 14,'bold'))
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Verdana', 12))

        self.tabela_pg1.heading("#0", text="")
        self.tabela_pg1.heading("#1", text="Classe")
        self.tabela_pg1.heading("#2", text="Diametro(px)")
        
        self.tabela_pg1.column("#0", width=1)
        self.tabela_pg1.column("#1", width=180)
        self.tabela_pg1.column("#2", width=200)
       
        cont = 0
        for dado in self.medidas_foto:
            if cont == 0:
                self.tabela_pg1.insert("", tk.END, values=('Bico', dado))
            else:
                self.tabela_pg1.insert("", tk.END, values=(f'Furo {cont}', dado))
            cont += 1
                    
        self.tabela_pg1.place(relx=0.45, rely=0.15, relwidth=0.5, relheight=0.7)

        # self.scroolLista = tk.Scrollbar(self.frame_1, orient ='vertical')
        # self.tabela_pg1.configure(yscroll = self.scroolLista.set)
        # self.scroolLista.place(relx=0.93, rely=0.15, relwidth=0.03, relheight=0.7)
        
        # {=======================Botão Repetir=========================}
        self.btRepetir_pg1 = tk.Button(self.frame_1,
                                      text='Repetir',
                                      cursor = "exchange",
                                      bd = 4,
                                      bg = '#545454',
                                      fg = 'white',
                                      font= ("arial", 13,'bold'))
        self.btRepetir_pg1.place(relx=0.35, rely=0.9, relwidth=0.12, relheight=0.08)

        # {=======================Botão Continuar=========================}
        self.btContinuar_pg1 = tk.Button(self.frame_1,
                                      text='Continuar',
                                      cursor = "hand2",
                                      bd = 4,
                                      bg = '#545454',
                                      fg = 'white',
                                      font= ("arial", 13,'bold'))
        self.btContinuar_pg1.place(relx=0.55, rely=0.9, relwidth=0.12, relheight=0.08)

    
    def componentes_frame2(self): # {=========Componentes da direita=========}
        #  # {=======================Título=========================}
        # self.furos_pg1 = tk.Label(self.frame_2,
        #                             text = self.ID,
        #                             font = ('verdana', '23'),
        #                             bg = '#B4EEB4',
        #                             fg = "#2F4F4F")
        # self.furos_pg1.place(relx=0.32, rely=0.03)

        # {=======================Imagem 1=========================}
        self.img1_pg1 = tk.PhotoImage(file = self.arquivofoto)
        self.img1_pg1 = self.img1_pg1.subsample(2, 2)

        self.fotoimg1_pg1 = tk.Label(self.frame_2,
                                      bg= '#B4EEB4',
                                      bd =0,
                                      image = self.img1_pg1)
        self.fotoimg1_pg1.place(relx=0.5, rely=0.25, anchor=CENTER)
        

        # {=======================Imagem 2=========================}
        self.img2_pg1 = tk.PhotoImage(file = self.arquivoguia)
        self.img2_pg1 = self.img2_pg1.subsample(2, 2)

        self.fotoimg2_pg1 = tk.Label(self.frame_2,
                                      bg= '#B4EEB4',
                                      bd =0,
                                      image = self.img2_pg1)
        self.fotoimg2_pg1.place(relx=0.5, rely=0.7, anchor=CENTER)

        # {=======================WRL=========================}
        self.titulo2_pg1 = tk.Label(self.frame_2,
                                    text="Where Register Lances(WRL)",
                                    font=('italic', '18'),
                                    bg= '#B4EEB4',
                                    fg="#2F4F4F")
        self.titulo2_pg1.place(relx=0.01, rely=0.94)

print("\n\n", color.Fore.GREEN + "Iniciando o código - Dados do bico" + color.Style.RESET_ALL)

APK() 
print(color.Fore.RED + "Finalizando o código - Dados do bico" + color.Style.RESET_ALL, "\n")