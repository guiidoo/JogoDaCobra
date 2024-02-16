import pygame
import random

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura, altura = 400, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Defina as cores
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Defina o tamanho da grade e da célula
tamanho_celula = 20
grade_largura = largura // tamanho_celula
grade_altura = altura // tamanho_celula

# Defina a velocidade inicial da cobra
velocidade = 5

# Inicialize a cobra
cobra = [(grade_largura // 2, grade_altura // 2)]
direcao = (1, 0)

# Inicialize a comida
comida = (random.randint(0, grade_largura - 1), random.randint(0, grade_altura - 1))

# Inicialize a variável de reinicialização
reiniciar = False

# Função para desenhar a cobra
def desenhar_cobra():
    for segmento in cobra:
        pygame.draw.rect(janela, verde, (segmento[0] * tamanho_celula, segmento[1] * tamanho_celula, tamanho_celula, tamanho_celula))

# Função para desenhar a comida
def desenhar_comida():
    pygame.draw.rect(janela, vermelho, (comida[0] * tamanho_celula, comida[1] * tamanho_celula, tamanho_celula, tamanho_celula))

# Função para desenhar o botão de reset
def desenhar_botao_reset():
    pygame.draw.rect(janela, vermelho, (10, 10, 80, 30))
    fonte = pygame.font.Font(None, 36)
    texto_reset = fonte.render("Reset", True, branco)
    janela.blit(texto_reset, (20, 15))

# Função para verificar se o mouse está sobre o botão de reset
def mouse_sobre_botao_reset(posicao_mouse):
    return 10 <= posicao_mouse[0] <= 90 and 10 <= posicao_mouse[1] <= 40

# Loop principal do jogo
jogo_rodando = True
while jogo_rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direcao != (0, 1):
                direcao = (0, -1)
            elif evento.key == pygame.K_DOWN and direcao != (0, -1):
                direcao = (0, 1)
            elif evento.key == pygame.K_LEFT and direcao != (1, 0):
                direcao = (-1, 0)
            elif evento.key == pygame.K_RIGHT and direcao != (-1, 0):
                direcao = (1, 0)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if mouse_sobre_botao_reset(evento.pos):
                # Reinicie o jogo
                cobra = [(grade_largura // 2, grade_altura // 2)]
                direcao = (1, 0)
                comida = (random.randint(0, grade_largura - 1), random.randint(0, grade_altura - 1))
                reiniciar = False

    # Atualize a posição da cobra
    if not reiniciar:
        cabeca_x, cabeca_y = cobra[0]
        nova_cabeca = (cabeca_x + direcao[0], cabeca_y + direcao[1])

        # Verifique se a cobra colidiu com a parede
        if nova_cabeca[0] < 0 or nova_cabeca[0] >= grade_largura or nova_cabeca[1] < 0 or nova_cabeca[1] >= grade_altura:
            reiniciar = True

        # Verifique se a cobra comeu a comida
        if nova_cabeca == comida:
            comida = (random.randint(0, grade_largura - 1), random.randint(0, grade_altura - 1))
        else:
            cobra.pop()

        cobra.insert(0, nova_cabeca)

        # Verifique se a cobra colidiu consigo mesma
        if nova_cabeca in cobra[1:]:
            reiniciar = True

    # Limpe a tela
    janela.fill(branco)

    # Desenhe a cobra e a comida
    desenhar_cobra()
    desenhar_comida()

    # Desenhe o botão de reset
    desenhar_botao_reset()

    # Atualize a tela
    pygame.display.update()

    # Controle de velocidade
    pygame.time.Clock().tick(velocidade)

# Encerre o Pygame
pygame.quit()