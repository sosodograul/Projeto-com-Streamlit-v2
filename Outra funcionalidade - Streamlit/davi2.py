import streamlit as st

st.set_page_config(
 page_title="Projetode estilização do Streamlit",
 page_icon="",
layout="wide"
)

st.title="Projeto de estilização do streamlit"
st.subheader="Exemplo de como organizar e estilizar um app"


st.sidebar.header("filtros")
st.sidebar.checkbox("ativar tema escuro", key="tema")
st.sidebar.slider("Selecionar valor",0,100,25 )

st.metric("vendas", "R$ 50.000", "+5%")
st.metric("Usuários", "1.200", "-2%")

col1, col2, col3=st.columns(3)

with col1:
    st.header("Coluna 1")
    st.success("Tudo certo")
    st.button("Clique aqui!")

with col1:
    st.header("Coluna 2")    
    st.warning("Atenção!")
    st.radio("Escolha uma alternativa", ["opção A", "opção B", "opção C"])

with col1:
    st.header("Coluna 3")
    st.info("Informação útil")
    st.selectbox("Escolha um item", ["item 1", "item 2", "item 3"])

    # Expander
with st.expander("Clique para ver mais detalhes"):
 st.write("Aqui dentro você pode colocar informações adicionais, gráficos ou tabelas.")
 st.checkbox("Ativar detalhe extra")
 st.text_input("Digite algo interessante")

# Cores e Markdown
st.markdown(
"""
<div style='background-color: #f9f9f9; padding: 10px; border-radius: 10px'>
<h4 style='color: #FF5733;'>Texto colorido com estilo personalizado</h4>
</div>
""",
unsafe_allow_html=True
)

# Rodapé
st.markdown("---")
st.markdown("💡 Exemplo simples de estilização no Streamlit sem lógica complexa")
