import pygame  # Importa o módulo pygame, usado para lidar com gráficos e interação

class Ship:
    """Classe que representa a espaçonave controlada pelo jogador."""

    def __init__(self, ai_game):
        """Inicializa a espaçonave e define sua posição inicial.

        Parâmetros:
        ai_game – instância da classe principal do jogo (AlienInvasion), 
                  usada para acessar atributos como screen e settings.
        """
        # Atribui a tela principal à nave
        self.screen = ai_game.screen
        # Acesso às configurações do jogo (por exemplo, velocidade da nave)
        self.settings = ai_game.settings

        # Obtém o retângulo da tela para controlar limites e posicionamento
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave a partir do diretório especificado
        self.image = pygame.image.load('images/spaceship/ship_1.png')

        # Redimensiona a imagem da nave para 60x60 pixels
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Rotaciona a imagem 90 graus no sentido horário
        self.image = pygame.transform.rotate(self.image, 90)

        # Obtém o "rect" da imagem para manipular posição na tela
        self.rect = self.image.get_rect()

        # Posiciona a nave inicialmente no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena a posição horizontal como número decimal (float),
        # permitindo movimentação mais suave do que apenas com inteiros
        self.x = float(self.rect.x)

        # Flags de controle de movimento: começam como False (nave parada)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da espaçonave com base nas flags de movimento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Desenha a nave na tela em sua posição atual."""
        self.screen.blit(self.image, self.rect)     
