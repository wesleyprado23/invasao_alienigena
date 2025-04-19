import pygame  # Biblioteca Pygame para gráficos, eventos e sprites
from pygame.sprite import Sprite

class Ship(Sprite):
    """Classe que representa a espaçonave controlada pelo jogador.

    Responsável por:
    - Carregar e renderizar a imagem da nave
    - Gerenciar movimento com base nas teclas pressionadas
    - Impedir que a nave ultrapasse os limites da tela
    - Ser usada como sprite (para grupos e colisões)
    """

    def __init__(self, ai_game):
        """Inicializa a nave e define sua posição inicial.

        Parâmetros:
        ai_game — instância de AlienInvasion (classe principal do jogo),
                  usada para acessar configurações, tela e limites da janela.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/spaceship/ship_9.png')

        # Redimensiona e rotaciona (opcional) para apontar para cima
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image = pygame.transform.rotate(self.image, 90)

        # Obtém o retângulo da imagem e posiciona no centro inferior
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena a posição horizontal como float para movimento suave
        self.x = float(self.rect.x)

        # Flags de movimento — controladas pelas teclas pressionadas
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da nave com base nas flags de movimento.

        Garante que a nave permaneça dentro dos limites da tela.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        # Atualiza a posição horizontal do rect
        self.rect.x = self.x

    def blitme(self):
        """Desenha a imagem da nave na tela, na posição atual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Reposiciona a nave no centro inferior da tela (usado após colisão)."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
