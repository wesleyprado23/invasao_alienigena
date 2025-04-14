import pygame  # Importa a biblioteca Pygame para gráficos e interação

class Ship:
    """Classe que representa a espaçonave controlada pelo jogador.

    Responsável por:
    - Carregar e posicionar a imagem da nave
    - Responder ao movimento do jogador
    - Atualizar a posição da nave na tela
    - Evitar que a nave ultrapasse os limites da janela
    - Renderizar a nave na tela
    """

    def __init__(self, ai_game):
        """Inicializa a nave e define sua posição inicial.

        Parâmetros:
        ai_game — instância da classe principal do jogo (AlienInvasion),
                  usada para acessar a tela, configurações e limites de tela.
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()  # Área da tela

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/spaceship/ship_9.png')

        # Ajusta o tamanho da nave para 60x60 pixels
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Rotaciona a imagem 90 graus para apontar para cima
        self.image = pygame.transform.rotate(self.image, 90)

        # Obtém o retângulo da imagem para controlar posição e colisão
        self.rect = self.image.get_rect()

        # Posiciona a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena a coordenada X como float para movimento suave
        self.x = float(self.rect.x)

        # Flags de controle de movimento (ativadas/desativadas com eventos de tecla)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da nave com base nas flags de movimento.

        Garante que a nave fique dentro dos limites da tela.
        """

        # Move para a direita, se não ultrapassar o limite da tela
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Move para a esquerda
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Move para cima
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

        # Move para baixo
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        # Atualiza a posição horizontal do rect com base no valor decimal
        self.rect.x = self.x

    def blitme(self):
        """Desenha a imagem da nave na tela, na posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaçonave na tela"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
