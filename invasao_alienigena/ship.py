import pygame  # Importa o módulo pygame.

class Ship:
    """Classe que representa a espaçonave controlada pelo jogador."""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial.

        Parâmetros:
        ai_game – instância da classe principal do jogo (AlienInvasion), 
                  usada para acessar atributos como screen e settings.
        """
        # Atribui a tela do jogo à nave
        self.screen = ai_game.screen
        # Acessa o retângulo da tela, usado para posicionar a nave
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/spaceship/ship_1.png')
        # Redimensiona para 40 x 40
        self.image = pygame.transform.scale(self.image, (60,60))
        # Rotaciona para cima
        self.image = pygame.transform.rotate(self.image, 90)
        # Obtém o rect (retângulo) da imagem, que será usado para posicionamento
        self.rect = self.image.get_rect()

        # Define a posição inicial da nave: centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a nave na tela, em sua posição atual."""
        self.screen.blit(self.image, self.rect)
