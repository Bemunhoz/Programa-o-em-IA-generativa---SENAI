# ============================================================
# 🌡️ APP - PROJEÇÃO DE GASTO COM AR-CONDICIONADO
# Analogia: o modelo aprende como uma pessoa que foi anotando
# a conta de luz todo mês e aprendeu o padrão de gasto!
# ============================================================

# 1️⃣ IMPORTANDO AS BIBLIOTECAS
import streamlit as st      # interface web
import tensorflow as tf     # modelo de aprendizado
import numpy as np          # cálculos numéricos
import pandas as pd         # organizar dados para o gráfico

# ============================================================
# ⚙️ CONFIGURAÇÕES DA PÁGINA
# st.set_page_config = personaliza o título e ícone da aba
# ============================================================
st.set_page_config(page_title="💡 Gasto com Ar-Condicionado", layout="centered")

st.title("🌡️ Projeção de Gasto com Ar-Condicionado")
st.write("Insira quantas horas por dia você usa o ar-condicionado e veja a projeção do gasto mensal!")

# ============================================================
# 📚 DADOS SIMULADOS PARA TREINAR O MODELO
# Analogia: são como anotações históricas de contas anteriores
# Quanto mais horas ligado → maior o gasto
#
# Valores baseados em:
# - Ar-condicionado de 9.000 BTUs (~850W de potência)
# - Tarifa média Brasil: R$ 0,75 por kWh
# - 30 dias no mês
#
# Fórmula real: horas × 0.85kW × 0.75 × 30 dias
# ============================================================
horas_treino = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
gasto_treino = np.array([19.13, 38.25, 57.38, 76.50, 95.63,
                          114.75, 133.88, 153.00, 172.13, 191.25], dtype=float)

# ============================================================
# 🤖 CRIANDO E TREINANDO O MODELO
# @st.cache_resource = treina só uma vez e guarda na memória
# Sem isso, o modelo treinaria do zero a cada clique do usuário!
# ============================================================
@st.cache_resource
def treinar_modelo():
    # Dense(1) = 1 neurônio tentando aprender a relação
    # horas → gasto (como um funcionário novo aprendendo a calcular)
    modelo = tf.keras.Sequential([
        tf.keras.layers.Dense(units=1, input_shape=[1])
    ])

    # sgd = método de aprendizado gradual (como errar e corrigir)
    # mse = mede o quanto errou (mean squared error)
    modelo.compile(optimizer='sgd', loss='mse')

    # verbose=0 = treina em silêncio, sem poluir a tela
    modelo.fit(horas_treino, gasto_treino, epochs=1000, verbose=0)

    return modelo

# Chamando a função para treinar (ou recuperar da memória)
modelo = treinar_modelo()

# ============================================================
# 🎛️ INTERFACE — ENTRADA DO USUÁRIO
# st.slider = controle deslizante para o usuário escolher as horas
# ============================================================
st.subheader("⏱️ Quantas horas por dia você usa o ar?")

horas_usuario = st.slider(
    label="Horas de uso diário:",
    min_value=1,
    max_value=24,
    value=8,       # valor padrão ao abrir o app
    step=1
)

# ============================================================
# 🔮 FAZENDO A PREVISÃO
# O modelo recebe as horas e devolve o gasto estimado
# ============================================================
entrada   = np.array([float(horas_usuario)])
previsao  = modelo.predict(entrada, verbose=0)
gasto_mes = previsao[0][0]

# ============================================================
# 📊 EXIBINDO O RESULTADO
# st.metric = componente visual de destaque para números
# ============================================================
st.subheader("💰 Resultado da Projeção")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="⏱️ Horas/dia",
        value=f"{horas_usuario}h"
    )

with col2:
    # Calculando o gasto diário estimado
    gasto_dia = gasto_mes / 30
    st.metric(
        label="📅 Gasto diário",
        value=f"R$ {gasto_dia:.2f}"
    )

with col3:
    st.metric(
        label="🗓️ Gasto mensal estimado",
        value=f"R$ {gasto_mes:.2f}"
    )

# ============================================================
# 📈 GRÁFICO DE LINHA — EVOLUÇÃO DO GASTO
# Mostra como o gasto cresce conforme aumentam as horas
#
# Analogia: como ver numa planilha o crescimento da conta
# de luz semana a semana ao longo do mês
# ============================================================
st.subheader("📈 Evolução do Gasto ao Longo do Mês")

# Gerando previsões para cada dia do mês (1 a 30)
# Cada dia acumula o gasto: dia 1 = 1x diário, dia 2 = 2x diário...
dias        = np.arange(1, 31, dtype=float)           # dias 1 ao 30
gasto_diario = gasto_mes / 30                          # gasto por dia
gasto_acumulado = dias * gasto_diario                  # acúmulo dia a dia

# Criando um DataFrame (tabela) para o st.line_chart
# O pandas organiza os dados no formato que o Streamlit entende
# DEPOIS — índice como número (ordena corretamente)
df_grafico = pd.DataFrame({
    "Gasto Acumulado (R$)": gasto_acumulado
}, index=dias.astype(int))

df_grafico.index.name = "Dia"

# Exibindo o gráfico de linha
st.line_chart(df_grafico)

# ============================================================
# ℹ️ INFORMAÇÕES ADICIONAIS
# st.info = caixa azul informativa
# st.expander = seção que o usuário pode abrir/fechar
# ============================================================
st.info(f"💡 Com **{horas_usuario}h/dia**, você gasta cerca de **R$ {gasto_diario:.2f} por dia** de energia só com o ar-condicionado.")

with st.expander("📋 Ver premissas do cálculo"):
    st.write("""
    - **Equipamento:** Ar-condicionado 9.000 BTUs
    - **Potência média:** 850W (0,85 kWh)
    - **Tarifa simulada:** R$ 0,75 por kWh
    - **Período:** 30 dias no mês
    - **Modelo:** Regressão linear com TensorFlow
    """)

# ============================================================
# ⚠️ RODAPÉ
# ============================================================
st.caption("⚠️ Valores simulados para fins educacionais. Consulte sua fatura real para dados precisos.")

# ============================================================
# 📱 CALCULADORA DE ENGAJAMENTO DE TIKTOK
# Analogia: como um termômetro que mede a "temperatura" do post
# Frio = Flopado ❄️ | Quente = Viral 🔥
# ============================================================

# 1️⃣ IMPORTANDO AS BIBLIOTECAS
import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(page_title="📱 TikTok Engajamento", layout="centered")

st.title("📱 Calculadora de Engajamento TikTok")
st.write("Descubra se seu vídeo vai **Flopar ❄️** ou ficar **Viral 🔥**!")

# ============================================================
# 📚 DADOS SIMULADOS PARA TREINAR O MODELO
#
# Analogia: são como anotações de um social media experiente
# que foi registrando quantas hashtags cada vídeo usou
# e quantas visualizações teve
#
# Regra simulada:
# - Poucas hashtags (1-3): alcance baixo
# - Hashtags ideais (5-8): alcance máximo
# - Muitas hashtags (10+): alcance cai (parece spam)
# ============================================================
hashtags_treino = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    dtype=float
)

alcance_treino = np.array(
    [1000, 3000, 8000, 15000, 40000, 80000, 95000, 90000,
     70000, 50000, 35000, 20000, 12000, 8000, 5000],
    dtype=float
)

# ============================================================
# 🔧 NORMALIZANDO OS DADOS
# Analogia: como converter notas de 0-100 para 0-1
# O TensorFlow aprende MUITO melhor com números pequenos!
# Sem isso, seria como tentar medir uma formiga com uma régua de km
# ============================================================
max_hashtags = float(hashtags_treino.max())   # 15
max_alcance  = float(alcance_treino.max())    # 95000

hashtags_norm = hashtags_treino / max_hashtags
alcance_norm  = alcance_treino  / max_alcance

# ============================================================
# 🤖 TREINANDO O MODELO
# @st.cache_resource = treina só uma vez, guarda na memória
# Sem isso: treinaria do zero a cada interação do usuário!
# ============================================================
@st.cache_resource
def treinar_modelo():
    # Modelo com 3 camadas para capturar a curva
    # (sobe até 7 hashtags, depois desce — não é linha reta!)
    modelo = tf.keras.Sequential([
        # Camada 1: 16 neurônios aprendendo padrões iniciais
        tf.keras.layers.Dense(16, activation='relu', input_shape=[1]),
        # Camada 2: 8 neurônios refinando os padrões
        tf.keras.layers.Dense(8, activation='relu'),
        # Camada 3: 1 neurônio dando a resposta final
        tf.keras.layers.Dense(1)
    ])

    # adam = otimizador mais inteligente que sgd para curvas complexas
    modelo.compile(optimizer='adam', loss='mse')
    modelo.fit(hashtags_norm, alcance_norm, epochs=1000, verbose=0)

    return modelo

modelo = treinar_modelo()

# ============================================================
# 🎛️ INTERFACE — ENTRADAS DO USUÁRIO
# ============================================================
st.subheader("🎬 Configure seu Vídeo")

# Caixa de seleção de categoria
# selectbox = menu dropdown com opções predefinidas
categoria = st.selectbox(
    label="📂 Categoria do vídeo:",
    options=[
        "💃 Dança",
        "😂 Humor",
        "🍳 Culinária",
        "💄 Beleza",
        "🎮 Games",
        "📚 Educação",
        "🐾 Pets",
        "💪 Fitness"
    ]
)

# Slider de hashtags
hashtags_usuario = st.slider(
    label="# Quantidade de hashtags:",
    min_value=1,
    max_value=15,
    value=5,
    step=1
)

# ============================================================
# 📊 MULTIPLICADOR POR CATEGORIA
# Analogia: cada categoria tem um "fator sorte"
# Como diferentes pratos têm tempos de cozimento diferentes
# ============================================================
multiplicadores = {
    "💃 Dança"    : 1.40,
    "😂 Humor"    : 1.35,
    "🍳 Culinária": 1.10,
    "💄 Beleza"   : 1.20,
    "🎮 Games"    : 1.05,
    "📚 Educação" : 0.90,
    "🐾 Pets"     : 1.30,
    "💪 Fitness"  : 1.15
}

fator = multiplicadores[categoria]

# ============================================================
# 🔮 FAZENDO A PREVISÃO
# 1. Normaliza a entrada (mesma escala do treino)
# 2. Modelo prevê o alcance normalizado
# 3. Desnormaliza para voltar ao número real
# 4. Aplica o multiplicador de categoria
# ============================================================
entrada_norm = np.array([hashtags_usuario / max_hashtags])
previsao_norm = modelo.predict(entrada_norm, verbose=0)[0][0]

# Desnormalizando: voltando para a escala real de visualizações
alcance_previsto = previsao_norm * max_alcance * fator

# Garantindo que não fique negativo (segurança extra)
alcance_previsto = max(0, alcance_previsto)

# ============================================================
# 🌡️ CLASSIFICANDO O RESULTADO
# Como um termômetro de engajamento
# ============================================================
if alcance_previsto >= 70000:
    status     = "🔥 VIRAL!"
    cor        = "success"    # verde
    mensagem   = "Esse post vai bombar! Poste já!"
elif alcance_previsto >= 30000:
    status     = "📈 Em Alta"
    cor        = "info"       # azul
    mensagem   = "Bom engajamento! Vale a pena postar."
elif alcance_previsto >= 10000:
    status     = "😐 Mediano"
    cor        = "warning"    # amarelo
    mensagem   = "Resultado ok, mas dá pra melhorar."
else:
    status     = "❄️ FLOPADO"
    cor        = "error"      # vermelho
    mensagem   = "Cuidado! Esse post pode não performar bem."

# ============================================================
# 📊 EXIBINDO OS RESULTADOS
# ============================================================
st.subheader("📊 Resultado da Previsão")

# Métricas em 3 colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📂 Categoria", categoria.split()[1])  # só o nome sem emoji

with col2:
    st.metric("# Hashtags", f"{hashtags_usuario}")

with col3:
    st.metric("👁️ Alcance Previsto", f"{int(alcance_previsto):,}".replace(",", "."))

# Alerta visual baseado no status
# getattr busca a função certa do st (st.success, st.error, etc.)
alerta = getattr(st, cor)
alerta(f"**{status}** — {mensagem}")

# ============================================================
# 📈 GRÁFICO — CURVA COMPLETA DE HASHTAGS
# Mostra como o alcance varia de 1 a 15 hashtags
# O ponto do usuário fica destacado visualmente
# ============================================================
st.subheader("📈 Curva de Alcance por Hashtags")

# Gerando previsões para todos os valores de 1 a 15
todos_hashtags   = np.arange(1, 16, dtype=float)
todos_norm       = todos_hashtags / max_hashtags
todas_previsoes  = modelo.predict(todos_norm, verbose=0).flatten()
todos_alcances   = todas_previsoes * max_alcance * fator
todos_alcances   = np.maximum(todos_alcances, 0)

# Criando DataFrame para o gráfico
df_grafico = pd.DataFrame({
    "Alcance Previsto": todos_alcances.astype(int)
}, index=todos_hashtags.astype(int))

df_grafico.index.name = "Hashtags"

st.line_chart(df_grafico)

# ============================================================
# 💡 DICA INTELIGENTE
# Encontra o número de hashtags com maior alcance previsto
# ============================================================
melhor_hashtag = int(todos_hashtags[np.argmax(todos_alcances)])

st.info(f"💡 Para a categoria **{categoria}**, o número ideal de hashtags é **{melhor_hashtag}**!")

# ============================================================
# 📋 TABELA DETALHADA (expansível)
# ============================================================
with st.expander("📋 Ver tabela completa de alcance"):
    df_tabela = pd.DataFrame({
        "Hashtags"        : todos_hashtags.astype(int),
        "Alcance Previsto": todos_alcances.astype(int)
    })
    st.dataframe(df_tabela, use_container_width=True)

# ============================================================
# ⚠️ RODAPÉ
# ============================================================
st.caption("⚠️ Valores simulados para fins educacionais. Engajamento real depende de muitos outros fatores.")

#_____________

# ============================================================
# 🛡️ FILTRO ANTISPAM DE DM DO INSTAGRAM - V2
# Analogia: um segurança de evento que lê o crachá de cada
# visitante e decide na hora se deixa entrar ou barra na porta
# Crachá = palavras da mensagem | Segurança = modelo TensorFlow
# ============================================================

import streamlit as st
import tensorflow as tf
import numpy as np

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(page_title="🛡️ Filtro Antispam", layout="centered")
st.title("🛡️ Filtro Antispam de DM do Instagram")
st.write("Cole uma mensagem e descubra se é **Segura ✅** ou **Spam 🚨**")

# ============================================================
# 📚 DADOS DE TREINO SIMULADOS
# Rótulos: 0 = Segura | 1 = Spam
# ============================================================
mensagens = [
    "adorei seu conteúdo continue assim",
    "quando sai o próximo vídeo",
    "você me inspirou muito obrigada",
    "que foto linda parabéns pelo trabalho",
    "amei a receita vou tentar fazer",
    "seu trabalho é incrível demais",
    "posso te fazer uma pergunta",
    "que lugar bonito onde foi isso",
    "boa noite tudo bem com você",
    "qual câmera você usa nos vídeos",
    "clique no link ganhe dinheiro rápido",
    "você foi selecionado premio acesse agora",
    "ganhe seguidores grátis clique aqui",
    "promoção exclusiva só hoje acesse o link",
    "sua conta foi comprometida acesse para resolver",
    "transferência urgente preciso de ajuda financeira",
    "venda de seguidores baratos link na bio",
    "parabéns você ganhou um iphone clique aqui",
    "atualize seus dados bancários urgente link abaixo",
    "oferta imperdível só para você acesse agora",
]

rotulos = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1], dtype=float)

# ============================================================
# 🔤 VETORIZADOR DE TEXTO
#
# Analogia: transforma cada palavra em um número
# Como traduzir um idioma para outro que o modelo entende
#
# ⚠️ CORREÇÃO DOS ERROS ANTERIORES:
# Não definimos VOCAB_SIZE manualmente!
# Deixamos o adapt() descobrir o tamanho real do vocabulário
# e só DEPOIS capturamos esse valor — evita conflito de tamanhos
# ============================================================
vetorizador = tf.keras.layers.TextVectorization(output_mode='multi_hot')

# adapt() estuda o vocabulário das mensagens de treino
vetorizador.adapt(mensagens)

# Transformando mensagens em vetores numéricos
X_treino = vetorizador(mensagens)

# Capturando o tamanho REAL do vocabulário depois do adapt()
# Essa é a chave que evitou o ValueError anterior!
tamanho_vocab = X_treino.shape[1]

# ============================================================
# 🤖 MODELO — recebe tamanho_vocab como parâmetro
#
# ⚠️ CORREÇÃO DOS ERROS ANTERIORES:
# Passamos tamanho_vocab como argumento da função
# para evitar o NameError de escopo
# ============================================================
@st.cache_resource
def treinar_modelo(vocab_size):
    modelo = tf.keras.Sequential([
        # Camada de entrada: tamanho dinâmico e real do vocabulário
        tf.keras.layers.Dense(32, activation='relu', input_shape=[vocab_size]),
        tf.keras.layers.Dense(16, activation='relu'),
        # Dropout: evita "decorar" as mensagens de treino
        tf.keras.layers.Dropout(0.3),
        # Saída: sigmoid → valor entre 0 (segura) e 1 (spam)
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    modelo.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    modelo.fit(X_treino, rotulos, epochs=300, verbose=0)
    return modelo

# ============================================================
# ⏳ TREINANDO COM FEEDBACK VISUAL
# st.spinner evita que a tela pareça travada durante o treino!
# ============================================================
with st.spinner("🤖 Carregando modelo antispam..."):
    modelo = treinar_modelo(tamanho_vocab)

st.success("✅ Modelo pronto! Cole uma DM para analisar.")
st.divider()

# ============================================================
# 🎛️ INTERFACE — ENTRADA DO USUÁRIO
# ============================================================
st.subheader("📩 Cole a DM aqui:")

dm = st.text_area(
    label="Mensagem recebida:",
    placeholder="Ex: parabéns você foi selecionado clique no link...",
    height=130
)

# ============================================================
# 🔍 ANÁLISE — só roda ao clicar no botão
# Isso evita que o app processe a cada letra digitada!
# ============================================================
if st.button("🔍 Analisar Mensagem", use_container_width=True):

    if not dm.strip():
        st.warning("⚠️ Digite ou cole uma mensagem primeiro!")

    else:
        # Vetorizando a entrada do usuário
        entrada = vetorizador([dm.lower()])

        # Modelo prevê: próximo de 0 = segura | próximo de 1 = spam
        probabilidade = float(modelo.predict(entrada, verbose=0)[0][0])
        eh_spam       = probabilidade >= 0.5

        # ====================================================
        # 📊 EXIBINDO O RESULTADO
        # ====================================================
        st.subheader("📊 Resultado")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("🔎 Probabilidade de Spam", f"{probabilidade * 100:.1f}%")
        with col2:
            confianca = probabilidade if eh_spam else (1 - probabilidade)
            st.metric("🎯 Confiança", f"{confianca * 100:.1f}%")

        # Veredito visual
        if eh_spam:
            st.error("🚨 **SPAM!** Não clique em links. Bloqueie e reporte o perfil.")
        else:
            st.success("✅ **SEGURA!** Nenhum padrão suspeito identificado.")

        # Barra de risco
        st.subheader("🌡️ Nível de Risco")
        st.progress(probabilidade)

        if probabilidade < 0.3:
            st.caption("🟢 Risco Baixo")
        elif probabilidade < 0.6:
            st.caption("🟡 Risco Médio — fique atento")
        else:
            st.caption("🔴 Risco Alto — provável spam!")

st.divider()

# ============================================================
# 💡 EXEMPLOS PARA TESTAR
# ============================================================
with st.expander("💡 Exemplos para testar"):
    st.write("**🚨 Spam:**")
    st.code("parabéns você foi selecionado acesse o link agora")
    st.code("clique aqui ganhe dinheiro rápido oferta exclusiva")

    st.write("**✅ Segura:**")
    st.code("adorei seu conteúdo quando sai o próximo vídeo")
    st.code("que foto linda você me inspirou muito obrigada")

st.caption("⚠️ Modelo treinado com dados simulados para fins educacionais.")


#_____________________________________________
# ============================================================
# 🏍️ SIMULADOR DE APROVAÇÃO DE CRÉDITO BANCÁRIO
# Analogia: como um gerente de banco experiente que analisa
# seu perfil financeiro antes de liberar o dinheiro
# Gerente = modelo TensorFlow | Perfil = seus dados financeiros
# ============================================================

import streamlit as st
import tensorflow as tf
import numpy as np

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(page_title="🏍️ Crédito para Moto", layout="centered")
st.title("🏍️ Simulador de Aprovação de Crédito")
st.write("Descubra se o banco vai liberar o financiamento da sua moto!")
st.divider()

# ============================================================
# 📚 DADOS SIMULADOS DE TREINO
#
# Cada linha representa um cliente:
# [idade, renda, parcela, score, entrada_percentual]
#
# Regras embutidas nos dados:
# ✅ Aprovado quando:
#    - Idade >= 18
#    - Parcela <= 30% da renda
#    - Score >= 500
# ❌ Negado quando qualquer regra é violada
# ============================================================
clientes = np.array([
    # idade  renda    parcela  score  entrada%
    [25,     3000,    600,     700,   20],   # ✅ aprovado
    [30,     5000,    800,     800,   30],   # ✅ aprovado
    [22,     2500,    500,     650,   15],   # ✅ aprovado
    [35,     8000,    1200,    900,   25],   # ✅ aprovado
    [28,     4000,    700,     750,   20],   # ✅ aprovado
    [40,     6000,    900,     820,   30],   # ✅ aprovado
    [19,     1800,    400,     600,   10],   # ✅ aprovado
    [32,     7000,    1000,    870,   25],   # ✅ aprovado
    [45,     9000,    1500,    950,   30],   # ✅ aprovado
    [27,     3500,    650,     720,   15],   # ✅ aprovado
    [17,     1000,    500,     200,   0],    # ❌ menor de idade + score baixo
    [20,     1500,    800,     250,   0],    # ❌ parcela > 30% da renda
    [23,     2000,    900,     150,   0],    # ❌ score muito baixo
    [18,     1200,    600,     300,   0],    # ❌ parcela > 30% da renda
    [29,     3000,    1500,    400,   0],    # ❌ parcela > 30% da renda
    [16,     500,     300,     100,   0],    # ❌ menor de idade
    [21,     1800,    900,     200,   0],    # ❌ score baixo + parcela alta
    [33,     4000,    2000,    350,   0],    # ❌ parcela > 30% da renda
    [25,     2500,    1200,    280,   0],    # ❌ score baixo + parcela alta
    [19,     1500,    700,     180,   0],    # ❌ score muito baixo
], dtype=float)

rotulos = np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0], dtype=float)

# ============================================================
# 🔧 NORMALIZANDO OS DADOS
#
# Analogia: converter tudo para a mesma "unidade de medida"
# Como comparar distâncias: não misturamos km com milhas
# O TensorFlow aprende melhor com valores entre 0 e 1
# ============================================================
maximos = clientes.max(axis=0)   # maior valor de cada coluna
clientes_norm = clientes / maximos

# ============================================================
# 🤖 TREINANDO O MODELO
# ============================================================
@st.cache_resource
def treinar_modelo(shape):
    modelo = tf.keras.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=[shape]),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1,  activation='sigmoid')
    ])
    modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    modelo.fit(clientes_norm, rotulos, epochs=500, verbose=0)
    return modelo

with st.spinner("🤖 Carregando sistema de análise de crédito..."):
    modelo = treinar_modelo(clientes_norm.shape[1])

st.success("✅ Sistema pronto! Preencha o formulário abaixo.")
st.divider()

# ============================================================
# 🎛️ FORMULÁRIO — DADOS DO CLIENTE
# ============================================================
st.subheader("📋 Seus Dados")

col1, col2 = st.columns(2)

with col1:
    idade  = st.number_input("🎂 Idade", min_value=16, max_value=80, value=22, step=1)
    renda  = st.number_input("💰 Renda Mensal (R$)", min_value=500.0, max_value=50000.0,
                              value=3000.0, step=100.0)

with col2:
    score   = st.slider("📊 Score de Crédito", min_value=0, max_value=1000, value=650)
    entrada = st.slider("💵 Entrada (%)", min_value=0, max_value=50, value=20, step=5)

st.subheader("🏍️ Dados do Financiamento")
parcela = st.number_input("📅 Valor da Parcela Desejada (R$)", min_value=100.0,
                           max_value=10000.0, value=600.0, step=50.0)

# ============================================================
# 📊 INDICADORES EM TEMPO REAL
# Mostram ao usuário o impacto dos dados conforme ele digita
# ============================================================
st.divider()
st.subheader("📈 Análise do seu Perfil")

comprometimento = (parcela / renda) * 100

col1, col2, col3 = st.columns(3)

with col1:
    cor_comprometimento = "normal" if comprometimento <= 30 else "inverse"
    st.metric(
        "💳 Comprometimento de Renda",
        f"{comprometimento:.1f}%",
        delta="✅ OK" if comprometimento <= 30 else "❌ Alto",
        delta_color=cor_comprometimento
    )

with col2:
    faixa_score = "🟢 Baixo Risco" if score >= 701 else ("🟡 Médio Risco" if score >= 301 else "🔴 Alto Risco")
    st.metric("📊 Faixa de Score", faixa_score)

with col3:
    limite_ideal = renda * 0.30
    st.metric("💡 Parcela Ideal Máxima", f"R$ {limite_ideal:.2f}")

st.divider()

# ============================================================
# 🔍 BOTÃO DE ANÁLISE
# ============================================================
if st.button("🔍 Analisar Crédito", use_container_width=True):

    # Validação básica antes de chamar o modelo
    if idade < 18:
        st.error("❌ **Crédito Negado!** É necessário ter pelo menos 18 anos.")

    else:
        # Montando o vetor do cliente com os mesmos 5 campos do treino
        cliente = np.array([[idade, renda, parcela, score, entrada]], dtype=float)

        # Normalizando com os mesmos máximos do treino
        cliente_norm = cliente / maximos

        # Previsão do modelo
        probabilidade = float(modelo.predict(cliente_norm, verbose=0)[0][0])
        aprovado      = probabilidade >= 0.5

        st.subheader("🏦 Resultado da Análise")

        # Métricas do resultado
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🎯 Probabilidade de Aprovação", f"{probabilidade * 100:.1f}%")
        with col2:
            st.metric("📅 Parcela Solicitada", f"R$ {parcela:.2f}")

        # ====================================================
        # ✅ CRÉDITO APROVADO
        # ====================================================
        if aprovado:
            st.success("✅ **CRÉDITO APROVADO!** O banco tende a liberar o financiamento.")
            st.balloons()

            st.info(f"""
            📋 **Resumo da Aprovação:**
            - 🎂 Idade: {idade} anos ✅
            - 💰 Renda: R$ {renda:.2f}
            - 📅 Parcela: R$ {parcela:.2f} ({comprometimento:.1f}% da renda)
            - 📊 Score: {score} pontos — {faixa_score}
            - 💵 Entrada: {entrada}%
            """)

        # ====================================================
        # ❌ CRÉDITO NEGADO — COM SUGESTÃO DE PARCELA MENOR
        # ====================================================
        else:
            st.error("❌ **CRÉDITO NEGADO!** O perfil atual não atende os critérios.")

            # Identificando os motivos da negação
            st.subheader("⚠️ Motivos da Negação:")
            motivos = []

            if comprometimento > 30:
                motivos.append(f"📛 Parcela compromete **{comprometimento:.1f}%** da renda (limite: 30%)")
            if score < 300:
                motivos.append("📛 Score muito baixo — alto risco para a financeira")
            elif score < 500:
                motivos.append("📛 Score abaixo do recomendado para aprovação")
            if entrada < 10:
                motivos.append("📛 Entrada muito baixa — aumentar facilita a aprovação")

            for motivo in motivos:
                st.warning(motivo)

            # ================================================
            # 💡 SUGESTÃO AUTOMÁTICA DE PARCELA MENOR
            #
            # Calcula a parcela máxima dentro do limite de 30%
            # e sugere ao usuário como alternativa viável
            # ================================================
            parcela_sugerida = renda * 0.28   # 28% para ter margem de segurança

            st.divider()
            st.subheader("💡 O que fazer para conseguir aprovação?")

            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                    "📅 Parcela Máxima Recomendada",
                    f"R$ {parcela_sugerida:.2f}",
                    delta=f"- R$ {parcela - parcela_sugerida:.2f} da atual"
                )
            with col2:
                st.metric(
                    "📊 Score Mínimo Recomendado",
                    "500 pontos",
                    delta=f"{500 - score:+} pontos necessários" if score < 500 else "✅ Atingido"
                )

            st.info(f"""
            🗺️ **Plano de ação sugerido:**
            1. 📅 Reduza a parcela para até **R$ {parcela_sugerida:.2f}** (28% da sua renda)
            2. 💵 Aumente a entrada para pelo menos **20–30%** do valor da moto
            3. 📊 Melhore seu score pagando dívidas em dia
            4. ⏳ Aguarde 3–6 meses e tente novamente
            """)

# ============================================================
# 📋 TABELA DE REFERÊNCIA — FAIXAS DE SCORE
# ============================================================
with st.expander("📋 Entenda as faixas de Score de Crédito"):
    st.write("""
    | Faixa | Score | Perfil |
    |---|---|---|
    | 🔴 Alto Risco | 0 – 300 | Crédito muito difícil |
    | 🟡 Médio Risco | 301 – 700 | Análise caso a caso |
    | 🟢 Baixo Risco | 701 – 1000 | Aprovação facilitada |
    """)
    st.write("""
    **Regra de comprometimento de renda:**
    - ✅ Até 30%: ideal
    - ⚠️ 31–40%: arriscado
    - ❌ Acima de 40%: tende a ser negado
    """)

st.caption("⚠️ Simulação educacional. Procure uma instituição financeira para análise real.")

#________________________
# ============================================================
# 🎵 RECOMENDADOR DE ESTILO DE MÚSICA - SPOTIFY EXPRESS
# Analogia: como um DJ amigo que te conhece bem e já sabe
# qual playlist colocar dependendo do seu humor do dia
# Sliders = seu humor | Modelo = o DJ | Gênero = a playlist
# ============================================================

import streamlit as st
import tensorflow as tf
import numpy as np

# ============================================================
# ⚙️ CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(page_title="🎵 Spotify Express", layout="centered")
st.title("🎵 Recomendador de Playlist por Humor")
st.write("Ajuste os sliders com seu humor atual e descubra qual playlist é perfeita pra você!")
st.divider()

# ============================================================
# 📚 DADOS SIMULADOS DE TREINO
#
# Cada linha: [energia, tristeza] → gênero
#
# Gêneros (rótulos):
# 0 = Lofi      → baixa energia, alta tristeza  (estudar/relaxar)
# 1 = Sertanejo → baixa energia, baixa tristeza (tranquilo/feliz)
# 2 = Pop       → alta energia, baixa tristeza  (animado/feliz)
# 3 = Rock      → alta energia, alta tristeza   (intenso/agitado)
#
# Analogia: como um cardápio onde cada combinação de
# ingredientes (humor) resulta num prato diferente (gênero)
# ============================================================
dados_treino = np.array([
    # energia  tristeza
    [0.1,      0.9],   # Lofi
    [0.2,      0.8],   # Lofi
    [0.1,      0.7],   # Lofi
    [0.3,      0.9],   # Lofi
    [0.2,      1.0],   # Lofi

    [0.2,      0.1],   # Sertanejo
    [0.3,      0.2],   # Sertanejo
    [0.1,      0.3],   # Sertanejo
    [0.4,      0.1],   # Sertanejo
    [0.3,      0.0],   # Sertanejo

    [0.8,      0.1],   # Pop
    [0.9,      0.2],   # Pop
    [1.0,      0.1],   # Pop
    [0.7,      0.3],   # Pop
    [0.9,      0.0],   # Pop

    [0.8,      0.9],   # Rock
    [0.9,      0.8],   # Rock
    [1.0,      1.0],   # Rock
    [0.7,      0.9],   # Rock
    [0.8,      0.7],   # Rock
], dtype=float)

rotulos_treino = np.array([
    0, 0, 0, 0, 0,   # Lofi
    1, 1, 1, 1, 1,   # Sertanejo
    2, 2, 2, 2, 2,   # Pop
    3, 3, 3, 3, 3,   # Rock
], dtype=int)

# Convertendo para one-hot encoding
# Analogia: em vez de dizer "gênero 2", dizemos [0, 0, 1, 0]
# O modelo entende probabilidades por categoria, não números
rotulos_onehot = tf.keras.utils.to_categorical(rotulos_treino, num_classes=4)

# ============================================================
# 🤖 TREINANDO O MODELO
# Classificação com 4 saídas → softmax na última camada
# softmax = distribui 100% de probabilidade entre os 4 gêneros
# ============================================================
@st.cache_resource
def treinar_modelo():
    modelo = tf.keras.Sequential([
        tf.keras.layers.Dense(16, activation='relu', input_shape=[2]),
        tf.keras.layers.Dense(16, activation='relu'),
        # softmax: cada neurônio = probabilidade de um gênero
        # A soma dos 4 sempre dá 100%
        tf.keras.layers.Dense(4,  activation='softmax')
    ])

    # categorical_crossentropy = ideal para múltiplas categorias
    modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    modelo.fit(dados_treino, rotulos_onehot, epochs=500, verbose=0)
    return modelo

with st.spinner("🎧 Carregando o DJ virtual..."):
    modelo = treinar_modelo()

st.success("✅ DJ pronto! Ajuste seu humor abaixo.")
st.divider()

# ============================================================
# 🎛️ INTERFACE — SLIDERS DE HUMOR
# ============================================================
st.subheader("😄 Como você está agora?")

col1, col2 = st.columns(2)

with col1:
    energia = st.slider(
        label="⚡ Energia",
        min_value=0,
        max_value=100,
        value=50,
        step=5,
        help="0 = sem energia / 100 = agitado"
    )

with col2:
    tristeza = st.slider(
        label="😢 Tristeza",
        min_value=0,
        max_value=100,
        value=50,
        step=5,
        help="0 = feliz / 100 = muito triste"
    )

# Emoji de humor em tempo real
energia_pct  = energia  / 100
tristeza_pct = tristeza / 100

if energia_pct >= 0.6 and tristeza_pct >= 0.6:
    humor_emoji = "😤 Intenso e agitado"
elif energia_pct >= 0.6 and tristeza_pct < 0.4:
    humor_emoji = "🥳 Animado e feliz"
elif energia_pct < 0.4 and tristeza_pct >= 0.6:
    humor_emoji = "😔 Quieto e melancólico"
else:
    humor_emoji = "😌 Tranquilo e relaxado"

st.write(f"**Seu humor agora:** {humor_emoji}")
st.divider()

# ============================================================
# 🔍 BOTÃO DE RECOMENDAÇÃO
# ============================================================
if st.button("🎵 Recomendar Playlist", use_container_width=True):

    # Entrada normalizada (0 a 1) igual ao treino
    entrada = np.array([[energia_pct, tristeza_pct]])

    # Modelo retorna probabilidade para cada gênero
    probabilidades = modelo.predict(entrada, verbose=0)[0]

    # Gênero com maior probabilidade = recomendação
    genero_idx = int(np.argmax(probabilidades))

    # ====================================================
    # 🎸 CONFIGURAÇÕES DE CADA GÊNERO
    # ====================================================
    generos = {
        0: {
            "nome"     : "Lofi Hip Hop",
            "emoji"    : "🎧",
            "cor"      : "info",
            "descricao": "Perfeito para relaxar, estudar ou processar sentimentos.",
            "artistas" : "Nujabes, ChilledCow, Idealism",
            "playlist" : "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4eYOIOd",
            "bpm"      : "60–80 BPM",
            "quando"   : "Tarde fria, estudando ou descansando"
        },
        1: {
            "nome"     : "Sertanejo",
            "emoji"    : "🤠",
            "cor"      : "success",
            "descricao": "Clima gostoso, letra que conta história e muito sentimento.",
            "artistas" : "Jorge & Mateus, Henrique & Juliano, Gusttavo Lima",
            "playlist" : "https://open.spotify.com/playlist/37i9dQZF1DX6z20IXnKMAS",
            "bpm"      : "80–110 BPM",
            "quando"   : "Final de semana, churrasco ou viagem"
        },
        2: {
            "nome"     : "Pop",
            "emoji"    : "🎤",
            "cor"      : "success",
            "descricao": "Energia alta, batida contagiante e letras animadas!",
            "artistas" : "Dua Lipa, The Weeknd, Anitta, Ludmilla",
            "playlist" : "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",
            "bpm"      : "110–130 BPM",
            "quando"   : "Academia, festa ou início de dia animado"
        },
        3: {
            "nome"     : "Rock",
            "emoji"    : "🎸",
            "cor"      : "error",
            "descricao": "Intenso, pesado e cheio de emoção. Para extravasar!",
            "artistas" : "Linkin Park, Foo Fighters, Metallica, System of a Down",
            "playlist" : "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U",
            "bpm"      : "120–160 BPM",
            "quando"   : "Quando precisa extravasar ou focar com intensidade"
        },
    }

    g = generos[genero_idx]

    # ====================================================
    # 📊 EXIBINDO A RECOMENDAÇÃO
    # ====================================================
    st.subheader("🎵 Sua Playlist Recomendada")

    alerta = getattr(st, g["cor"])
    alerta(f"{g['emoji']} **{g['nome']}** — {g['descricao']}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎵 Gênero",    g["nome"])
    with col2:
        st.metric("🥁 Ritmo",     g["bpm"])
    with col3:
        st.metric("⚡ Confiança", f"{probabilidades[genero_idx]*100:.1f}%")

    st.info(f"""
    🎤 **Artistas recomendados:** {g['artistas']}
    📅 **Ideal para:** {g['quando']}
    🔗 **Abrir playlist no Spotify:** {g['playlist']}
    """)

    # ====================================================
    # 📊 GRÁFICO DE PROBABILIDADES
    # Mostra quanto % o modelo deu para cada gênero
    # ====================================================
    st.subheader("📊 Probabilidade por Gênero")

    import pandas as pd
    nomes_generos = ["🎧 Lofi", "🤠 Sertanejo", "🎤 Pop", "🎸 Rock"]

    df_prob = pd.DataFrame({
        "Probabilidade (%)": (probabilidades * 100).round(1)
    }, index=nomes_generos)

    st.bar_chart(df_prob)

# ============================================================
# 📋 LEGENDA DOS HUMORES
# ============================================================
with st.expander("🗺️ Como funciona o mapa de humores?"):
    st.write("""
    | Energia | Tristeza | Gênero Recomendado |
    |---|---|---|
    | 🔴 Alta | 🔴 Alta | 🎸 Rock |
    | 🔴 Alta | 🟢 Baixa | 🎤 Pop |
    | 🟢 Baixa | 🔴 Alta | 🎧 Lofi |
    | 🟢 Baixa | 🟢 Baixa | 🤠 Sertanejo |
    """)

st.caption("⚠️ Recomendações baseadas em modelo simulado para fins educacionais.")