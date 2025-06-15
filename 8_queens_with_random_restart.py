import pygame
import sys
import random
import tracemalloc
import time
from itertools import permutations

# Configurações
TAM_CELULA = 60  # Tamanho de cada célula do tabuleiro
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS + 100 # Espaço extra para os dos botões
LARGURA_BOTAO = 60 * 8
ALTURA_BOTAO = 45

# Função para verificar se uma solução é válida
def eh_valida(solucao):
    for i in range(NUM_RAINHAS):
        for j in range(i + 1, NUM_RAINHAS):
            if solucao[i] == solucao[j] or abs(solucao[i] - solucao[j]) == abs(i - j):
                return False
    return True

# Função para gerar uma solução aleatória
def gerar_solucao_aleatoria():
    solucao = list(range(NUM_RAINHAS))  # Cria uma lista [0, 1, 2, ..., 7]
    random.shuffle(solucao)  # Embaralha a lista para criar uma solução aleatória
    return solucao

# Função para tentar encontrar uma solução válida com Random Restart
def random_restart():
    tentativas = 0
    while True:
        tentativas += 1
        solucao = gerar_solucao_aleatoria()
        if eh_valida(solucao):
            print(f"Número de tentativas até solução válida: {tentativas}")
            return solucao

# Inicia o Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("8 Rainhas - Random Restart")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            if (linha + coluna) % 2 == 0:
                cor = BRANCO
            else:
                cor = PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

# Função para desenhar as rainhas
def desenhar_rainhas(solucao):
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y = linha * TAM_CELULA + TAM_CELULA // 2
        radius = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)

# Função para desenhar os botões
def desenhar_botao():
    font = pygame.font.Font(None, 36)

    # Botão de uma Solução
    botao_rect = pygame.Rect(LARGURA // 2 - LARGURA_BOTAO // 2, ALTURA - (ALTURA_BOTAO * 2 + 10), LARGURA_BOTAO, ALTURA_BOTAO)
    pygame.draw.rect(screen, AZUL, botao_rect)
    texto = font.render("Nova Solução", True, BRANCO)
    screen.blit(texto, (botao_rect.x + (botao_rect.width - texto.get_width()) // 2, 
                        botao_rect.y + (botao_rect.height - texto.get_height()) // 2))

    # Botão para calculo de tempo das 92 soluções
    botao_rect = pygame.Rect(LARGURA // 2 - LARGURA_BOTAO // 2, ALTURA - ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
    pygame.draw.rect(screen, AZUL, botao_rect)
    texto = font.render("Tempo das 92 Soluções", True, BRANCO)
    screen.blit(texto, (botao_rect.x + (botao_rect.width - texto.get_width()) // 2, 
                        botao_rect.y + (botao_rect.height - texto.get_height()) // 2))

# Função principal para rodar o Pygame
def main():
    tracemalloc.start()

    # Tempo de Execução (1 solução)
    tempo_inicio = time.time()
    solucao = random_restart()
    tempo_fim = time.time()
    print(f"Tempo para solução: {(tempo_fim - tempo_inicio) * 1000:.4f} milisegundos")

    clock = pygame.time.Clock()
    memoria_usada = tracemalloc.get_traced_memory()[1] / 1024  # em KB
    print(f"Memória usada: {memoria_usada:.2f} KB")
    tracemalloc.stop()
    
    while True:
        tracemalloc.start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Detectando clique no botão
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                botao_rect = pygame.Rect(LARGURA // 2 - LARGURA_BOTAO // 2, ALTURA - (ALTURA_BOTAO * 2 + 10), LARGURA_BOTAO, ALTURA_BOTAO)
                if botao_rect.collidepoint(mouse_x, mouse_y):
                    # Tempo de Execução (1 solução)
                    tempo_inicio = time.time()
                    solucao = random_restart()
                    tempo_fim = time.time()
                    print(f"Tempo para solução: {(tempo_fim - tempo_inicio) * 1000:.4f} milisegundos")

                    memoria_usada = tracemalloc.get_traced_memory()[1] / 1024  # em KB
                    print(f"Memória usada: {memoria_usada:.2f} KB")
                
                botao_rect = pygame.Rect(LARGURA // 2 - LARGURA_BOTAO // 2, ALTURA - ALTURA_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
                if botao_rect.collidepoint(mouse_x, mouse_y):
                    # Tempo de Execução (92 soluções)
                    tempo_inicio = time.time()
                    todas = list(permutations(range(8)))
                    validas = [s for s in todas if eh_valida(s)]
                    tempo_fim = time.time()

                    print(f"Número de soluções válidas: {len(validas)}")  # Deve imprimir 92
                    print(f"Tempo para achar as {len(validas)} soluções: {(tempo_fim - tempo_inicio) * 1000:.4f} milisegundos")

        tracemalloc.stop()

        # Desenhar tabuleiro e rainhas
        desenhar_tabuleiro()
        desenhar_rainhas(solucao)
        desenhar_botao()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
