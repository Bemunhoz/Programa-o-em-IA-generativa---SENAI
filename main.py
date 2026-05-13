import streamlit as st
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

st.title('ENSINA A MÁQUINA A PREVER O FUTURO')
st.write('Preve o campeão da copa ⚽')

st.header('Opções de campeão 🏆🏆🏆...')

#dados

dados = pd.DataFrame({
'gols':[12,15,10,18,14,11,16],
'ranking':[1,3,2,1,4,10,2],
'pais':['Brasil', 'Argentina', 'França', 'Brasil', 'França', 'Argentina', 'Brasil']
})

#alinhamento do modelo

modelo_copa = DecisionTreeClassifier()
#treinamento
modelo_copa.fit(dados[['gols', 'ranking']], dados['pais'])

gols_input = st.number_input('Quantos gols o time fez?', 0,30,15)
rank_input = st.number_input('Qual a posição', 1, 100, 1)

if st.button('Prever'):
    #previsao
    resultado_copa = modelo_copa.predict([[gols_input, rank_input]])
    st.success(f'O provavel campeão é {resultado_copa}')

#---------------------------------------------

#notas de estudos

st.header('ANÁLIZE DE NOTAS - PREVENDO')

estudos = pd.DataFrame({
    'notas':[1,2,4,6,8,10],
    'horas':[2,4,5,7,9,10]
})

st.scatter_chart(estudos, x='horas', y='notas')

modelo_escola = LinearRegression()
modelo_escola.fit(estudos[['horas']], estudos['notas'])

h_estudo = st.slider('horas de estudos', 0,12,5)
nota_final = modelo_escola.predict([[h_estudo]])

st.metric (f'sua nota seria', f'{ min(nota_final[0], 10.0):.1f}')

#--------------------------------------------------------

#previsao de faturamento

st.header('Previsão de Vendas')
dados_vendas = pd.DataFrame({
    'investimento':[100,200,300,400,500,600],
    'faturamento': [1200,2500,3200,4800,5100,6300]
})

st.line_chart(dados_vendas, x= 'investimento', y= 'faturamento')

modelo_vendas = LinearRegression()
modelo_vendas.fit(dados_vendas [['investimento']], dados_vendas ['faturamento'])

v_investido = st.slider('valor investido',0,600,1000)
faturamento_vendas = modelo_vendas.predict([[v_investido]])

st.metric (f' seu faturamento seria', f'{ min(faturamento_vendas[0], 10000):.1f}')