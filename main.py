import pygame  # indica que utilizaremos pygame
#from scripts.jogador import Jogador
#from scripts.cano import Cano
from scripts.cenas import Partida
from scripts.cenas import Menu
pygame.init()  # inicia o pygame

tamanhoTela = [600, 400]  # define o tamanho da janela do jogo
tela = pygame.display.set_mode(tamanhoTela)  # cria a janela que utilizaremos
pygame.display.set_caption("FlappyBird Clone")  # define o título da janela
relogio = pygame.time.Clock()  # cria um relógio para controlar a velocidade do jogo
corFundo = (86, 148, 214)  # cria uma cor de fundo em formato RGB

# Criação do objeto jogador antes do loop
#jog = Jogador(tela, 100, 100)
#cano = Cano(tela)
# Loop principal do jogo
listaCenas ={
    'partida': Partida(tela),
    'menu': Menu(tela)
}

cenaAtual = 'menu'
while True:  # cria um laço infinito para manter o jogo aberto
    for e in pygame.event.get():  # laço que passa em cada evento do pygame
        if e.type == pygame.QUIT:  # verifica se é do tipo sair; que ocorre quando fecha a tela
            pygame.quit()  # finaliza o pygame

    tela.fill(corFundo)  # pinta a tela de fundo

    # Atualiza e desenha o jogador
   # jog.atualizar()
   # jog.desenhar()
   # cano.atualizar()
   # cano.desenhar()
    cenaAtual =listaCenas[cenaAtual].atualizar()
    relogio.tick(60)  # controla a tela para atualizar 60 vezes por segundo
    pygame.display.flip()  # atualiza a tela, mostrando as alterações feitas
