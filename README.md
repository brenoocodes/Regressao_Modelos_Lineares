# Regressão e Modelos Lineares

Este repositório contém uma coleção de estudos, experimentos e aplicações práticas focados em algoritmos de **Regressão Linear**, expansão de **Features Polinomiais** e técnicas de **Regularização** (Ridge, Lasso, ElasticNet) utilizando a biblioteca Scikit-Learn.

O objetivo principal é explorar o ciclo de vida de um projeto de ciência de dados, desde a análise exploratória até o deploy de um modelo preditivo.

## 📁 Estrutura do Repositório

O projeto está organizado em módulos que cobrem diferentes aspectos do aprendizado supervisionado linear:

*   **`projeto/`**: Módulo principal contendo a análise completa do dataset de preços de casas da Califórnia:
    *   `notebooks/`:
        *   `01_analises_iniciais_e_tratamento.ipynb`: Análise exploratória (EDA), tratamento de outliers e limpeza dos dados.
        *   `02_mapas_com_plotly.ipynb`: Visualização geoespacial interativa dos dados de habitação.
        *   `03_ml_linear_regression.ipynb` & `04_ml_linear_regression.ipynb`: Implementação de modelos baseline de Regressão Linear.
        *   `05_ml_elasticnet.ipynb`: Experimentos com regularização ElasticNet.
        *   `06_ml_ridge.ipynb`: Modelo final utilizando Regressão Ridge com expansão polinomial.
    *   `home.py`: Interface interativa desenvolvida com **Streamlit** para realizar previsões de preços em tempo real.
    *   `src/`: Scripts auxiliares de configuração, gráficos e modelos.
*   **`Regressão com Scikit-Learn - algoritmos lineares/`**: Estudos iniciais sobre os fundamentos da regressão linear e pipelines.
*   **`Regressao Polimonial/`**: Experimentos focados em capturar relações não-lineares através da expansão de atributos.
*   **`Regularizacao/`**: Implementação e comparação de modelos com penalidades L1 e L2 para evitar overfitting e seleção de atributos.

## 📊 Dataset Principal

A maioria das análises utiliza o dataset **California Housing Prices** (Censo dos EUA de 1990). O objetivo é prever o valor mediano das casas (`median_house_value`) com base em características como:
*   Renda mediana do bloco (`median_income`).
*   Idade média das casas (`housing_median_age`).
*   Localização geográfica (`latitude`, `longitude`).
*   Proximidade com o oceano (`ocean_proximity`).

## 🛠️ Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Manipulação de Dados:** Pandas, NumPy
*   **Visualização:** Plotly, Seaborn, Matplotlib
*   **Machine Learning:** Scikit-Learn, Joblib
*   **Deploy/Interface:** Streamlit

## 🚀 Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-repositorio>
    cd Regressao_Modelos_Lineares
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No Linux/Mac:
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run projeto/home.py
    ```

---
*Este projeto foi desenvolvido com base em modelos de referência para ensino de ciência de dados.*
