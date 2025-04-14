import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que representa os projéteis disparados pela espaçonave.

    Herda de pygame.sprite.Sprite para permitir o uso eficiente com grupos de sprites,
    facilitando atualização, colisões e remoção de vários projéteis de uma só vez.
    """

    def __init__(self, ai_game):
        """Cria um projétil na posição atual da nave do jogador.

        Parâmetros:
        ai_game – instância de AlienInvasion que fornece acesso à tela,
                  configurações do jogo e à própria nave.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um retângulo do projétil com largura e altura definidos nas configurações
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)

        # Posiciona o projétil no topo central da nave
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição vertical como float para permitir movimento suave
        self.y = float(self.rect.y)

    def update(self):
        """Move o projétil para cima na tela (em direção ao topo)."""
        # Em Pygame, a coordenada Y diminui conforme sobe na tela
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do retângulo com base no novo valor de y
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil como um retângulo na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
