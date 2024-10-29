import pygame

class Jogador:  # cria uma classe jogador
    def __init__(self, tela, x, y):  # inicializa a classe
        self.posicao = [x, y]  # posição do jogador (x e y)
        self.tamanho = (32, 32)  # tamanho do jogador
        self.rect = pygame.Rect(self.posicao, self.tamanho)  # rect para detectar colisão
        
        self.contador = 0  # contador para animação
        self.imagemAtual = 0  # índice da imagem atual
        self.tela = tela  # define a tela do jogador
        self.listaImagens = []  # lista que receberá as imagens do jogador

        for i in range(3):  # laço para carregar as 3 imagens
            imagem = pygame.image.load(f'assets/passaro-{i}.png')
            imagem = pygame.transform.scale(imagem, self.tamanho)
            self.listaImagens.append(imagem)

        # Variáveis para gerenciar a velocidade e a gravidade
        self.velocidadeAtual = 0
        self.gravidade = 1 / 60 * 10
        self.velocidadeMaxima = 1 / 60 * 100

    def desenhar(self):  # desenha o jogador na tela
        self.contador += 1  # incrementa o contador
        if self.contador > 5:  # altera a imagem a cada 5 frames
            self.contador = 0
            self.imagemAtual = (self.imagemAtual + 1) % 3
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)

    def atualizar(self):  # atualiza a posição e velocidade
        self.velocidadeAtual = min(self.velocidadeAtual + self.gravidade, self.velocidadeMaxima)
        self.posicao = [self.posicao[0], self.posicao[1] + self.velocidadeAtual]
        self.rect = pygame.Rect(self.posicao, self.tamanho)

        self.teclas = pygame.key.get_pressed()  # verifica as teclas pressionadas
        if self.teclas[pygame.K_SPACE]:  # se espaço for pressionado
            self.velocidadeAtual = -self.velocidadeMaxima*2  # faz o jogador "subir"

    def getRect(self):  # retorna o rect do jogador
        return pygame.Rect(self.posicao, self.tamanho)
