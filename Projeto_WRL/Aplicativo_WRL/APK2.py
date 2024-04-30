import tkinter as tk
import colorama as color
# import cv2
# import imutils
# import pyrealsense2
# import os
# os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
# import pandas as pd
# import math

from tkinter.constants import *
from tkinter import ttk
from tkinter import messagebox
# from customtkinter import *
# from PIL import Image, ImageTk
# from realsense_depth import *
# from datetime import datetime
# from ultralytics import YOLO
# from skimage.measure import regionprops

janela2 = tk.Tk()
video = None


def tela(): # {=======================Configuração de tela=========================}
    janela2.title("Where Register Lances (WRL)")
    janela2.configure(background= '#9BCD9B')
    janela2.geometry("1600x900")
    janela2.resizable(True, True) #se quiser impedir que amplie ou diminua a tela, altere para False
    # janela2.maxsize(width=1920, height=1080) #limite máximo da tela
    janela2.minsize(width=700, height=450) #limite minimo da tela

def frame_1():
    # {=======================Frame da Direita=========================}
    frame_um = tk.Frame(janela2, bd=2,
                            bg= '#B4EEB4',
                            highlightbackground= '#668B8B', 
                            highlightthickness=1)
    frame_um.place(relx=0.72, rely=0.02,relwidth=0.27, relheight=0.96)
    return frame_um

def frame_2():
    # {=======================Frame da Esquerda=========================}
    frame_dois = tk.Frame(janela2, bd=2,
                            bg= '#B4EEB4',
                            highlightbackground= '#668B8B', 
                            highlightthickness=1)
    frame_dois.place(relx=0.01, rely=0.02,relwidth=0.7, relheight=0.96)
    return frame_dois


def componentes_frame1():
    # {=======================Botão Voltar=========================}
    btvoltar_pg2 = tk.Button(frame_1(),
                            text='Voltar',
                            relief = "raised",
                            cursor = "hand2",
                            bd = 3,
                            bg = '#545454',
                            fg = 'white',
                            font= ("arial", 13))
    btvoltar_pg2.place(relx=0.7, rely=0.02, relwidth=0.25, relheight=0.05)
    
    # {=======================Message box=========================}
    # messagebox.showinfo(title = "",message="OIOI")
    
    
    
    
    
    # {=======================Botão Foto=========================}
    # image_btfoto_pg2 = tk.PhotoImage(file = "fotoclick.png")
    # image_btfoto_pg2 = image_btfoto_pg2.subsample(1, 2)

    btfoto_pg2 = tk.Button(frame_1(),
                                text='Click',
                                relief = "ridge",
                                cursor = "circle",
                                bd = 4,
                                bg = '#545454',
                                fg = 'white',
                                font= ("arial", 13)
                                #   image = image_btfoto_pg2
                                )
    btfoto_pg2.place(relx=0.5, rely=0.93, anchor=CENTER)

    # def componentes_frame2(:

    #     label = tk.Label(frame_2()).place(x=5,y=5,relwidth=0.99, relheight=0.985)
        
    #     marcador_cima = tk.Label(frame_2(),bg="black")
    #     marcador_cima.place(x=5,y=5)
        
    #     dc = DepthCamera()

    #     # num = int(input('Selecione o molde: \n1- Quatro furos \n2- Seis furos \nResposta: '))

    #     # if num == 1:
    #     overlay_image = cv2.imread(r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\molde2.png', cv2.IMREAD_UNCHANGED)
    #     # else:
    #     #     overlay_image = cv2.imread(r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\molde.png', cv2.IMREAD_UNCHANGED)

    #     while True:

    #         ret, depth_frame, frame, depth_scale = dc.get_frame()

    #         back_frame = frame.copy()

    #         # Redimensionar a imagem se necessário
    #         overlay_image_resized = cv2.resize(overlay_image, (frame.shape[1], frame.shape[0]))

    #         # Definir a região de interesse (ROI) onde a imagem será sobreposta
    #         roi = back_frame[0:overlay_image_resized.shape[0], 0:overlay_image_resized.shape[1]]
            
    #         # Sobrepor a imagem na região de interesse
    #         for c in range(0, 3):
    #             roi[:, :, c] = overlay_image_resized[:, :, c] * (overlay_image_resized[:, :, 3] / 255.0) + roi[:, :, c] * (1.0 - overlay_image_resized[:, :, 3] / 255.0)
            
    #         # Obter as dimensões do frame
    #         altura, largura, _ = frame.shape

    #         # Calcular as coordenadas do ponto no meio do frame
    #         mid_x, mid_y = largura // 2, altura // 2
    #         ponto = (mid_x, mid_y)

    #         # Coordenadas do canto superior direito
    #         canto_superior_direito = (largura - 115, 30)

    #         # Mostrar a distancia de um ponto especifico
    #         cv2.circle(back_frame, ponto, 4, (0, 0, 255))
    #         distancia = depth_frame[ponto[1], ponto[0]]
            
    #         cv2.putText(back_frame, '{}cm'.format(distancia/10), canto_superior_direito, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))
            

    #         diretorio_destino = r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\fotos'
            
    #         agora = datetime.now()
            
    #         # Formatar a data e hora como parte do nome do arquivo
    #         nome_arquivo = agora.strftime('registro_%d-%m-%Y_%H.%M') + '.png'

    #         caminho_completo = os.path.join(diretorio_destino, nome_arquivo)


    #         # Aguardar a tecla 'q' para salvar o frame e encerrar o programa
    #         key = cv2.waitKey(1)
    #         if key == ord('q'):
    #             # Salvar o frame como imagem 
    #             cv2.imwrite(caminho_completo, frame)
    #             break

    #         # cv2.imshow('Color frame', back_frame)
    #         # key = cv2.waitKey(1)
    #         # if key == 27:
    #         #     break
    #     #-------------------------------------------------

    #     def up():
           
            
    #             # frame = imutils.resize(frame,width=1000)
    #             # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                
    #             img = Image.fromarray(back_frame)
    #             imagetk = ImageTk.PhotoImage(image=img)
                
    #             marcador_cima.configure(image = imagetk)
    #             marcador_cima.image = imagetk
    #             marcador_cima.after(10,up)

    #     up() 
        
     
    
def inicio():
    tela()
    # frames_da_tela()
    componentes_frame1()
    # componentes_frame2()
    janela2.mainloop()

print("\n\n", color.Fore.GREEN + "Iniciando o código - Tela da câmera" + color.Style.RESET_ALL)
inicio()
print(color.Fore.RED + "Finalizando o código - Tela da câmera" + color.Style.RESET_ALL, "\n")