import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

from joblib import load
from notebooks.src.config import DADOS_GEO_MEDIAN, DADOS_LIMPOS, MODELO_FINAL

@st.cache_data
def carregar_data():
    return pd.read_parquet(DADOS_LIMPOS), pd.read_parquet(DADOS_GEO_MEDIAN)

@st.cache_resource
def carregar_modelo():
    return load(MODELO_FINAL)

df, df_per_city = carregar_data()
modelo = carregar_modelo()

st.title('Previsão de preços de imóveis')

condados = list(df_per_city['city'].sort_values())

condado = st.selectbox(label='Selecione o condado', options=condados)

longitude = df_per_city.query("city == @condado")['longitude'].values
latitude = df_per_city.query("city == @condado")['latitude'].values

housing_median_age = st.number_input("Idade do imóvel", value=10, min_value=1, max_value=50)

total_rooms = df_per_city.query("city == @condado")['total_rooms'].values
total_bedrooms = df_per_city.query("city == @condado")['total_bedrooms'].values
population = df_per_city.query("city == @condado")['population'].values
households = df_per_city.query("city == @condado")['households'].values

median_income = st.slider(label="Renda média (milhares de US$)", min_value=5.0, max_value=100.0, value=45.0, step=5.0)

ocean_proximity = df_per_city.query("city == @condado")['ocean_proximity'].values

bins = [0, 1.5, 3, 4.5, 6, np.inf]
median_income_cat = np.digitize(median_income / 10, bins=bins)

rooms_per_household = total_rooms / households
population_per_household = population / households
bedroomns_per_room = total_bedrooms / total_rooms

entrada_modelo = {
    "longitude": longitude,
    "latitude": latitude,
    "housing_median_age": housing_median_age,
    "total_rooms": total_rooms,
    "total_bedrooms": total_bedrooms,
    "population": population,
    "households": households,
    "median_income": median_income / 10,
    "ocean_proximity": ocean_proximity,
    "median_income_cat": median_income_cat,
    "rooms_per_household": rooms_per_household,
    "population_per_household": population_per_household,
    "bedroomns_per_room": bedroomns_per_room
}

df_entrada_modelo = pd.DataFrame(entrada_modelo, index=[0])

botao_previsao = st.button(label='Prever preço')

if botao_previsao:
    preco = modelo.predict(df_entrada_modelo)
    st.write(f'O preço previsto é US${preco[0][0]:.2f}.')