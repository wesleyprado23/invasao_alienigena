import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Classe que representa um único alienígena da frota inimiga.

    Herda de pygame.sprite.Sprite para facilitar o uso com grupos de sprites,
    como desenhar múltiplos aliens de uma vez, detectar colisões em grupo, etc.
    """

    def __init__(self, ai_game):
        """Inicializa o alienígena e define sua posição inicial.

        Parâmetros:
        ai_game — instância da classe principal do jogo (AlienInvasion),
                  usada para acessar a tela, configurações e contexto do jogo.
        """
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carrega a imagem do alienígena
        self.image = pygame.image.load('images/alien/alien_spaceship1.png')

        # Redimensiona a imagem para padronizar o tamanho na frota
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Rotaciona a imagem para que fique voltada para baixo (caso necessário)
        self.image = pygame.transform.rotate(self.image, 180)

        # Obtém o retângulo (área) da imagem para posicionamento
        self.rect = self.image.get_rect()

        # Define a posição inicial perto do canto superior esquerdo da tela
        self.rect.x = self.rect.width     # margem esquerda = largura do alien
        self.rect.y = self.rect.height    # margem superior = altura do alien

        # Armazena a posição real como float para permitir movimento suave
        self.x = float(self.rect.x)

    def check_edges(self):
        """Retorna True se o alienígena estiver tocando a borda da tela.

        Isso é usado para mudar a direção da frota quando um dos aliens atinge a borda.
        """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Atualiza a posição horizontal do alienígena.

        O movimento é controlado por:
        - `alien_speed`: a velocidade definida nas configurações
        - `fleet_direction`: 1 (direita) ou -1 (esquerda)
        """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
