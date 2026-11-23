import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

CORES = ["#E63946", "#F4A261", "#E9C46A", "#2A9D8F", "#457B9D", "#8E7DBE",
         "#F78FB3", "#6A994E", "#118AB2", "#EF476F", "#06D6A0", "#FFB703"]

st.set_page_config(page_title="Torneio e Grafos", page_icon="🏆")
st.title("🏆 Quem é o jogador mais poderoso?")
st.write("Num torneio, **a₁ derrota a₂, a₂ derrota a₃, ...** Cada vitória é uma "
         "seta no grafo. Será que alguém tem vantagem?")

# ---------- Escolhas da pessoa ----------
n = st.slider("Quantos jogadores?", 3, 12, 5)
ciclo = st.toggle("O último jogador também derrota o primeiro (torneio em ciclo)",
                  value=True)

# ---------- Matemática ----------
# A[i][j] = 1 quando o jogador i derrota o jogador j
A = np.zeros((n, n), dtype=int)
for i in range(n - 1):
    A[i, i + 1] = 1
if ciclo:
    A[n - 1, 0] = 1

# Poder = vitórias diretas (A) + vitórias em 2 passos (A²)
poder = (A + A @ A).sum(axis=1)

# ---------- Desenho do grafo ----------
ang = np.linspace(0, 2 * np.pi, n, endpoint=False) + np.pi / 2
pos = np.c_[np.cos(ang), np.sin(ang)]

fig, ax = plt.subplots(figsize=(5, 5))
for i, j in zip(*np.nonzero(A)):
    ax.annotate("", xy=pos[j], xytext=pos[i],
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=2,
                                shrinkA=18, shrinkB=18))
ax.scatter(*pos.T, s=900, c=CORES[:n], zorder=3)
for k, (x, y) in enumerate(pos):
    ax.text(x, y, f"a{k + 1}", ha="center", va="center", color="white",
            fontsize=13, fontweight="bold", zorder=4)
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.axis("off")
st.pyplot(fig)
st.caption("Cada seta aponta de quem vence para quem perde.")

# ---------- O jogo ----------
st.subheader("🎯 Faça o seu palpite")
palpite = st.radio("Quem você acha que tem MAIS poder?",
                   [f"a{k + 1}" for k in range(n)], horizontal=True)

if st.button("Revelar o poder de cada um", type="primary"):
    fig2, ax2 = plt.subplots(figsize=(6, 3))
    ax2.bar([f"a{k + 1}" for k in range(n)], poder, color=CORES[:n])
    ax2.set_ylabel("Poder")
    ax2.set_ylim(0, max(poder.max(), 1) + 1)
    for k, p in enumerate(poder):
        ax2.text(k, p + 0.05, str(p), ha="center", fontweight="bold")
    st.pyplot(fig2)

    if len(set(poder)) == 1:
        st.success(f"Todos têm o mesmo poder: **{poder[0]}**. "
                   f"Seu palpite ({palpite}) estava certo, e todos os outros também!")
        st.info("Por quê? Em um ciclo, cada jogador vence exatamente **1** pessoa "
                "diretamente e, por meio dela, mais **1** pessoa em dois passos. "
                "Logo: 1 + 1 = 2 para todos.")
    else:
        melhor = [f"a{k + 1}" for k in np.nonzero(poder == poder.max())[0]]
        st.warning(f"Sem o ciclo, os poderes são diferentes. "
                   f"Mais poderosos: {', '.join(melhor)}. "
                   "Ative a chave acima para fechar o ciclo!")

# ---------- Para quem quer ver as contas ----------
with st.expander("📐 Ver a matemática"):
    st.write("**Matriz A** (linha vence coluna):")
    st.dataframe(A)
    st.write("**Matriz A²** (vitórias em dois passos):")
    st.dataframe(A @ A)
    st.write("**Poder = soma de cada linha de A + A²:**", poder.tolist())
