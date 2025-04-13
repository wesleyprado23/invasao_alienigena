import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que gerencia os projéteis disparados pela espaçonave.

    Cada projétil é uma instância de Sprite, permitindo o uso de grupos
    e atualizações automáticas com o método .update().
    """

    def __init__(self, ai_game):
        """Cria um novo projétil na posição atual da espaçonave.

        Parâmetros:
        ai_game – instância de AlienInvasion, usada para acessar tela, configurações e a nave.
        """
        super().__init__()  # Inicializa como um Sprite

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria o retângulo que representa o projétil
        # Começa em (0, 0), e depois é posicionado corretamente
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
                                self.settings.bullet_height)

        # Define o topo central do projétil para coincidir com o topo da nave
        self.rect.midtop = ai_game.ship.rect.midtop

        # Armazena a posição Y como float para permitir movimentação suave
        self.y = float(self.rect.y)

    def update(self):
        """Atualiza a posição do projétil, movendo-o para cima na tela."""
        # Reduz o valor de y para subir (em Pygame, o eixo Y cresce para baixo)
        self.y -= self.settings.bullet_speed

        # Atualiza a posição do retângulo com o novo valor
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
