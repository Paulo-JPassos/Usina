import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Título do aplicativo
st.title("Correlação entre Usinas Hidrelétricas")

# Carregando o arquivo CSV
# Troque o caminho abaixo se necessário!

df = pd.read_csv('Usinas.csv', sep=';', encoding='latin1')

st.subheader("Primeiras linhas da base de dados:")
st.write(df.head())

# Seleção das colunas (usinas) para filtro
usinas = df.columns.tolist()
usinas_selecionadas = st.sidebar.multiselect("Selecione as usinas:", options=usinas)

if len(usinas_selecionadas) > 1:
    # Cálculo da matriz de correlação apenas para as usinas selecionadas
    correlacao = df[usinas_selecionadas].corr()

    st.subheader("Matriz de Correlação:")
    st.dataframe(correlacao)  # Exibe a matriz de correlação como dataframe

    # Opção de visualizar como mapa de calor
    st.subheader("Mapa de Calor (Heatmap) das Correlações")

    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(correlacao, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)
else:
    st.warning("Selecione pelo menos duas usinas para calcular a matriz de correlação.")