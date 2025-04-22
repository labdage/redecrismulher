
import streamlit as st
import json

st.set_page_config(page_title="RedeCRIS Mulher", layout="wide")

st.title("🔍 RedeCRIS Mulher")
st.markdown("Sistema de informação sobre pesquisas e pesquisadores(as) que atuam no enfrentamento à violência contra a mulher no Brasil.")

# Carregar dados
with open("redecris_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Pesquisadores
st.header("👩‍🔬 Pesquisadores(as)")
for pesq in data["pesquisadores"]:
    st.subheader(pesq["nome"])
    st.markdown(f"**Instituição:** {pesq['instituicao']}")
    st.markdown(f"**Linha de pesquisa:** {pesq['linha_de_pesquisa']}")
    st.markdown(f"[Ver ORCID]({pesq['link_orcid']})", unsafe_allow_html=True)
    st.markdown("---")

# Grupos de Pesquisa
st.header("🏛️ Grupos de Pesquisa")
for grupo in data["grupos_de_pesquisa"]:
    st.subheader(grupo["nome"])
    st.markdown(f"**Instituição:** {grupo['instituicao']}")
    st.markdown(f"[Acessar link oficial]({grupo['link']})", unsafe_allow_html=True)
    st.markdown("---")
