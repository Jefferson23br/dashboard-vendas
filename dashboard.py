import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de Vendas")

@st.cache_data
def load_data():
    df = pd.read_csv("vendas.csv", parse_dates=["Data"])
    return df

df = load_data()

st.sidebar.header("🔎 Filtros")
regiao = st.sidebar.multiselect("Selecione a região:", df["Região"].unique(), default=df["Região"].unique())
produto = st.sidebar.multiselect("Selecione o produto:", df["Produto"].unique(), default=df["Produto"].unique())

df_filtrado = df[(df["Região"].isin(regiao)) & (df["Produto"].isin(produto))]

st.metric("Total de Vendas", f'R$ {df_filtrado["Vendas"].sum():,.2f}')

fig1 = px.line(df_filtrado.groupby("Data")["Vendas"].sum().reset_index(), x="Data", y="Vendas", title="📈 Vendas ao longo do tempo")
st.plotly_chart(fig1)

fig2 = px.bar(df_filtrado.groupby("Região")["Vendas"].sum().reset_index(), x="Região", y="Vendas", title="📍 Vendas por Região")
st.plotly_chart(fig2)

fig3 = px.pie(df_filtrado, names="Produto", values="Vendas", title="📦 Distribuição por Produto")
st.plotly_chart(fig3)
