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

#---------------- projeto 2 __________

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título da aplicação
st.title("🎮 Detector de Sono Gamer")

# Criando a base de dados
dados = pd.DataFrame({
    'horas_jogo': [1, 2, 4, 6, 8, 10],
    'cansaco': [1, 2, 3, 5, 8, 10]
})

# Exibindo tabela
st.subheader("📋 Base de Dados")
st.dataframe(dados)

# Separando entrada e saída
X = dados[['horas_jogo']]
y = dados['cansaco']

# Criando modelo
modelo = LinearRegression()

# Treinando IA
modelo.fit(X, y)

# Slider do usuário
horas = st.slider(
    "Quantas horas o gamer jogou?",
    1,
    10,
    5
)

# Fazendo previsão
previsao = modelo.predict([[horas]])[0]

# Limitando valor máximo
previsao = min(previsao, 10)

# Resultado
st.success(
    f'😴 Cansaço previsto: {previsao:.2f}'
)

# Criando linha prevista
dados['previsao'] = modelo.predict(X)

# Exibindo gráfico no Streamlit
st.subheader("📊 Gráfico da IA")

st.line_chart(
    dados.set_index('horas_jogo')[['cansaco', 'previsao']]
)

#-----------------projeto 3 ---------------

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("🍦 IA do Sorvete")

# Dados
dados = pd.DataFrame({
    'temperatura': [18, 20, 24, 27, 30, 35],
    'vendas': [20, 25, 40, 55, 70, 100]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['temperatura']]
y = dados['vendas']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
temperatura = st.slider(
    "🌡️ Temperatura do dia",
    15,
    40,
    30
)

# Previsão
previsao = modelo.predict([[temperatura]])[0]

# Resultado
st.success(
    f'🍦 Vendas previstas: {previsao:.0f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('temperatura')[['vendas', 'previsao']]
)

#--------------------projeto 4_________

import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Título
st.title("🥷 Detector de Aprovação Ninja")

# Dados
dados = pd.DataFrame({
    'faltas': [0, 1, 2, 5, 7, 10],
    'resultado': [1, 1, 1, 0, 0, 0]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['faltas']]
y = dados['resultado']

# Modelo
modelo = LogisticRegression()

# Treinamento
modelo.fit(X, y)

# Slider
faltas = st.slider(
    "📚 Quantidade de faltas",
    0,
    10,
    2
)

# Previsão
previsao = modelo.predict([[faltas]])[0]

# Resultado
if previsao == 1:
    st.success("✅ A IA prevê APROVAÇÃO")
else:
    st.error("❌ A IA prevê REPROVAÇÃO")

# Probabilidades
probabilidade = modelo.predict_proba([[faltas]])[0]

# Mostrar gráfico
grafico = pd.DataFrame({
    'Aprovado': [probabilidade[1]],
    'Reprovado': [probabilidade[0]]
})

st.bar_chart(grafico)

#--------------------projeto 5-----------

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("🐶 IA do Pet Feliz")

# Base de dados
dados = pd.DataFrame({
    'passeios': [1, 2, 3, 4, 5],
    'felicidade': [2, 4, 5, 8, 10]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['passeios']]
y = dados['felicidade']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
passeios = st.slider(
    "🐾 Quantidade de passeios",
    1,
    10,
    5
)

# Previsão
previsao = modelo.predict([[passeios]])[0]

# Limite máximo
previsao = min(previsao, 10)

# Resultado
st.success(
    f'🐕 Felicidade prevista: {previsao:.2f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('passeios')[['felicidade', 'previsao']]
)

#--------------------projeto 6-----------
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("🎬 Detector de Filme Bom")

# Dados
dados = pd.DataFrame({
    'duracao': [80, 90, 100, 110, 120],
    'nota': [4, 5, 7, 8, 9]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['duracao']]
y = dados['nota']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
duracao = st.slider(
    "🎥 Duração do filme",
    60,
    180,
    120
)

# Previsão
previsao = modelo.predict([[duracao]])[0]

# Limite máximo
previsao = min(previsao, 10)

# Resultado
st.success(
    f'⭐ Nota prevista: {previsao:.2f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('duracao')[['nota', 'previsao']]
)
#--------------------projeto 7-----------

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("🍕 IA da Pizza")

# Dados
dados = pd.DataFrame({
    'tamanho': [20, 25, 30, 35, 40],
    'preco': [20, 30, 40, 50, 60]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['tamanho']]
y = dados['preco']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
tamanho = st.slider(
    "🍕 Tamanho da pizza",
    20,
    60,
    35
)

# Previsão
previsao = modelo.predict([[tamanho]])[0]

# Resultado
st.success(
    f'💰 Preço previsto: R${previsao:.2f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('tamanho')[['preco', 'previsao']]
)

#--------------------projeto 8-----------
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("🎵 Detector de Música Viral")

# Dados
dados = pd.DataFrame({
    'bpm': [80, 90, 100, 120, 140],
    'viral': [1, 2, 4, 7, 10]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['bpm']]
y = dados['viral']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
bpm = st.slider(
    "🎶 BPM da música",
    50,
    150,
    100
)

# Previsão
previsao = modelo.predict([[bpm]])[0]

# Limite máximo
previsao = min(previsao, 10)

# Resultado
st.success(
    f'🔥 Nível viral previsto: {previsao:.2f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('bpm')[['viral', 'previsao']]
)
#--------------------projeto 9-----------

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Título
st.title("☕ IA da Energia do Café")

# Dados
dados = pd.DataFrame({
    'xicaras': [1, 2, 3, 4, 5],
    'energia': [2, 4, 6, 8, 10]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['xicaras']]
y = dados['energia']

# Modelo
modelo = LinearRegression()

# Treinamento
modelo.fit(X, y)

# Slider
xicaras = st.slider(
    "☕ Quantidade de cafés",
    1,
    10,
    4
)

# Previsão
previsao = modelo.predict([[xicaras]])[0]

# Limite máximo
previsao = min(previsao, 10)

# Resultado
st.success(
    f'⚡ Energia prevista: {previsao:.2f}'
)

# Linha da IA
dados['previsao'] = modelo.predict(X)

# Gráfico
st.line_chart(
    dados.set_index('xicaras')[['energia', 'previsao']]
)
#--------------------projeto 10-----------
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Título
st.title("🦸 Rede Neural dos Super-Heróis")

# Dados
dados = pd.DataFrame({
    'forca': [1, 2, 3, 7, 8, 10],
    'heroi': [0, 0, 0, 1, 1, 1]
})

# Mostrar tabela
st.dataframe(dados)

# Entrada e saída
X = dados[['forca']]
y = dados['heroi']

# Modelo
modelo = LogisticRegression()

# Treinamento
modelo.fit(X, y)

# Slider
forca = st.slider(
    "💪 Nível de força",
    0,
    100,
    50
)

# Previsão
previsao = modelo.predict([[forca]])[0]

# Resultado
if previsao == 1:
    st.success("🦸 A IA prevê: SUPER-HERÓI")
else:
    st.error("🙂 A IA prevê: HUMANO COMUM")

# Probabilidades
probabilidade = modelo.predict_proba([[forca]])[0]

# Gráfico
grafico = pd.DataFrame({
    'Herói': [probabilidade[1]],
    'Humano': [probabilidade[0]]
})

st.bar_chart(grafico)