# import cv2

# def abrir_camera():
#     while True:
#         cap = cv2.VideoCapture(0)

#         ret, frame = cap.read()

#         # Exibe o frame capturado
#         cv2.imshow('Webcam', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#             # Libera os recursos e fecha as janelas
#     cap.release()
#     cv2.destroyAllWindows()

# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk

# def componentes_frame2(self):
#     frame = tk.Frame(janela2)
        
#     frame.pack()

#     label = tk.Label(frame) #.place(x=0,y=0,relwith=1, relheight=1)
#     label.pack(padx=(10, 10), pady=(10, 10))
    
    
#     cap = cv2.VideoCapture(2


#     def up():
#         ret,frame = cap.read()
#         if ret:
#             frame = cv2.resize(frame,(600,600))
            
#             img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             img = Image.fromarray(img)
            
#             imgtk = ImageTk.PhotoImage(image = img)
            
#             label.imgtk = imgtk
#             label.configure(image=imgtk)
#         janela2.after(10,up)

#     up()  

import cv2
import pyrealsense2
from realsense_depth import *
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

from datetime import datetime
from ultralytics import YOLO
import pandas as pd
from skimage.measure import regionprops
import math

#--------------- FUNCOES ---------------#
def analisar_imagem(image):
    modelo = YOLO(r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\best.pt')
    resultados = modelo.predict(image, conf=0.2)

    resultados_array = resultados[0].plot()
    resultados_array_bgr = cv2.cvtColor(resultados_array, cv2.COLOR_RGB2BGR)

    return resultados_array_bgr, resultados
''

def extrair_dados(resultados, nome):
    resultados = resultados[0]
    resultados.masks.xyn
    extracted_masks = resultados.masks.data
    resultados.masks.xy
    extracted_masks.shape

    # Converter tensor PyTorch para numpy
    masks_array = extracted_masks.cpu().numpy()

    classes_nomes = resultados.names.values()

    # Extrair caixas delimitadoras
    detected_boxes = resultados.boxes.data
    # Extrair classes a partir das caixas identificadas
    notas_classes = detected_boxes[:, -1].int().tolist()
    # Armazenando as mascaras por classes
    masks_by_class = {name: [] for name in resultados.names.values()}

    # Iterar pelas mascaras e rotulos de classe
    for mask, class_id in zip(extracted_masks, notas_classes):
        nome_classe = resultados.names[class_id] 
        masks_by_class[nome_classe].append(mask.cpu().numpy())

    bico_masks = masks_by_class['bico']
    furo_masks = masks_by_class['furo']

    props_lista = []
    i=-1
    # Iterar por todas as classes
    for nome_classe, masks in masks_by_class.items():
        for mask in masks:
            mask = mask.astype(int)
            props = regionprops(mask) # retorna uma lista de propriedades encontradas nas mascaras
            i+=1

            # Extrair propriedades
            for prop in props:
                area = prop.area
                diametro = prop.equivalent_diameter_area

                # Calcula a profundidade média na região de interesse em metros
                profundidade_media_metros = np.mean(depth_frame[mask])

                # Converte a profundidade média para milímetros usando o depth_scale
                profundidade_media_mm = profundidade_media_metros * depth_scale

                # Calcula a área em milímetros quadrados
                area_mm2 = area * profundidade_media_mm

                # Calcula o raio do círculo em centímetros
                raio_mm = math.sqrt(area_mm2 / math.pi)

                # Calcula o diâmetro do círculo em centímetros
                diametro_mm = 2 * raio_mm

                if i == 0:
                    props_lista.append({'Classe': f'{nome_classe}','Arquivo': nome,'Diametro[mm]': f'{diametro_mm:.2f}'})
                else:
                    props_lista.append({'Classe': f'{nome_classe} {i}','Arquivo': nome, 'Diametro[mm]': f'{diametro_mm:.2f}'})

    # Converter para DataFrame
    props_df = pd.DataFrame(props_lista)

    return props_df, masks_array, detected_boxes, resultados


# Função para extrair as coordenadas e centro das caixas delimitadoras
def extrair_coordenadas_centro(detected_boxes, classes_nomes):

    coordenadas_caixas = []
    pontos = []

    for box in detected_boxes:
        x1, y1, x2, y2, sla, classe = box.tolist()
        centro_x = int((x1 + x2) / 2)
        centro_y = int((y1 + y2) / 2)

        ponto = (centro_x, centro_y)
        pontos.append(ponto)
        
        coordenadas_caixas.append({
            'Classe': classes_nomes[int(classe)],
            'Centro': {
                'x': centro_x,
                'y': centro_y
            }
        })

        
    # Converter para DataFrame
    coordenadas_df = pd.DataFrame(coordenadas_caixas)
    
    return coordenadas_df, pontos

def salvar_dados(novos_dados, excel_filename):
        # Carregar o DataFrame existente da planilha Excel
        props_df = pd.read_excel(excel_filename)

        # Converter os novos dados em DataFrame
        novos_df = pd.DataFrame(novos_dados)

        # Adicionar novos dados ao DataFrame existente
        props_df = pd.concat([props_df, novos_df], ignore_index=True)

        # Salvar o DataFrame atualizado na planilha Excel
        props_df.to_excel(excel_filename, index=False)

        print(f'Novos dados adicionados com sucesso em {excel_filename}')



# -------- MAIN -------- #


# Iniciando a cameras
dc = DepthCamera()

num = int(input('Selecione o molde: \n1- Quatro furos \n2- Seis furos \nResposta: '))

if num == 1:
    overlay_image = cv2.imread(r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\molde2.png', cv2.IMREAD_UNCHANGED)
else:
    overlay_image = cv2.imread(r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\molde.png', cv2.IMREAD_UNCHANGED)

while True:

    ret, depth_frame, frame, depth_scale = dc.get_frame()

    back_frame = frame.copy()

    # Redimensionar a imagem se necessário
    overlay_image_resized = cv2.resize(overlay_image, (frame.shape[1], frame.shape[0]))

     # Definir a região de interesse (ROI) onde a imagem será sobreposta
    roi = back_frame[0:overlay_image_resized.shape[0], 0:overlay_image_resized.shape[1]]
    
    # Sobrepor a imagem na região de interesse
    for c in range(0, 3):
        roi[:, :, c] = overlay_image_resized[:, :, c] * (overlay_image_resized[:, :, 3] / 255.0) + roi[:, :, c] * (1.0 - overlay_image_resized[:, :, 3] / 255.0)
    
    # Obter as dimensões do frame
    altura, largura, _ = frame.shape

    # Calcular as coordenadas do ponto no meio do frame
    mid_x, mid_y = largura // 2, altura // 2
    ponto = (mid_x, mid_y)

    # Coordenadas do canto superior direito
    canto_superior_direito = (largura - 115, 30)

    # Mostrar a distancia de um ponto especifico
    cv2.circle(back_frame, ponto, 4, (0, 0, 255))
    distancia = depth_frame[ponto[1], ponto[0]]
    
    cv2.putText(back_frame, '{}cm'.format(distancia/10), canto_superior_direito, cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255))
    

    diretorio_destino = r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\fotos'
    
    agora = datetime.now()
    
    # Formatar a data e hora como parte do nome do arquivo
    nome_arquivo = agora.strftime('registro_%d-%m-%Y_%H.%M') + '.png'

    caminho_completo = os.path.join(diretorio_destino, nome_arquivo)


    # Aguardar a tecla 'q' para salvar o frame e encerrar o programa
    key = cv2.waitKey(1)
    if key == ord('q'):
        # Salvar o frame como imagem 
        cv2.imwrite(caminho_completo, frame)
        break

    cv2.imshow('Color frame', back_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break


print('Fotografia salva')


#img = cv2.imread(r'C:\Users\julia\OneDrive\Projetos\Projeto_IC\fotos\registro_06-03-2024_14.19.jpg')
img = cv2.imread(caminho_completo)

resultado, novos_resultados = analisar_imagem(img)

planilha = r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\arquivos\dados_bicos.xlsx'

dados, masks_array, detected_boxes, resultados = extrair_dados(novos_resultados, nome_arquivo)
x = salvar_dados(dados, planilha)

# Converter para lista 
nomes_classes = list(resultados[0].names.values())

print(dados)

# Converter para lista
nomes_classes = list(resultados[0].names.values())

# Extrair coordenadas e centro das caixas delimitadoras
coordenadas_df, lista = extrair_coordenadas_centro(detected_boxes, nomes_classes)

img_copia = resultado.copy()

# Adicionar texto à imagem para cada ponto
for i in range(1, len(lista)):
    imagem = cv2.putText(img_copia, f'{i}', lista[i], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


diretorio_destino = r'C:\Users\20211MPECA0020\Documents\Projeto\Aplicativo\guias'
nome_arquivo = agora.strftime('registro_%d-%m-%Y_%H.%M') + '.png'
caminho = os.path.join(diretorio_destino, nome_arquivo)

cv2.imwrite(caminho, imagem)

while True:

    cv2.imshow('Foto', img)
    cv2.imshow('Resultado', resultado)
    cv2.imshow('Imagem com Texto', imagem)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()