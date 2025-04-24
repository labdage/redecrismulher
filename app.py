
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='RedeCRIS Mulher', layout='wide')

st.title('RedeCRIS Mulher')
st.subheader('Conectando dados, pesquisas e políticas no enfrentamento à violência de gênero.')

df = pd.read_csv('base_geral.csv')

with st.sidebar:
    st.header('Filtros')
    grupo = st.selectbox('Grupo de Pesquisa', ['Todos'] + sorted(df['Grupo'].dropna().unique().tolist()))
    instituicao = st.selectbox('Instituição', ['Todas'] + sorted(df['Instituicao'].dropna().unique().tolist()))
    tema = st.selectbox('Tema', ['Todos'] + sorted(df['Tema'].dropna().unique().tolist()))
    ano = st.selectbox('Ano', ['Todos'] + sorted(df['Ano'].dropna().astype(str).unique().tolist()))

filtered = df.copy()
if grupo != 'Todos':
    filtered = filtered[filtered['Grupo'] == grupo]
if instituicao != 'Todas':
    filtered = filtered[filtered['Instituicao'] == instituicao]
if tema != 'Todos':
    filtered = filtered[filtered['Tema'] == tema]
if ano != 'Todos':
    filtered = filtered[filtered['Ano'].astype(str) == ano]

st.dataframe(filtered)

st.subheader('Distribuição Geográfica')
if 'UF' in filtered.columns:
    mapa = filtered.groupby('UF').size().reset_index(name='Contagem')
    fig = px.choropleth(locations=mapa['UF'], locationmode='ISO-3166-2', color=mapa['Contagem'],
                        scope='south america', title='Produção por UF')
    st.plotly_chart(fig, use_container_width=True)
