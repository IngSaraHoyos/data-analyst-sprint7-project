import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Proyecto Sprint 7')

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')

if hist_button:
    
    st.write('Histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, width='stretch')
    