# page_bg_img =""" <style>
#              [data-testid="stAppViewContainer"] {
#              background-color: #e5e5f7;
#              background-image: repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 23px ), repeating-linear-gradient( #c7e5bf55, #c7e5bf );}

#              [data-testid="stHeader"] {
#              background-color: rgba(0,0,0,0);
#              }

#              [data-testid="stSidebar"]{
#              background-image: url("https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm00MjItMDQ3LWtxOTJ3eDl5LmpwZw.jpg");
#              background-size: cover;
#              }
#              </style>"""

# page_bg_img =""" <style>
#              [data-testid="stAppViewContainer"] {
#              background-image:url("https://i.pinimg.com/originals/3d/a7/53/3da753c069cc528443dc798630ad5bdb.jpg");
#              background-size: cover;
#              }
             
#              [data-testid="stHeader"] {
#              background-color: rgba(0,0,0,0);
#              }

#              [data-testid="stToolbar"] {
#              right: 2rem;
#              }

#              [data-testid="stSidebar"]{
#              background-image: url("https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm00MjItMDQ3LWtxOTJ3eDl5LmpwZw.jpg");
#              background-size: cover;
#              }
#              </style>"""


# st.markdown('[Isso é um texto com html](https://docs.streamlit.io/en/stable/api.html#display-text)',False)

#new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">New image</p>'
#st.markdown(new_title, unsafe_allow_html=True)

# {=======================Seleção de datas=========================}

# col1, col2 = st.columns((2))

# df["Order Date"] = pd.to_datetime(df["DATA"])

# startDate = pd.to_datetime(df["Order Date"]).min()
# endDate = pd.to_datetime(df["Order Date"]).max()

# with col1:
#     date1 = pd.to_datetime(st.date_input("Data de início", startDate))

# with col2:
#     date2 = pd.to_datetime(st.date_input("Data final", endDate))

#     df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)]. copy()





# if not pais and not grupo and not site:
#     filtered_df = df

# elif not grupo and not site:
#     filtered_df = df[df["PAIS"].isin(pais)]
# elif not pais and not site:
#     filtered_df = df[df["GRUPO"].isin(grupo)]

# elif grupo and site:
#     filtered_df = df3[df["GRUPO"].isin(grupo) & df3["SITE"].isin(site)]
# elif pais and site:
#     filtered_df = df3[df["PAIS"].isin(pais) & df3["SITE"].isin(site)]
# elif pais and grupo:
#     filtered_df = df3[df["PAIS"].isin(pais) & df3["GRUPO"].isin(grupo)]

# elif site:
#     filtered_df = df3[df3["SITE"].isin(site)]
# else:
#     filtered_df = df3[df3["PAIS"].isin(pais) & df3["GRUPO"].isin(grupo) & df3["SITE"].isin(site)]

# ============================modelo de TEXTO================================
# st.markdown(""" Este é um Projeto desenvolvido por alunos do IFES <span style = 'color:green;'>IFES</span>
#     Que terá utilidades para a empresa **ArcelorMITTAL**.
    
#     > O que varia nos bicos?
            
#     - Quantidade;
#     - Diâmetro;
#     - Vidas.
#     """,
#     unsafe_allow_html=True)