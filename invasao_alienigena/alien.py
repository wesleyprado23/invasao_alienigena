import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa um único alienígena da frota inimiga.

    Herda de `pygame.sprite.Sprite` para que possa ser usado com grupos de sprites,
    permitindo manipulação em lote (como atualização, colisões e renderização).
    """

    def __init__(self, ai_game):
        """Inicializa o alienígena e define sua posição inicial.

        Parâmetros:
        ai_game — instância da classe principal do jogo (AlienInvasion),
                  usada para acessar a tela, configurações e contexto geral.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alien
        self.image = pygame.image.load('images/alien/alien_spaceship1.png')

        # Redimensiona a imagem para 60x60 pixels (padrão da frota)
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Rotaciona a imagem 180° para apontar para baixo (opcional)
        self.image = pygame.transform.rotate(self.image, 180)

        # Obtém o retângulo da imagem (usado para posicionamento e colisão)
        self.rect = self.image.get_rect()

        # Define a posição inicial perto do canto superior esquerdo
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal exata como float (para movimento suave)
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True se o alienígena atingiu a borda da tela.

        Utilizado para inverter a direção da frota e fazê-la descer.
        """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Atualiza a posição do alienígena na tela.

        O deslocamento horizontal é determinado por:
        - `alien_speed`: velocidade definida nas configurações
        - `fleet_direction`: 1 (direita) ou -1 (esquerda)
        """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
