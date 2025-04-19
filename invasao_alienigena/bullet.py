import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que representa os projéteis disparados pela espaçonave.

    Herda de pygame.sprite.Sprite para que possa ser adicionado a grupos,
    facilitando atualização em lote, verificação de colisões e renderização.
    """

    def __init__(self, ai_game):
        """Cria um projétil na posição atual da nave do jogador.

        Parâmetros:
        ai_game – instância da classe principal AlienInvasion.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria o retângulo que representa o projétil
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # Posiciona o projétil no topo central da nave
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a coordenada y como float para movimento mais preciso
        self.y = float(self.rect.y)

    def update(self):
        """Atualiza a posição do projétil na tela (movimento vertical)."""
        # Em Pygame, o topo da tela é y = 0, então subir = diminuir y
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do rect com a nova coordenada y
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
