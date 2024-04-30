import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings 
from PIL import Image
from datetime import datetime
import locale

warnings.filterwarnings("ignore")  # ->ignorar os erros que aparecem no site

# {=======================Estilos da página=========================}

st.set_page_config(page_title= "Registros de Bico",page_icon=":clipboard:", layout="wide")  #->Titulo da aba no navegador
page_bg_img =""" <style>
[data-testid="stAppViewContainer"] {
             background-color: #eaf7e9;
             }

             [data-testid="stHeader"] {
             background-color: rgba(0,0,0,0);
             }

             [data-testid="stSidebar"]{
             background-image: url("https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm00MjItMDQ3LWtxOTJ3eDl5LmpwZw.jpg");
             background-size: cover;
             }
             </style>"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# {=======================Imagens=========================}

image_4F = Image.open('./4Furos.jpeg')
image_5F = Image.open('./5Furos.jpeg')
image_6F = Image.open('./6Furos.jpeg') 
# imagem_IFES = Image.open('./ifes.png')
# imagem_LUMAR = Image.open('./LUMAR2.png')
# imagem_ARCELOR = Image.open('./arcelormittal.png')
imagem_LOGOS = Image.open('./LOGOS.png')

# {=======================Título=========================}

st.title("Registros de Desgaste de Furo de Lança de Convertedores LD")
st.markdown('<style>div.block-container{padding-top:1rem;}</> ',unsafe_allow_html=True)

# {=======================Leitura de arquivo=========================}

os.chdir(r"C:\Users\20221CECA0402\Documents\Projeto_WRL\Site_WRL")
df = pd.read_csv("plan.csv", encoding = 'ISO-8859-1')

# {=======================Barra de seleção=========================}

st.sidebar.header("Seja bem-vindo :bangbang:")

pais = st.sidebar.multiselect("Pais:", df["PAIS"].unique(),placeholder="")
if not pais:
    df2 = df.copy()
else:
    df2 = df[df["PAIS"].isin(pais)]

grupo = st.sidebar.multiselect("Grupo:", df2["GRUPO"].unique(),placeholder="")
if not grupo:
    df3 = df2.copy()
else:
    df3 = df2[df["GRUPO"].isin(grupo)]

limite = 1
site = st.sidebar.multiselect("Site:".format(limite), df3["SITE"].unique(),placeholder="Selecione apenas um site")
if not site:
    df4 = df3.copy()

else:
    aviso_site = site
    site = site[:limite]
    df4 = df3[df["SITE"].isin(site)]

    if len(aviso_site) > limite:
        st.sidebar.warning("Selecione no máximo uma opção de site")

st.sidebar.image(imagem_LOGOS, width= 270) 

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_atual = datetime.today()
data_formatada = data_atual.strftime("%d de %B de %Y - %H:%M")
st.sidebar.write(data_formatada)

# {=======================Filtro baseado na região, estado e cidade=========================}

if not pais and not grupo and not site:
    filtered_df = df

elif not grupo and not site:
    filtered_df = df[df["PAIS"].isin(pais)]
elif not pais and not site:
    filtered_df = df[df["GRUPO"].isin(grupo)]

elif grupo and site:
    filtered_df = df4[df["GRUPO"].isin(grupo) & df4["SITE"].isin(site)]
elif pais and site:
    filtered_df = df4[df["PAIS"].isin(pais) & df4["SITE"].isin(site)]
elif pais and grupo:
    filtered_df = df4[df["PAIS"].isin(pais) & df4["GRUPO"].isin(grupo)]

elif site:
    filtered_df = df4[df4["SITE"].isin(site)]
else:
    filtered_df = df4[df4["PAIS"].isin(pais) & df4["GRUPO"].isin(grupo) & df4["SITE"].isin(site)]

# {=======================Texto na página=========================}

st.markdown('''<div style="text-align: justify;">
            <H4>Este projeto existe para monitorar o nível de desgaste nos furos do bico de lança do convertedor LD.
            Este problema é um risco para o desempenho e segurança deste processo, ocasionando paradas, contaminação 
            ambiental e riscos para os operadores, causando assim grandes prejuízos.
            </H4></div>
            ''', unsafe_allow_html= True)

st.markdown(""" <div style="text-align: justify;">
            <H4>Os moldes das lanças possuem este formato circular, onde cada diâmetro sofre variações conforme o seu uso.
            A indústria dispõe de alguns moldes. Verifique as fotografias: 
            </H4></div>
            
            """, unsafe_allow_html=True )

col1, col2, col3 = st.columns([4, 4, 4])
with col1:
    st.image(image_4F, caption='Lança de Quatro Furos', width= 280, output_format='auto')
with col2:
    st.image(image_5F, caption='Lança de Cinco Furos', width= 280, output_format='auto')
with col3:
    st.image(image_6F, caption='Lança de Seis Furos', width= 280, output_format='auto')

st.divider()

# {=======================Informações com a pré-seleção=========================}

if site:
    # {=======================Gráfico principal=========================}

    st.markdown(f"<H3 style='text-align: center; color: gray;'>Variação dos diâmetros: {', '.join(site)} </H3>" , unsafe_allow_html=True)

    filtered_df = df4[df4["SITE"].isin(site)]
    teste = filtered_df.groupby(['BICO','VIDA'])['MEDIDA'].sum().reset_index()

    fig = px.line(teste,
                x = "VIDA",
                y= "MEDIDA",
                template = "seaborn",
                markers=True,
                color = 'BICO')

    st.plotly_chart(fig,use_container_width=True, height=200, width="100%")
    st.divider()
    
    st.markdown(f"# País: {', '.join(pais)} - Grupo: {', '.join(grupo)} - Site: {', '.join(site)}")
    
    bico = st.selectbox("BICO",df4["BICO"].unique() )
    if not bico:
        df5 = df4.copy()
    else:
        df5 = df4[df4["BICO"].isin([bico])]

    # {=======================Gráfico secundário=========================}

    filtered_df = df5[df5["SITE"].isin(site) & df5["BICO"].isin([bico])]
    fig = px.line(filtered_df,
                  x = "VIDA",
                  y= "MEDIDA",
                  template = "seaborn",
                  markers=True,
                  title=' Registros dos bicos')
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig,use_container_width=True, height=200, width="100%")

else:
    st.markdown("<H3 style='color:red'>Selecione Site </H3>" , unsafe_allow_html=True)
    

# {=======================Seleção de datas=========================}

st.caption('Este é um Projeto desenvolvido por alunos do **IFES** que terá utilidades para a empresa **ArcelorMITTAL**')