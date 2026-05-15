# Importação das bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -------------------------------
# Título da aplicação
# -------------------------------
st.title("Previsão de Notas com Machine Learning")

st.write("""
Aplicação desenvolvida com Streamlit e Scikit-Learn
para prever notas com base nas horas de estudo.
""")

# -------------------------------
# Base de dados
# -------------------------------
estudos = pd.DataFrame({
    'notas': [1, 2, 4, 6, 8, 10],
    'horas': [2, 4, 5, 7, 9, 10]
})

# Exibição da base
st.subheader("Base de Dados")
st.dataframe(estudos)

# -------------------------------
# Separação das variáveis
# -------------------------------
X = estudos[['horas']]
y = estudos['notas']

# -------------------------------
# Criação e treinamento do modelo
# -------------------------------
modelo = LinearRegression()
modelo.fit(X, y)

# -------------------------------
# Entrada do usuário
# -------------------------------
st.subheader("Previsão de Nota")

horas_estudo = st.slider(
    "Selecione a quantidade de horas de estudo:",
    min_value=1,
    max_value=12,
    value=6
)
previsao = modelo.predict([[horas_estudo]])[0]

# Limitar nota máxima em 10
previsao = min(previsao, 10)

# Limitar nota mínima em 0
previsao = max(previsao, 0)
# Realização da previsão
previsao = modelo.predict([[horas_estudo]])

# Resultado
st.success(
    f'Nota prevista para {horas_estudo} horas de estudo: {previsao[0]:.2f}'
)

# -------------------------------
# Representação gráfica
# -------------------------------
st.subheader("Gráfico da Regressão Linear")

fig, ax = plt.subplots()

# Pontos reais
ax.scatter(estudos['horas'], estudos['notas'])

# Linha da regressão
ax.plot(
    estudos['horas'],
    modelo.predict(X)
)

# Configurações do gráfico
ax.set_xlabel("Horas de Estudo")
ax.set_ylabel("Notas")
ax.set_title("Horas de Estudo x Notas")

# Exibição no Streamlit
st.pyplot(fig)

# -------------------------------
# Informações do modelo
# -------------------------------
st.subheader("Equação da Regressão Linear")

coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

st.write(
    f'Equação do modelo: nota = {coeficiente:.2f} * horas + {intercepto:.2f}'
)
