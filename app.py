import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Proyecto Sprint 7')

st.write('Por favor marca las casillas de los tipos de gráficos quieres generar.')

car_data = pd.read_csv('vehicles_us.csv')

hist_selection = st.checkbox('Construir histograma')
scatter_selection = st.checkbox('Construir gráfico de dispersión')

button_generate = st.button('Generar')

if button_generate:

    if hist_selection:
    
        st.write('Histograma para el conjunto de datos de anuncios de venta de coches')

        fig = px.histogram(car_data, x="odometer")

        st.plotly_chart(fig, width='stretch')
    
    if scatter_selection:
    
        st.write('Gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

        fig2 = px.scatter(car_data, x="odometer")

        st.plotly_chart(fig2, width='stretch')