import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Dashboard de Anúncios de Carros')

car_data = pd.read_csv('vehicles.csv')

build_histogram = st.button('Criar Histograma')

if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de aanúncios de vendas de carros')

    fig = px.histogram(car_data, x='odometer')

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.button('Criar Gráfico de Dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Relação entre Quilometragem e Preço', labels={'odometer': 'Quilometragem', 'price': 'Preço (USD)'}, opacity=0.5)
    
    st.plotly_chart(fig_scatter, use_container_width=True)


