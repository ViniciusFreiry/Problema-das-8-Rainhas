# Problema das 8 Rainhas com Random Restart e Hill Climbing

Este projeto implementa duas abordagens para resolver o **Problema das 8 Rainhas**:  
- **Random Restart**
- **Hill Climbing**

Ambos os algoritmos são apresentados com visualização gráfica utilizando a biblioteca **Pygame**.

O objetivo é posicionar 8 rainhas em um tabuleiro 8x8 de modo que **nenhuma ataque a outra** (sem conflitos em linhas, colunas ou diagonais). Além disso, o código realiza medições de **tempo de execução**, **memória usada**, **tentativas ou passos computacionais**, e, no caso do Random Restart, calcula também o tempo necessário para encontrar as **92 soluções válidas** possíveis.

---

## 🔧 Como Funciona

Cada versão do algoritmo (Random Restart e Hill Climbing) possui sua própria janela e botão para gerar soluções:

### Hill Climbing
- Executa o algoritmo com melhoria local.
- Mede o número de **passos computacionais** até alcançar uma solução ou um ótimo local.
- Mede **uso de memória** e **tempo de execução** para encontrar **uma** solução.

### Random Restart
- Gera permutações aleatórias até encontrar uma solução válida.
- Mede o número de **tentativas** (restarts) necessárias até encontrar uma solução válida.
- Possui botão adicional para calcular o **tempo necessário para encontrar todas as 92 soluções válidas**.
- Mede **uso de memória** e **tempo de execução** para uma ou todas as soluções.

---

## 📦 Funcionalidades
- Interface gráfica interativa com **Pygame**.
- Tabuleiro 8x8 com posicionamento visual das rainhas.
- Botões:
  - **"Nova Solução"**: gera uma nova configuração com base no algoritmo.
  - **"Tempo das 92 Soluções"** (somente no Random Restart): mede o tempo para calcular todas as soluções válidas.

---

## ▶️ Como Executar

1. Instale o Python (versão 3.7 ou superior).
2. Instale o **Pygame**:

```bash
pip install pygame
```

3. Execute os arquivos:
- Para Hill Climbing: `8_queens_with_hill_climbing.py`
- Para Random Restart: `8_queens_with_random_restart.py`

---

## 📊 Métricas Apresentadas

- ✅ Tempo de execução (ms)
- ✅ Memória usada (KB)
- ✅ Passos computacionais ou número de tentativas
- ✅ Tempo para encontrar todas as 92 soluções válidas (Random Restart)

---

## 👨‍💻 Autores

Feito por Vinícius Freiry e Henrique Duarte