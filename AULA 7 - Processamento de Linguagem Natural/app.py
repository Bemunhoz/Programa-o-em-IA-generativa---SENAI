import nltk
from nltk.tokenize import word_tokenize
 
# Download do recurso necessário para tokenização
nltk.download('punkt')
nltk.download('punkt_tab')
 
# Simulação de mensagens recebidas de clientes
mensagens = [
    "Quero cancelar meu pedido número 4521 feito ontem.",
    "O produto chegou danificado e preciso de reembolso urgente!",
    "Vocês têm entrega para o interior de São Paulo? Qual o prazo?",
]
 
print("=" * 60)
print("  SISTEMA DE TOKENIZAÇÃO DE MENSAGENS DE CLIENTES")
print("=" * 60)
 
for i, mensagem in enumerate(mensagens, start=1):
    tokens = word_tokenize(mensagem, language='portuguese')
    
    print(f"\n📩 Mensagem {i}:")
    print(f"   Texto original : {mensagem}")
    print(f"   Total de tokens: {len(tokens)}")
    print(f"   Tokens         : {tokens}")
    print("-" * 60)
 
print("\n✅ Tokenização concluída com sucesso!")

#ATIVIDADE 2
#-------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Avaliações simuladas de clientes do SAC
avaliacoes = """
O atendimento foi excelente e o produto chegou rápido.
Produto de ótima qualidade, mas o atendimento deixou a desejar.
Entrega rápida e produto bem embalado, adorei a qualidade.
O atendimento foi péssimo, produto chegou com defeito.
Qualidade excelente, entrega rápida, recomendo muito o produto.
O produto é bom, mas a entrega demorou muito mais que o esperado.
Atendimento excelente, resolveram meu problema com qualidade e rapidez.
Produto chegou danificado, atendimento demorou para responder.
Excelente qualidade do produto e entrega dentro do prazo.
Atendimento rápido e eficiente, produto de boa qualidade.
"""

# Tokenização e limpeza
tokens = word_tokenize(avaliacoes.lower(), language='portuguese')

# Remover stopwords e pontuação
stop_words = set(stopwords.words('portuguese'))
tokens_limpos = [
    palavra for palavra in tokens
    if palavra.isalpha() and palavra not in stop_words
]

# Calcular frequência
freq = FreqDist(tokens_limpos)
mais_comuns = freq.most_common(10)

# ─────────────────────────────────────────────
print("=" * 55)
print("   📊 ANÁLISE DE FREQUÊNCIA — AVALIAÇÕES DE CLIENTES")
print("=" * 55)

print(f"\n📝 Total de palavras analisadas : {len(tokens)}")
print(f"✅ Palavras após limpeza        : {len(tokens_limpos)}")
print(f"🔤 Vocabulário único            : {freq.B()}")

print("\n" + "─" * 55)
print(f"  {'#':<4} {'PALAVRA':<20} {'FREQUÊNCIA':>10}   BARRA")
print("─" * 55)

max_freq = mais_comuns[0][1]

for rank, (palavra, contagem) in enumerate(mais_comuns, start=1):
    barra = "█" * int((contagem / max_freq) * 20)
    print(f"  {rank:<4} {palavra:<20} {contagem:>10}   {barra}")

print("─" * 55)
print("\n💡 Insights para o SAC:")

# Insight automático simples
palavras_positivas = {'excelente', 'ótima', 'adorei', 'recomendo', 'eficiente', 'bom', 'boa'}
palavras_negativas = {'péssimo', 'defeito', 'danificado', 'demorou', 'desejar', 'problema'}

positivas_encontradas = [p for p, _ in mais_comuns if p in palavras_positivas]
negativas_encontradas = [p for p, _ in mais_comuns if p in palavras_negativas]

if positivas_encontradas:
    print(f"   👍 Termos positivos frequentes : {', '.join(positivas_encontradas)}")
if negativas_encontradas:
    print(f"   👎 Termos negativos frequentes : {', '.join(negativas_encontradas)}")

print(f"\n   🔝 Tema mais citado: '{mais_comuns[0][0]}' ({mais_comuns[0][1]}x)")
print("\n✅ Análise concluída com sucesso!")
print("=" * 55)

#ATIVIDADE 3
#------------------------------------------
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

# ── Dicionário de palavras negativas por categoria ──────────────
palavras_negativas = {
    "qualidade":    ["ruim", "péssimo", "péssima", "horrível", "defeito", "danificado", "quebrado"],
    "atendimento":  ["descaso", "ignorado", "grosseiro", "despreparado", "demora", "demorou"],
    "entrega":      ["atrasado", "atraso", "extraviado", "perdido", "errado"],
    "geral":        ["erro", "problema", "falha", "insatisfeito", "decepcionante", "lamentável", "absurdo"],
}

# Mapa plano: palavra → categoria
mapa_palavras = {
    palavra: categoria
    for categoria, lista in palavras_negativas.items()
    for palavra in lista
}

# ── Mensagens simuladas de clientes ─────────────────────────────
mensagens = [
    {"id": "MSG-001", "texto": "O produto chegou quebrado e o atendimento foi péssimo!"},
    {"id": "MSG-002", "texto": "Entrega rápida e produto de ótima qualidade, recomendo!"},
    {"id": "MSG-003", "texto": "Meu pedido está atrasado e ninguém resolve o erro no sistema."},
    {"id": "MSG-004", "texto": "Atendimento foi razoável, mas o produto veio com defeito."},
    {"id": "MSG-005", "texto": "Adorei a compra, chegou antes do prazo e estava perfeito."},
    {"id": "MSG-006", "texto": "Situação lamentável! Pedido extraviado e nenhuma resposta do suporte."},
    {"id": "MSG-007", "texto": "Tudo certo com o pedido, muito satisfeito com o serviço!"},
    {"id": "MSG-008", "texto": "Produto com falha grave, atendente foi grosseiro comigo."},
]

# ── Função de análise ────────────────────────────────────────────
def analisar_mensagem(msg):
    tokens = word_tokenize(msg["texto"].lower(), language="portuguese")
    encontradas = {}
    for token in tokens:
        if token in mapa_palavras:
            cat = mapa_palavras[token]
            encontradas.setdefault(cat, []).append(token)

    return {
        "id":          msg["id"],
        "texto":       msg["texto"],
        "negativa":    len(encontradas) > 0,
        "categorias":  encontradas,
        "prioridade":  "🔴 ALTA" if len(encontradas) >= 2 else ("🟡 MÉDIA" if encontradas else "🟢 BAIXA"),
    }

# ── Processamento ────────────────────────────────────────────────
resultados   = [analisar_mensagem(m) for m in mensagens]
negativas    = [r for r in resultados if r["negativa"]]
positivas    = [r for r in resultados if not r["negativa"]]
alta_prior   = [r for r in negativas if "ALTA"  in r["prioridade"]]
media_prior  = [r for r in negativas if "MÉDIA" in r["prioridade"]]

# ── Print ────────────────────────────────────────────────────────
print("=" * 62)
print("   🚨 DETECTOR DE MENSAGENS NEGATIVAS — SUPORTE AO CLIENTE")
print("=" * 62)
print(f"\n📨 Total de mensagens analisadas : {len(resultados)}")
print(f"🔴 Mensagens negativas           : {len(negativas)}")
print(f"🟢 Mensagens positivas           : {len(positivas)}")
print(f"⚡ Prioridade ALTA               : {len(alta_prior)}")
print(f"⚠️  Prioridade MÉDIA              : {len(media_prior)}")

print("\n" + "─" * 62)
print("  DETALHAMENTO POR MENSAGEM")
print("─" * 62)

for r in resultados:
    print(f"\n  [{r['id']}] {r['prioridade']}")
    print(f"  📩 {r['texto']}")
    if r["negativa"]:
        for cat, palavras in r["categorias"].items():
            print(f"     ⚠️  {cat.upper()}: {', '.join(palavras)}")
    else:
        print("     ✅ Nenhuma palavra negativa detectada.")
    print("  " + "·" * 58)

print("\n" + "─" * 62)
print("  📋 FILA DE ATENDIMENTO PRIORITÁRIO")
print("─" * 62)

fila = sorted(negativas, key=lambda x: (0 if "ALTA" in x["prioridade"] else 1))
for pos, r in enumerate(fila, start=1):
    print(f"  {pos}º {r['prioridade']}  [{r['id']}] — {r['texto'][:50]}...")

print("\n✅ Análise concluída. Fila de prioridade gerada com sucesso!")
print("=" * 62)

#ATIVIDADE 4
#------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Textos simulados de avaliações de clientes ───────────────────
textos = [
    {"id": "TXT-001", "texto": "O produto que eu comprei para a minha casa chegou com defeito e não funcionou."},
    {"id": "TXT-002", "texto": "O atendimento da empresa foi muito bom e resolveram o meu problema rapidamente."},
    {"id": "TXT-003", "texto": "Fiz o pedido para entrega em casa mas o prazo não foi cumprido pela loja."},
]

# ── Stopwords em português ───────────────────────────────────────
stop_words = set(stopwords.words('portuguese'))

# ── Função de limpeza ────────────────────────────────────────────
def remover_stopwords(texto):
    tokens = word_tokenize(texto.lower(), language='portuguese')
    tokens_limpos = [t for t in tokens if t.isalpha() and t not in stop_words]
    removidas     = [t for t in tokens if t.isalpha() and t     in stop_words]
    return tokens, tokens_limpos, removidas

# ── Print ────────────────────────────────────────────────────────
print("=" * 62)
print("   🧹 REMOÇÃO DE STOPWORDS — ANÁLISE DE TEXTOS EM PORTUGUÊS")
print("=" * 62)
print(f"\n📚 Stopwords carregadas (NLTK/PT): {len(stop_words)} palavras\n")

total_tokens   = 0
total_removidas = 0
total_uteis     = 0

for item in textos:
    tokens, limpos, removidas = remover_stopwords(item["texto"])

    total_tokens    += len(tokens)
    total_removidas += len(removidas)
    total_uteis     += len(limpos)

    reducao = round((len(removidas) / len(tokens)) * 100) if tokens else 0

    print("─" * 62)
    print(f"  📄 [{item['id']}]")
    print(f"  📝 Original  : {item['texto']}")
    print(f"\n  🔵 Todos os tokens  : {tokens}")
    print(f"  🔴 Stopwords        : {removidas}")
    print(f"  ✅ Palavras úteis   : {limpos}")
    print(f"\n  📊 Tokens originais : {len(tokens)}")
    print(f"     Removidas        : {len(removidas)}  ({reducao}% do texto)")
    print(f"     Úteis restantes  : {len(limpos)}")

print("\n" + "=" * 62)
print("  📋 RESUMO GERAL DA ANÁLISE")
print("=" * 62)
print(f"  📨 Textos processados   : {len(textos)}")
print(f"  🔢 Total de tokens      : {total_tokens}")
print(f"  🗑️  Total de stopwords   : {total_removidas}")
print(f"  💡 Palavras úteis       : {total_uteis}")
print(f"  📉 Redução média        : {round((total_removidas / total_tokens) * 100)}% do volume total")
print("=" * 62)
print("\n✅ Limpeza concluída! Textos prontos para análise.")

#ATIVIDADE 5
#---------------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Dicionário de sentimentos por categoria ──────────────────────
palavras_positivas = {
    "elogio":     ["excelente", "ótimo", "ótima", "incrível", "perfeito", "perfeita", "adorei", "amei"],
    "satisfação": ["satisfeito", "satisfeita", "feliz", "contente", "recomendo", "aprovado"],
    "qualidade":  ["qualidade", "eficiente", "rápido", "rápida", "pontual", "caprichado"],
    "atendimento":["atencioso", "prestativo", "educado", "simpático", "resolveram"],
}

palavras_negativas = {
    "reclamação":  ["péssimo", "péssima", "horrível", "terrível", "lamentável", "absurdo"],
    "insatisfação":["insatisfeito", "decepcionado", "decepcionante", "frustrado", "arrependido"],
    "problema":    ["defeito", "quebrado", "danificado", "erro", "falha", "problema"],
    "atendimento": ["grosseiro", "ignorado", "demorou", "demora", "descaso", "despreparado"],
}

palavras_neutras = ["regular", "razoável", "médio", "comum", "simples", "ok", "normal"]

# Mapas planos: palavra → categoria
mapa_pos = {p: cat for cat, lst in palavras_positivas.items() for p in lst}
mapa_neg = {p: cat for cat, lst in palavras_negativas.items() for p in lst}

stop_words = set(stopwords.words('portuguese'))

# ── Comentários simulados de clientes ───────────────────────────
comentarios = [
    {"id": "C-001", "texto": "O produto é excelente e o atendimento foi muito atencioso!"},
    {"id": "C-002", "texto": "Péssima experiência, produto chegou com defeito e ninguém resolveu."},
    {"id": "C-003", "texto": "Entrega pontual e qualidade acima do esperado. Recomendo!"},
    {"id": "C-004", "texto": "O atendimento foi razoável, nada de especial, serviço comum."},
    {"id": "C-005", "texto": "Estou muito decepcionado, a entrega demorou e o produto veio errado."},
    {"id": "C-006", "texto": "Adorei tudo! Rápido, eficiente e perfeito do início ao fim."},
    {"id": "C-007", "texto": "Produto ok, mas o atendente foi grosseiro e ignorou minha reclamação."},
    {"id": "C-008", "texto": "Serviço simplesmente incrível! Me sinto muito satisfeita com a compra."},
]

# ── Função de classificação ──────────────────────────────────────
def classificar(comentario):
    tokens = word_tokenize(comentario["texto"].lower(), language="portuguese")
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]

    hits_pos = {t: mapa_pos[t] for t in tokens if t in mapa_pos}
    hits_neg = {t: mapa_neg[t] for t in tokens if t in mapa_neg}
    hits_neu = [t for t in tokens if t in palavras_neutras]

    score = len(hits_pos) - len(hits_neg)

    if score > 0:
        sentimento = "POSITIVO"
        emoji      = "😊"
        label      = "🟢"
    elif score < 0:
        sentimento = "NEGATIVO"
        emoji      = "😠"
        label      = "🔴"
    else:
        sentimento = "NEUTRO"
        emoji      = "😐"
        label      = "🟡"

    return {
        "id":         comentario["id"],
        "texto":      comentario["texto"],
        "sentimento": sentimento,
        "emoji":      emoji,
        "label":      label,
        "score":      score,
        "positivos":  hits_pos,
        "negativos":  hits_neg,
        "neutros":    hits_neu,
    }

# ── Processar todos os comentários ──────────────────────────────
resultados  = [classificar(c) for c in comentarios]
positivos   = [r for r in resultados if r["sentimento"] == "POSITIVO"]
negativos   = [r for r in resultados if r["sentimento"] == "NEGATIVO"]
neutros     = [r for r in resultados if r["sentimento"] == "NEUTRO"]

# ── Print ────────────────────────────────────────────────────────
print("=" * 64)
print("   💬 CLASSIFICADOR DE SENTIMENTO — COMENTÁRIOS DE CLIENTES")
print("=" * 64)
print(f"\n  📨 Total analisado : {len(resultados)} comentários")
print(f"  🟢 Positivos       : {len(positivos)}")
print(f"  🔴 Negativos       : {len(negativos)}")
print(f"  🟡 Neutros         : {len(neutros)}")

satisfacao = round((len(positivos) / len(resultados)) * 100)
print(f"  📈 Índice positivo : {satisfacao}% dos comentários")

print("\n" + "─" * 64)
print("  ANÁLISE DETALHADA POR COMENTÁRIO")
print("─" * 64)

for r in resultados:
    print(f"\n  {r['label']} [{r['id']}]  {r['emoji']}  SENTIMENTO: {r['sentimento']}  (score: {r['score']:+})")
    print(f"  📝 \"{r['texto']}\"")

    if r["positivos"]:
        itens = ", ".join([f"{p} ({c})" for p, c in r["positivos"].items()])
        print(f"  👍 Termos positivos : {itens}")
    if r["negativos"]:
        itens = ", ".join([f"{p} ({c})" for p, c in r["negativos"].items()])
        print(f"  👎 Termos negativos : {itens}")
    if r["neutros"]:
        print(f"  😐 Termos neutros   : {', '.join(r['neutros'])}")
    if not r["positivos"] and not r["negativos"] and not r["neutros"]:
        print(f"  ℹ️  Nenhum termo classificável encontrado.")
    print("  " + "·" * 60)

print("\n" + "─" * 64)
print("  📋 RANKING — COMENTÁRIOS MAIS CRÍTICOS (NEGATIVOS)")
print("─" * 64)
criticos = sorted(negativos, key=lambda x: x["score"])
if criticos:
    for i, r in enumerate(criticos, 1):
        print(f"  {i}º [{r['id']}] score {r['score']:+} — {r['texto'][:55]}...")
else:
    print("  ✅ Nenhum comentário negativo identificado.")

print("\n" + "─" * 64)
print("  🏆 RANKING — MELHORES AVALIAÇÕES (POSITIVOS)")
print("─" * 64)
melhores = sorted(positivos, key=lambda x: x["score"], reverse=True)
for i, r in enumerate(melhores, 1):
    print(f"  {i}º [{r['id']}] score {r['score']:+} — {r['texto'][:55]}...")

print("\n" + "=" * 64)
print("  ✅ Classificação concluída! Relatório pronto para o marketing.")
print("=" * 64)

#ATIVIDADE 6
#-------------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Dicionário de setores e palavras-chave ───────────────────────
setores = {
    "CANCELAMENTO": {
        "emoji":    "🚫",
        "cor":      "VERMELHO",
        "palavras": ["cancelar", "cancelamento", "cancelei", "desistir",
                     "devolver", "devolução", "reembolso", "arrependido", "desistência"],
        "mensagem": "Vamos te conectar ao setor de Cancelamentos. Um agente irá te atender em instantes.",
    },
    "PAGAMENTO": {
        "emoji":    "💳",
        "cor":      "AZUL",
        "palavras": ["pagamento", "pagar", "boleto", "pix", "cartão",
                     "cobrança", "cobrado", "fatura", "parcela", "débito"],
        "mensagem": "Direcionando para o setor Financeiro. Verifique seu comprovante antes de prosseguir.",
    },
    "SUPORTE TÉCNICO": {
        "emoji":    "🔧",
        "cor":      "LARANJA",
        "palavras": ["erro", "falha", "bug", "travou", "não funciona",
                     "problema", "defeito", "quebrou", "parou", "lento"],
        "mensagem": "Abrindo chamado no Suporte Técnico. Nossos especialistas vão te ajudar.",
    },
    "ENTREGA": {
        "emoji":    "📦",
        "cor":      "VERDE",
        "palavras": ["entrega", "pedido", "rastreio", "rastrear", "chegou",
                     "atrasado", "atraso", "transportadora", "frete", "enviado"],
        "mensagem": "Conectando ao setor de Logística. Tenha o número do pedido em mãos.",
    },
    "ATENDIMENTO": {
        "emoji":    "🎧",
        "cor":      "ROXO",
        "palavras": ["atendente", "atendimento", "reclamação", "reclamar",
                     "desrespeito", "grosseiro", "mal atendido", "demora", "insatisfeito"],
        "mensagem": "Encaminhando para a Ouvidoria. Seu feedback é muito importante para nós.",
    },
}

# Mapa plano: palavra → setor
mapa_palavras = {
    palavra: setor
    for setor, dados in setores.items()
    for palavra in dados["palavras"]
}

stop_words = set(stopwords.words('portuguese'))

# ── Mensagens simuladas de clientes ─────────────────────────────
mensagens = [
    {"id": "MSG-001", "texto": "Quero cancelar meu pedido, não quero mais o produto."},
    {"id": "MSG-002", "texto": "Fui cobrado duas vezes no cartão e preciso de ajuda com o pagamento."},
    {"id": "MSG-003", "texto": "O aplicativo travou e está com erro, não consigo acessar."},
    {"id": "MSG-004", "texto": "Meu pedido está atrasado, quero rastrear a entrega."},
    {"id": "MSG-005", "texto": "O atendente foi grosseiro e quero registrar uma reclamação."},
    {"id": "MSG-006", "texto": "Preciso cancelar e também verificar um erro no meu boleto."},
    {"id": "MSG-007", "texto": "Bom dia, gostaria de informações sobre os produtos da loja."},
    {"id": "MSG-008", "texto": "O produto chegou com defeito e quero reembolso."},
]

# ── Função de roteamento ─────────────────────────────────────────
def rotear_mensagem(msg):
    tokens   = word_tokenize(msg["texto"].lower(), language="portuguese")
    tokens   = [t for t in tokens if t.isalpha() and t not in stop_words]

    hits = {}
    for token in tokens:
        if token in mapa_palavras:
            setor = mapa_palavras[token]
            hits.setdefault(setor, []).append(token)

    if not hits:
        return {
            "id":       msg["id"],
            "texto":    msg["texto"],
            "setores":  {},
            "destino":  "GERAL",
            "mensagem": "Aguarde, um atendente irá te ajudar em breve.",
            "multi":    False,
        }

    destino = max(hits, key=lambda s: len(hits[s]))
    multi   = len(hits) > 1

    return {
        "id":       msg["id"],
        "texto":    msg["texto"],
        "setores":  hits,
        "destino":  destino,
        "mensagem": setores[destino]["mensagem"],
        "multi":    multi,
    }

# ── Processar todas as mensagens ────────────────────────────────
resultados = [rotear_mensagem(m) for m in mensagens]

# ── Contadores por setor ─────────────────────────────────────────
contagem = {}
for r in resultados:
    contagem[r["destino"]] = contagem.get(r["destino"], 0) + 1

# ── Print ────────────────────────────────────────────────────────
print("=" * 64)
print("   🤖 CHATBOT DE ROTEAMENTO — DIRECIONAMENTO POR SETOR")
print("=" * 64)
print(f"\n  📨 Mensagens recebidas : {len(resultados)}")
print(f"  🔀 Com múltiplos temas : {sum(1 for r in resultados if r['multi'])}")
print(f"  ❓ Sem classificação   : {sum(1 for r in resultados if r['destino'] == 'GERAL')}")

print("\n" + "─" * 64)
print("  ROTEAMENTO DETALHADO POR MENSAGEM")
print("─" * 64)

for r in resultados:
    destino = r["destino"]
    emoji   = setores[destino]["emoji"] if destino in setores else "❓"

    print(f"\n  {emoji}  [{r['id']}]  ➜  SETOR: {destino}")
    print(f"  💬 Cliente : \"{r['texto']}\"")

    if r["setores"]:
        for setor, palavras in r["setores"].items():
            marcador = "✅" if setor == destino else "📌"
            print(f"  {marcador} {setor:<20} → palavras detectadas: {', '.join(palavras)}")
        if r["multi"]:
            print(f"  ⚡ Múltiplos temas detectados — roteado para o mais relevante.")
    else:
        print(f"  ℹ️  Nenhuma palavra-chave identificada — encaminhado para atendimento geral.")

    print(f"  🗣️  Bot: \"{r['mensagem']}\"")
    print("  " + "·" * 60)

print("\n" + "─" * 64)
print("  📊 VOLUME DE CHAMADOS POR SETOR")
print("─" * 64)

ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
total    = len(resultados)

for setor, qtd in ordenado:
    emoji   = setores[setor]["emoji"] if setor in setores else "❓"
    barra   = "█" * qtd
    pct     = round((qtd / total) * 100)
    print(f"  {emoji}  {setor:<20} {barra:<10} {qtd} chamado(s)  ({pct}%)")

print("\n" + "=" * 64)
print("  ✅ Roteamento concluído! Todos os clientes foram direcionados.")
print("=" * 64)

#ATIVIDADE 7
#-------------------------------------------------------------------------

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Reclamações simuladas de clientes ────────────────────────────
reclamacoes = [
    {"id": "R-001", "categoria": "Produto",     "texto": "O produto chegou com defeito e apresentou problema logo no primeiro uso. Péssima qualidade."},
    {"id": "R-002", "categoria": "Entrega",     "texto": "Minha entrega atrasou mais de 10 dias. O prazo não foi cumprido e ninguém avisou sobre o atraso."},
    {"id": "R-003", "categoria": "Atendimento", "texto": "O atendimento foi horrível, o atendente foi grosseiro e não resolveu meu problema."},
    {"id": "R-004", "categoria": "Produto",     "texto": "Produto com defeito, tela quebrada e bateria com problema. Qualidade muito ruim para o preço pago."},
    {"id": "R-005", "categoria": "Pagamento",   "texto": "Fui cobrado duas vezes no cartão. A cobrança indevida gerou um problema no meu limite."},
    {"id": "R-006", "categoria": "Entrega",     "texto": "Entrega atrasada novamente! O produto foi entregue errado e a embalagem chegou danificada."},
    {"id": "R-007", "categoria": "Atendimento", "texto": "Liguei três vezes e ninguém resolveu o problema. Atendimento demorado e sem solução."},
    {"id": "R-008", "categoria": "Produto",     "texto": "O produto parou de funcionar após dois dias. Defeito claro de fabricação. Péssimo produto."},
    {"id": "R-009", "categoria": "Pagamento",   "texto": "Boleto com valor errado, cobrança duplicada e nenhuma resposta do financeiro sobre o problema."},
    {"id": "R-010", "categoria": "Entrega",     "texto": "Atraso de uma semana na entrega, produto chegou danificado e a embalagem estava aberta."},
]

stop_words = set(stopwords.words('portuguese'))

# ── Categorias para agrupamento temático ─────────────────────────
temas = {
    "⚙️  Qualidade":    ["defeito", "quebrado", "danificado", "fabricação", "funcionar", "parou", "bateria", "tela"],
    "🚚 Entrega":       ["entrega", "atraso", "atrasou", "atrasada", "prazo", "embalagem", "entregue", "enviado"],
    "🎧 Atendimento":   ["atendimento", "atendente", "grosseiro", "demorado", "liguei", "resolveu", "solução"],
    "💳 Pagamento":     ["cobrança", "cobrado", "cartão", "boleto", "duplicada", "financeiro", "limite", "valor"],
    "❗ Insatisfação":  ["péssimo", "péssima", "horrível", "ruim", "problema", "errado", "indevida"],
}

mapa_temas = {p: t for t, ps in temas.items() for p in ps}

# ── Processar texto completo ─────────────────────────────────────
texto_total = " ".join([r["texto"] for r in reclamacoes])
tokens_all  = word_tokenize(texto_total.lower(), language="portuguese")
tokens_limpos = [t for t in tokens_all if t.isalpha() and t not in stop_words]

freq        = FreqDist(tokens_limpos)
top_geral   = freq.most_common(12)

# ── Frequência por categoria de reclamação ───────────────────────
freq_por_cat = defaultdict(list)
for r in reclamacoes:
    tokens = word_tokenize(r["texto"].lower(), language="portuguese")
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]
    freq_por_cat[r["categoria"]].extend(tokens)

# ── Contagem por tema ────────────────────────────────────────────
contagem_temas = {}
for tema, palavras_tema in temas.items():
    total = sum(freq[p] for p in palavras_tema if p in freq)
    contagem_temas[tema] = total

# ── Print ────────────────────────────────────────────────────────
print("=" * 64)
print("   🔍 ANÁLISE DE RECLAMAÇÕES — PALAVRAS MAIS FREQUENTES")
print("=" * 64)
print(f"\n  📋 Reclamações analisadas  : {len(reclamacoes)}")
print(f"  🔢 Total de tokens         : {len(tokens_all)}")
print(f"  ✅ Palavras úteis          : {len(tokens_limpos)}")
print(f"  🔤 Vocabulário único       : {freq.B()}")

# ── Ranking geral ────────────────────────────────────────────────
print("\n" + "─" * 64)
print("  🏆 TOP 12 — PALAVRAS MAIS FREQUENTES NAS RECLAMAÇÕES")
print("─" * 64)
print(f"  {'#':<4} {'PALAVRA':<18} {'QTD':>5}   FREQUÊNCIA")
print("─" * 64)

max_freq = top_geral[0][1]
for rank, (palavra, qtd) in enumerate(top_geral, 1):
    barra  = "█" * int((qtd / max_freq) * 22)
    tema   = mapa_temas.get(palavra, "")
    alerta = " ⚠️" if qtd >= 4 else ""
    print(f"  {rank:<4} {palavra:<18} {qtd:>5}   {barra}{alerta}")

# ── Agrupamento por tema ─────────────────────────────────────────
print("\n" + "─" * 64)
print("  📂 FREQUÊNCIA AGRUPADA POR TEMA")
print("─" * 64)

temas_ord = sorted(contagem_temas.items(), key=lambda x: x[1], reverse=True)
max_tema  = temas_ord[0][1] if temas_ord else 1

for tema, total in temas_ord:
    barra = "█" * int((total / max_tema) * 18)
    print(f"  {tema:<22} {barra:<20} {total} ocorrência(s)")

# ── Frequência por categoria ─────────────────────────────────────
print("\n" + "─" * 64)
print("  📁 TOP 3 PALAVRAS POR CATEGORIA DE RECLAMAÇÃO")
print("─" * 64)

emojis_cat = {
    "Produto": "📦", "Entrega": "🚚",
    "Atendimento": "🎧", "Pagamento": "💳"
}

for cat, palavras in freq_por_cat.items():
    fdist = FreqDist(palavras)
    top3  = fdist.most_common(3)
    emoji = emojis_cat.get(cat, "📌")
    termos = "  |  ".join([f"{p} ({n}x)" for p, n in top3])
    print(f"  {emoji}  {cat:<14} ➜  {termos}")

# ── Insights automáticos ─────────────────────────────────────────
print("\n" + "─" * 64)
print("  💡 INSIGHTS PARA O ANALISTA DE QUALIDADE")
print("─" * 64)

palavra_critica = top_geral[0][0]
tema_critico    = temas_ord[0][0].strip()
cat_critica     = max(freq_por_cat, key=lambda c: len(freq_por_cat[c]))

print(f"  🔴 Palavra mais recorrente  : '{palavra_critica}' ({freq[palavra_critica]}x)")
print(f"  🔴 Tema mais problemático   : {tema_critico} ({temas_ord[0][1]} ocorrências)")
print(f"  🔴 Categoria com mais queixas: {emojis_cat.get(cat_critica,'📌')} {cat_critica}")
print(f"\n  📌 Recomendações:")
print(f"     → Revisar processos ligados a '{palavra_critica}' com urgência.")
print(f"     → Priorizar melhorias no tema: {tema_critico}.")
print(f"     → Criar plano de ação focado na categoria: {cat_critica}.")

print("\n" + "=" * 64)
print("  ✅ Análise concluída! Relatório pronto para o time de Qualidade.")
print("=" * 64)

#ATIVIDADE 8
#----------------------------------------

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Dicionário de setores e palavras-chave ───────────────────────
setores = {
    "SUPORTE TÉCNICO": {
        "emoji": "🔧",
        "cor":   "AZUL",
        "prioridade": {
            "CRÍTICA": ["sistema caiu", "fora do ar", "servidor down", "sem acesso"],
            "ALTA":    ["erro", "falha", "travou", "bug", "crashou", "corrompido"],
            "MÉDIA":   ["lento", "instável", "reiniciando", "parou", "não abre", "tela"],
            "BAIXA":   ["dúvida", "configurar", "instalar", "atualizar", "senha", "acesso"],
        },
        "resposta": "🔧 Ticket aberto no Suporte Técnico. Equipe de TI notificada.",
        "sla":      {"CRÍTICA": "15 min", "ALTA": "1 hora", "MÉDIA": "4 horas", "BAIXA": "1 dia"},
    },
    "FINANCEIRO": {
        "emoji": "💰",
        "cor":   "VERDE",
        "prioridade": {
            "CRÍTICA": ["fraude", "golpe", "clonado", "roubo", "invasão conta"],
            "ALTA":    ["cobrança indevida", "duplicada", "bloqueado", "estornado"],
            "MÉDIA":   ["boleto", "fatura", "pagamento", "reembolso", "nota fiscal"],
            "BAIXA":   ["saldo", "extrato", "limite", "parcela", "desconto", "plano"],
        },
        "resposta": "💰 Chamado registrado no Financeiro. Time responsável acionado.",
        "sla":      {"CRÍTICA": "30 min", "ALTA": "2 horas", "MÉDIA": "8 horas", "BAIXA": "2 dias"},
    },
    "INFRAESTRUTURA": {
        "emoji": "🖥️",
        "cor":   "LARANJA",
        "prioridade": {
            "CRÍTICA": ["datacenter", "rede caiu", "switch desligou", "firewall bloqueou"],
            "ALTA":    ["vpn", "internet", "cabo", "roteador", "conexão", "ping"],
            "MÉDIA":   ["impressora", "periférico", "monitor", "teclado", "mouse"],
            "BAIXA":   ["cabo solto", "fonte", "driver", "usb", "porta"],
        },
        "resposta": "🖥️ Ocorrência encaminhada para Infraestrutura. Técnico será designado.",
        "sla":      {"CRÍTICA": "10 min", "ALTA": "1 hora", "MÉDIA": "4 horas", "BAIXA": "1 dia"},
    },
}

# Mapa plano: palavra → (setor, prioridade)
mapa = {}
for setor, dados in setores.items():
    for prioridade, palavras in dados["prioridade"].items():
        for palavra in palavras:
            mapa[palavra] = (setor, prioridade)

stop_words = set(stopwords.words('portuguese'))

# Peso por prioridade para ranking
peso = {"CRÍTICA": 4, "ALTA": 3, "MÉDIA": 2, "BAIXA": 1}

# ── Mensagens simuladas do ambiente corporativo ──────────────────
mensagens = [
    {"id": "TKT-001", "usuario": "Carlos (Dev)",      "texto": "O sistema travou durante o deploy e agora está fora do ar para todos os usuários."},
    {"id": "TKT-002", "usuario": "Ana (Financeiro)",  "texto": "Recebi uma cobrança duplicada no cartão corporativo e preciso de reembolso urgente."},
    {"id": "TKT-003", "usuario": "Pedro (Infra)",     "texto": "A VPN caiu e a internet está instável em todo o andar. O roteador está piscando."},
    {"id": "TKT-004", "usuario": "Julia (RH)",        "texto": "Não consigo instalar o software de ponto eletrônico. Aparece um erro de acesso."},
    {"id": "TKT-005", "usuario": "Marcos (Compras)",  "texto": "O boleto do fornecedor está vencido e preciso emitir uma nova nota fiscal."},
    {"id": "TKT-006", "usuario": "Lucia (Diretora)",  "texto": "Suspeito de fraude na conta da empresa. Transações não reconhecidas apareceram hoje."},
    {"id": "TKT-007", "usuario": "Rafael (TI)",       "texto": "O servidor de banco de dados crashou e os logs mostram falha crítica no disco."},
    {"id": "TKT-008", "usuario": "Beatriz (Vendas)",  "texto": "Quero saber o saldo disponível no limite do cartão corporativo para fechar um pedido."},
    {"id": "TKT-009", "usuario": "Diego (Suporte)",   "texto": "O firewall bloqueou o acesso ao sistema de CRM. Preciso de liberação de porta."},
    {"id": "TKT-010", "usuario": "Fernanda (ADM)",    "texto": "Dúvida sobre como configurar a senha do sistema financeiro após a atualização."},
]

# ── Função de classificação ──────────────────────────────────────
def classificar(msg):
    texto  = msg["texto"].lower()
    tokens = word_tokenize(texto, language="portuguese")
    tokens = [t for t in tokens if t.isalpha() and t not in stop_words]

    # Busca exata e por token
    hits = defaultdict(lambda: defaultdict(list))

    # Verificação por frases (multi-palavra)
    for chave, (setor, prior) in mapa.items():
        if chave in texto:
            hits[setor][prior].append(chave)

    # Score por setor
    scores = {}
    for setor, priors in hits.items():
        score = sum(peso[p] * len(palavras) for p, palavras in priors.items())
        scores[setor] = score

    if not scores:
        return {
            "id":        msg["id"],
            "usuario":   msg["usuario"],
            "texto":     msg["texto"],
            "setor":     "NÃO CLASSIFICADO",
            "prioridade":"BAIXA",
            "hits":      {},
            "score":     0,
            "resposta":  "⚠️  Mensagem encaminhada para triagem manual.",
            "sla":       "—",
        }

    setor_final = max(scores, key=scores.get)
    priors_hits = hits[setor_final]
    prior_final = max(priors_hits, key=lambda p: peso[p])
    sla         = setores[setor_final]["sla"][prior_final]

    return {
        "id":        msg["id"],
        "usuario":   msg["usuario"],
        "texto":     msg["texto"],
        "setor":     setor_final,
        "prioridade":prior_final,
        "hits":      dict(hits),
        "score":     scores[setor_final],
        "resposta":  setores[setor_final]["resposta"],
        "sla":       sla,
    }

# ── Processar ────────────────────────────────────────────────────
resultados = [classificar(m) for m in mensagens]

# ── Contadores ───────────────────────────────────────────────────
contagem_setor  = defaultdict(int)
contagem_prior  = defaultdict(int)
for r in resultados:
    contagem_setor[r["setor"]] += 1
    contagem_prior[r["prioridade"]] += 1

icones_prior = {"CRÍTICA": "🔴", "ALTA": "🟠", "MÉDIA": "🟡", "BAIXA": "🟢"}

# ── Print ────────────────────────────────────────────────────────
print("=" * 66)
print("   🖥️  CLASSIFICADOR DE CHAMADOS — TI CORPORATIVO")
print("=" * 66)
print(f"\n  📨 Total de mensagens     : {len(resultados)}")
for setor, qtd in sorted(contagem_setor.items(), key=lambda x: x[1], reverse=True):
    emoji = setores[setor]["emoji"] if setor in setores else "❓"
    print(f"  {emoji}  {setor:<22}: {qtd} chamado(s)")

print()
for prior in ["CRÍTICA", "ALTA", "MÉDIA", "BAIXA"]:
    qtd = contagem_prior.get(prior, 0)
    if qtd:
        print(f"  {icones_prior[prior]}  Prioridade {prior:<10}: {qtd} chamado(s)")

print("\n" + "─" * 66)
print("  DETALHAMENTO DOS CHAMADOS")
print("─" * 66)

for r in resultados:
    emoji_s = setores[r["setor"]]["emoji"] if r["setor"] in setores else "❓"
    emoji_p = icones_prior.get(r["prioridade"], "⚪")
    sla_tag = f"SLA: {r['sla']}" if r["sla"] != "—" else "triagem manual"

    print(f"\n  {emoji_s} [{r['id']}]  {emoji_p} {r['prioridade']:<10}  ⏱  {sla_tag}")
    print(f"  👤 {r['usuario']}")
    print(f"  💬 \"{r['texto']}\"")

    if r["hits"]:
        for setor_hit, priors in r["hits"].items():
            e = setores[setor_hit]["emoji"] if setor_hit in setores else "📌"
            marcador = "✅" if setor_hit == r["setor"] else "📌"
            for prior_hit, palavras in priors.items():
                print(f"  {marcador} {e} {setor_hit:<22} [{prior_hit}] → {', '.join(palavras)}")
    else:
        print(f"  ⚠️  Nenhuma palavra-chave detectada.")

    print(f"  🤖 Bot: {r['resposta']}")
    print("  " + "·" * 62)

print("\n" + "─" * 66)
print("  🚨 FILA DE ATENDIMENTO — ORDEM DE PRIORIDADE")
print("─" * 66)

ordem = ["CRÍTICA", "ALTA", "MÉDIA", "BAIXA", "NÃO CLASSIFICADO"]
fila  = sorted(resultados, key=lambda r: (
    ordem.index(r["prioridade"]) if r["prioridade"] in ordem else 99,
    r["id"]
))

for pos, r in enumerate(fila, 1):
    emoji_s = setores[r["setor"]]["emoji"] if r["setor"] in setores else "❓"
    emoji_p = icones_prior.get(r["prioridade"], "⚪")
    print(f"  {pos:>2}º  {emoji_p} {r['prioridade']:<10}  {emoji_s} {r['setor']:<22}  [{r['id']}] {r['usuario']}")

print("\n" + "=" * 66)
print("  ✅ Classificação concluída! Fila gerada e equipes notificadas.")
print("=" * 66)

#ATIVIDADE 9
#----------------------------------------------

import nltk
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Textos brutos simulados para análise ─────────────────────────
textos = [
    {
        "id":       "DOC-001",
        "origem":   "E-mail de cliente",
        "texto":    "Olá!! Comprei o produto em 12/03/2024 e ele CHEGOU com DEFEITO!!! Quero meu dinheiro de volta. Att, João Silva."
    },
    {
        "id":       "DOC-002",
        "origem":   "Avaliação do app",
        "texto":    "Péssimo... O app trava TODA hora! (versão 3.2.1) -- Já desinstalei 2x e nada resolve. #frustrante"
    },
    {
        "id":       "DOC-003",
        "origem":   "Chat de suporte",
        "texto":    "Boa tarde! Meu pedido #45821 está ATRASADO há 7 dias... quando vai chegar?? A entrega foi prometida p/ 10/04."
    },
    {
        "id":       "DOC-004",
        "origem":   "Formulário web",
        "texto":    "O produto é ÓTIMO! Entrega rápida, embalagem perfeita & atendimento 5 estrelas. Recomendo 100%!!! :)"
    },
    {
        "id":       "DOC-005",
        "origem":   "Redes sociais",
        "texto":    "@empresa Vocês são um ABSURDO!! Cobrou R$299,90 indevido no cartão. Vou pro PROCON!!! #reclamação #vergonha"
    },
]

stop_words   = set(stopwords.words('portuguese'))
pontuacoes   = set(string.punctuation + '""''…–—«»°')

# ── Função de limpeza em etapas ──────────────────────────────────
def limpar_texto(texto):

    # ETAPA 1 — original
    original = texto

    # ETAPA 2 — minúsculas
    minusculo = texto.lower()

    # ETAPA 3 — remove menções, hashtags, URLs e números
    sem_ruido = re.sub(r'@\w+', '', minusculo)
    sem_ruido = re.sub(r'#\w+', '', sem_ruido)
    sem_ruido = re.sub(r'http\S+|www\.\S+', '', sem_ruido)
    sem_ruido = re.sub(r'\d+[\/\.\-]\d+[\/\.\-]?\d*', '', sem_ruido)  # datas
    sem_ruido = re.sub(r'r\$[\d\.,]+', '', sem_ruido)                  # valores
    sem_ruido = re.sub(r'\d+', '', sem_ruido)                          # outros números

    # ETAPA 4 — remove pontuação
    sem_pontuacao = re.sub(r'[^\w\s]', ' ', sem_ruido)
    sem_pontuacao = re.sub(r'\s+', ' ', sem_pontuacao).strip()

    # ETAPA 5 — tokenização
    tokens = word_tokenize(sem_pontuacao, language='portuguese')

    # ETAPA 6 — remove stopwords e tokens curtos
    tokens_limpos = [
        t for t in tokens
        if t.isalpha() and t not in stop_words and len(t) > 2
    ]

    # Itens removidos por etapa
    tokens_brutos   = word_tokenize(minusculo, language='portuguese')
    removidos_punct = [t for t in tokens_brutos if not t.isalpha()]
    removidos_stop  = [t for t in word_tokenize(sem_pontuacao, language='portuguese')
                       if t.isalpha() and (t in stop_words or len(t) <= 2)]

    return {
        "original":       original,
        "minusculo":      minusculo,
        "sem_pontuacao":  sem_pontuacao,
        "tokens_limpos":  tokens_limpos,
        "removidos_punct": removidos_punct,
        "removidos_stop":  removidos_stop,
        "total_original": len(tokens_brutos),
        "total_limpos":   len(tokens_limpos),
    }

# ── Processar todos os textos ────────────────────────────────────
resultados = [(doc, limpar_texto(doc["texto"])) for doc in textos]

# ── Totalizadores gerais ─────────────────────────────────────────
total_orig  = sum(r["total_original"] for _, r in resultados)
total_limp  = sum(r["total_limpos"]   for _, r in resultados)
reducao_geral = round(((total_orig - total_limp) / total_orig) * 100)

# ── Print ────────────────────────────────────────────────────────
print("=" * 66)
print("   🧹 LIMPEZA E NORMALIZAÇÃO DE TEXTOS — TIME DE ANÁLISES")
print("=" * 66)
print(f"\n  📄 Documentos processados  : {len(resultados)}")
print(f"  🔢 Total de tokens brutos  : {total_orig}")
print(f"  ✅ Total de tokens úteis   : {total_limp}")
print(f"  📉 Redução total           : {reducao_geral}% do volume removido")

for doc, r in resultados:
    reducao = round(((r["total_original"] - r["total_limpos"]) / r["total_original"]) * 100)

    print("\n" + "─" * 66)
    print(f"  📄 [{doc['id']}]  🗂  Origem: {doc['origem']}")
    print("─" * 66)

    print(f"\n  1️⃣  ORIGINAL")
    print(f"     {r['original']}")

    print(f"\n  2️⃣  MINÚSCULAS")
    print(f"     {r['minusculo']}")

    print(f"\n  3️⃣  SEM PONTUAÇÃO / RUÍDO")
    print(f"     {r['sem_pontuacao']}")

    print(f"\n  4️⃣  TOKENS LIMPOS (sem stopwords)")
    print(f"     {r['tokens_limpos']}")

    print(f"\n  📊 Estatísticas:")
    print(f"     Tokens originais  : {r['total_original']}")
    print(f"     Pontuação/ruído   : {len(r['removidos_punct'])} itens removidos → {r['removidos_punct'][:6]}")
    print(f"     Stopwords         : {len(r['removidos_stop'])} itens removidos  → {r['removidos_stop'][:6]}")
    print(f"     Tokens úteis      : {r['total_limpos']}  ({100 - reducao}% do original)")
    print(f"     📉 Redução total  : {reducao}%")

print("\n" + "─" * 66)
print("  📋 RESUMO COMPARATIVO — ANTES × DEPOIS")
print("─" * 66)
print(f"  {'ID':<10} {'ORIGEM':<22} {'ANTES':>6}  {'DEPOIS':>6}  {'REDUÇÃO':>8}")
print("─" * 66)
for doc, r in resultados:
    red = round(((r["total_original"] - r["total_limpos"]) / r["total_original"]) * 100)
    print(f"  {doc['id']:<10} {doc['origem']:<22} {r['total_original']:>6}  {r['total_limpos']:>6}  {red:>7}%")
print("─" * 66)
print(f"  {'TOTAL':<10} {'':<22} {total_orig:>6}  {total_limp:>6}  {reducao_geral:>7}%")

print("\n" + "─" * 66)
print("  🔎 ETAPAS DO PIPELINE DE LIMPEZA")
print("─" * 66)
etapas = [
    ("1️⃣ ", "Texto original",           "Entrada bruta com ruídos, caps, emojis e símbolos"),
    ("2️⃣ ", "Minúsculas",               "text.lower() — padroniza o caso de todas as letras"),
    ("3️⃣ ", "Remoção de ruído",         "Regex remove @menções, #hashtags, datas, valores R$"),
    ("4️⃣ ", "Remoção de pontuação",     "re.sub remove !?.,;:()[] e demais símbolos"),
    ("5️⃣ ", "Tokenização (NLTK)",       "word_tokenize() divide em tokens individuais"),
    ("6️⃣ ", "Remoção de stopwords",     "NLTK filtra 207 stopwords em português"),
    ("7️⃣ ", "Filtro de tamanho",        "Remove tokens com ≤ 2 caracteres (preposições, etc)"),
]
for num, etapa, descricao in etapas:
    print(f"  {num} {etapa:<26} → {descricao}")

print("\n" + "=" * 66)
print("  ✅ Pipeline concluído! Textos prontos para análise e modelagem.")
print("=" * 66)

#ATIVIDADE 10
#----------------------------------------------------------

import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ── Léxico de sentimentos ─────────────────────────────────────────
lexico = {
    "POSITIVO": {
        "excelente":    3, "incrível":     3, "perfeito":    3, "adorei":      3,
        "amei":         3, "espetacular":  3, "fantástico":  3, "maravilhoso": 3,
        "ótimo":        2, "ótima":        2, "recomendo":   2, "satisfeito":  2,
        "satisfeita":   2, "qualidade":    2, "eficiente":   2, "rápido":      2,
        "rápida":       2, "pontual":      2, "caprichado":  2, "cuidado":     2,
        "bom":          1, "boa":          1, "gostei":      1, "aprovado":    1,
        "funciona":     1, "chegou":       1, "atencioso":   1, "prestativo":  1,
    },
    "NEGATIVO": {
        "péssimo":      3, "péssima":      3, "horrível":    3, "terrível":    3,
        "lamentável":   3, "absurdo":      3, "vergonha":    3, "inaceitável": 3,
        "defeito":      2, "quebrado":     2, "danificado":  2, "arrependido": 2,
        "decepcionado": 2, "frustrado":    2, "insatisfeito":2, "demora":      2,
        "atraso":       2, "atrasado":     2, "cobrado":     2, "cobrança":    2,
        "ruim":         1, "problema":     1, "erro":        1, "falha":       1,
        "demorou":      1, "parou":        1, "travou":      1, "grosseiro":   1,
    },
    "INTENSIFICADOR": {
        "muito": 1.5, "demais": 1.5, "super": 1.4, "extremamente": 1.6,
        "bastante": 1.3, "totalmente": 1.4, "completamente": 1.4, "jamais": 1.5,
    },
    "NEGADOR": ["não", "nunca", "jamais", "nem", "nenhum", "nada", "sequer"],
}

stop_words = set(stopwords.words('portuguese'))

# ── Avaliações simuladas de produtos ─────────────────────────────
avaliacoes = [
    {"id": "AV-001", "produto": "Smartphone X Pro",   "nota": 5,
     "texto": "Produto incrível! Entrega rápida e embalagem perfeita. Recomendo muito para todos!"},
    {"id": "AV-002", "produto": "Fone Bluetooth Z",   "nota": 1,
     "texto": "Péssimo produto! Parou de funcionar em 2 dias. Defeito claro de fabricação. Terrível."},
    {"id": "AV-003", "produto": "Smartwatch Fit Pro", "nota": 4,
     "texto": "Ótimo custo-benefício. Chegou pontual e bem embalado. Só achei a bateria um pouco fraca."},
    {"id": "AV-004", "produto": "Caixa de Som Max",   "nota": 2,
     "texto": "Não recomendo. O produto chegou danificado e o atendimento foi horrível. Muito decepcionado."},
    {"id": "AV-005", "produto": "Tablet Ultra 10",    "nota": 5,
     "texto": "Simplesmente maravilhoso! Super rápido, tela fantástica e qualidade espetacular. Amei demais!"},
    {"id": "AV-006", "produto": "Carregador Turbo",   "nota": 3,
     "texto": "O produto é bom mas demorou bastante para chegar. Atendimento razoável, nada especial."},
    {"id": "AV-007", "produto": "Mouse Gamer Pro",    "nota": 1,
     "texto": "Absurdo! Cobrado duas vezes e o mouse travou no primeiro uso. Jamais compro novamente."},
    {"id": "AV-008", "produto": "Teclado Mecânico K", "nota": 5,
     "texto": "Qualidade excelente! Entrega rápida, produto caprichado e atendimento muito atencioso."},
    {"id": "AV-009", "produto": "Webcam HD 1080p",    "nota": 2,
     "texto": "Não funciona como prometido. Imagem ruim e o foco falha o tempo todo. Frustrante."},
    {"id": "AV-010", "produto": "Monitor UltraWide",  "nota": 4,
     "texto": "Chegou bem embalado e funciona perfeitamente. Gostei bastante, recomendo para home office."},
]

# ── Função de análise de sentimento ──────────────────────────────
def analisar_sentimento(av):
    texto  = av["texto"].lower()
    texto  = re.sub(r'[^\w\s]', ' ', texto)
    tokens = word_tokenize(texto, language='portuguese')

    score_pos  = 0.0
    score_neg  = 0.0
    hits_pos   = defaultdict(float)
    hits_neg   = defaultdict(float)
    negado     = False
    intensif   = 1.0

    for i, token in enumerate(tokens):
        # Verifica negador
        if token in lexico["NEGADOR"]:
            negado = True
            continue

        # Verifica intensificador
        if token in lexico["INTENSIFICADOR"]:
            intensif = lexico["INTENSIFICADOR"][token]
            continue

        peso_pos = lexico["POSITIVO"].get(token, 0)
        peso_neg = lexico["NEGATIVO"].get(token, 0)

        if peso_pos > 0:
            val = peso_pos * intensif
            if negado:
                score_neg += val
                hits_neg[token] = -val
            else:
                score_pos += val
                hits_pos[token] = val

        if peso_neg > 0:
            val = peso_neg * intensif
            if negado:
                score_pos += val
                hits_pos[token] = val
            else:
                score_neg += val
                hits_neg[token] = -val

        # Reset após processar palavra de sentimento
        if peso_pos > 0 or peso_neg > 0:
            negado   = False
            intensif = 1.0

    score_total = score_pos - score_neg
    score_norm  = round(score_total, 2)

    # ── Classificação condicional ─────────────────────────────────
    if score_total >= 6:
        sentimento = "MUITO POSITIVO"
        emoji      = "😍"
        label      = "🟢🟢"
        acao       = "Destaque como caso de sucesso e use como testemunho."
    elif score_total >= 2:
        sentimento = "POSITIVO"
        emoji      = "😊"
        label      = "🟢"
        acao       = "Manter padrão de qualidade. Monitorar continuidade."
    elif score_total > 0:
        sentimento = "LEVEMENTE POSITIVO"
        emoji      = "🙂"
        label      = "🟡"
        acao       = "Investigar pontos de melhoria mencionados."
    elif score_total == 0:
        sentimento = "NEUTRO"
        emoji      = "😐"
        label      = "⚪"
        acao       = "Analisar manualmente para contexto adicional."
    elif score_total >= -2:
        sentimento = "LEVEMENTE NEGATIVO"
        emoji      = "😕"
        label      = "🟠"
        acao       = "Acionar equipe de qualidade para revisão do produto."
    elif score_total >= -5:
        sentimento = "NEGATIVO"
        emoji      = "😠"
        label      = "🔴"
        acao       = "Contatar cliente e abrir chamado de qualidade urgente."
    else:
        sentimento = "MUITO NEGATIVO"
        emoji      = "🤬"
        label      = "🔴🔴"
        acao       = "ALERTA CRÍTICO — Acionar gerência e contatar cliente imediatamente."

    tokens_limpos = [t for t in tokens if t.isalpha() and t not in stop_words and len(t) > 2]

    return {
        "id":         av["id"],
        "produto":    av["produto"],
        "nota":       av["nota"],
        "texto":      av["texto"],
        "sentimento": sentimento,
        "emoji":      emoji,
        "label":      label,
        "score":      score_norm,
        "score_pos":  round(score_pos, 2),
        "score_neg":  round(score_neg, 2),
        "hits_pos":   dict(hits_pos),
        "hits_neg":   dict(hits_neg),
        "tokens":     tokens_limpos,
        "acao":       acao,
    }

# ── Processar todas as avaliações ────────────────────────────────
resultados = [analisar_sentimento(av) for av in avaliacoes]

# ── Totalizadores ────────────────────────────────────────────────
contagem = defaultdict(int)
for r in resultados:
    cat = "POSITIVO" if r["score"] > 0 else ("NEGATIVO" if r["score"] < 0 else "NEUTRO")
    contagem[cat] += 1

score_medio   = round(sum(r["score"] for r in resultados) / len(resultados), 2)
nota_media    = round(sum(r["nota"]  for r in resultados) / len(resultados), 1)
criticos      = [r for r in resultados if r["score"] <= -5]
destaques     = [r for r in resultados if r["score"] >= 6]

# ── Print ─────────────────────────────────────────────────────────
print("=" * 66)
print("   💡 ANÁLISE DE SENTIMENTO — AVALIAÇÕES DE PRODUTOS")
print("   🏭 SETOR DE QUALIDADE")
print("=" * 66)

print(f"\n  📦 Avaliações analisadas : {len(resultados)}")
print(f"  ⭐ Nota média            : {nota_media} / 5.0")
print(f"  📊 Score médio           : {score_medio:+.2f}")
print(f"  🟢 Positivas             : {contagem['POSITIVO']}")
print(f"  ⚪ Neutras               : {contagem['NEUTRO']}")
print(f"  🔴 Negativas             : {contagem['NEGATIVO']}")

if criticos:
    print(f"\n  🚨 ALERTAS CRÍTICOS      : {len(criticos)} avaliação(ões)!")
if destaques:
    print(f"  🏆 DESTAQUES POSITIVOS   : {len(destaques)} avaliação(ões)!")

print("\n" + "─" * 66)
print("  DETALHAMENTO POR AVALIAÇÃO")
print("─" * 66)

for r in resultados:
    print(f"\n  {r['label']} [{r['id']}]  {r['emoji']}  {r['sentimento']}")
    print(f"  📦 Produto : {r['produto']}  ({'⭐' * r['nota']} {r['nota']}/5)")
    print(f"  💬 Texto   : \"{r['texto']}\"")
    print(f"  📊 Score   : {r['score']:+.2f}  (pos: +{r['score_pos']}  neg: -{r['score_neg']})")

    if r["hits_pos"]:
        termos = ", ".join([f"{p}(+{v:.1f})" for p, v in r["hits_pos"].items()])
        print(f"  👍 Positivos detectados : {termos}")
    if r["hits_neg"]:
        termos = ", ".join([f"{p}({v:.1f})" for p, v in r["hits_neg"].items()])
        print(f"  👎 Negativos detectados : {termos}")

    print(f"  🎯 Tokens úteis : {r['tokens']}")
    print(f"  📌 Ação         : {r['acao']}")
    print("  " + "·" * 62)

# ── Ranking de satisfação ─────────────────────────────────────────
print("\n" + "─" * 66)
print("  🏆 RANKING DE SATISFAÇÃO — MELHORES AVALIAÇÕES")
print("─" * 66)
melhores = sorted(resultados, key=lambda x: x["score"], reverse=True)[:3]
for i, r in enumerate(melhores, 1):
    print(f"  {i}º  {r['emoji']} score {r['score']:+.2f}  [{r['id']}] {r['produto']}")

print("\n" + "─" * 66)
print("  🚨 FILA CRÍTICA — AVALIAÇÕES QUE EXIGEM AÇÃO IMEDIATA")
print("─" * 66)
critica = sorted([r for r in resultados if r["score"] < 0], key=lambda x: x["score"])
if critica:
    for r in critica:
        print(f"  {r['label']} score {r['score']:+.2f}  [{r['id']}] {r['produto']}")
        print(f"       → {r['acao']}")
else:
    print("  ✅ Nenhuma avaliação negativa identificada.")

print("\n" + "─" * 66)
print("  📈 TERMÔMETRO DE SATISFAÇÃO GERAL")
print("─" * 66)
satisfacao_pct = round((contagem["POSITIVO"] / len(resultados)) * 100)
barra_pos = "█" * (satisfacao_pct // 5)
barra_neg = "░" * (20 - (satisfacao_pct // 5))
print(f"\n  [{barra_pos}{barra_neg}] {satisfacao_pct}% de avaliações positivas\n")

if satisfacao_pct >= 80:
    print("  ✅ QUALIDADE APROVADA — Produto bem avaliado pelos clientes.")
elif satisfacao_pct >= 60:
    print("  ⚠️  ATENÇÃO — Há pontos de melhoria a investigar.")
else:
    print("  🚨 ALERTA CRÍTICO — Produto com alto índice de insatisfação!")

print("\n" + "=" * 66)
print("  ✅ Análise concluída! Relatório disponível para o Setor de Qualidade.")
print("=" * 66)
