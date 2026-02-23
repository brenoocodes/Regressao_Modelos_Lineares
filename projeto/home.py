import streamlit as st
import pandas as pd
import plotly.express as px

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

longitude = st.number_input(label='Longitude', value=-122.33)
latitude = st.number_input(label='Latitude', value=37.33)

housing_median_age = st.number_input("Idade do imóvel", value=10)

total_rooms = st.number_input("Total de cômodos", value=800)
total_bedrooms = st.number_input("Total de quartos", value=100)
population = st.number_input("População", value=300)
households = st.number_input("Domicílios", value=800)

median_income = st.slider(label="Renda média (múltiplos de US$ 10k)", min_value=0.5, max_value=15.0, value=4.5, step=0.5)

ocean_proximity = st.selectbox(label="Proximidade do oceano", options=df['ocean_proximity'].unique())

median_income_cat = st.slider(label="Renda média categoria", min_value=1.0, max_value=5.0, value=2.0, step=1.0)
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
    "median_income": median_income,
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