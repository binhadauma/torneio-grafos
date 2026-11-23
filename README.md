# 🏆 Torneio e Grafos Dirigidos

Um joguinho para entender o "poder" dos jogadores de um torneio usando
**grafos dirigidos** (Álgebra Linear).

## A ideia

Num torneio com jogadores a₁, a₂, ..., aₙ:

- a₁ derrota a₂, a₂ derrota a₃, ..., e o último derrota o primeiro (o torneio "dá a volta").
- Desenhamos cada vitória como uma **seta**: quem vence → quem perde.
- O **poder** de um jogador é o número de vitórias dele:
  - **diretas** (ele venceu alguém), mais
  - **indiretas** (ele venceu alguém que venceu outra pessoa).

## Resultado

Cada jogador vence 1 pessoa diretamente e mais 1 pessoa de forma indireta.
Então **todos têm o mesmo poder: 1 + 1 = 2**.

Sem "dar a volta" (se o último não vence o primeiro), os dois últimos jogadores
ficam com menos poder. O jogo mostra essa diferença.

## Como jogar

1. Escolha quantos jogadores participam.
2. Faça o seu palpite: quem tem mais poder?
3. Clique em **Revelar** e veja o resultado.
4. Abra "Ver a matemática" para ver as matrizes usadas.

## Como acessar via web

1.Entre no site [Torneios e Grafos](https://torneio-grafos.streamlit.app/)

## Como abrir no seu computador

1. Instale o [Python](https://www.python.org/downloads/).
2. Abra o terminal na pasta do projeto e digite:

```
pip install -r requirements.txt
streamlit run app.py
```

O jogo abrirá no seu navegador.
