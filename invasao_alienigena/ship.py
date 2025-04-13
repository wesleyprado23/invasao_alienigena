import pygame  # Importa o módulo pygame, usado para lidar com gráficos e interação

class Ship:
    """Classe que representa a espaçonave controlada pelo jogador.

    Responsável por:
    - Carregar a imagem da nave
    - Definir sua posição e limites de movimento
    - Atualizar a posição com base nas entradas do jogador
    - Desenhar a nave na tela
    """

    def __init__(self, ai_game):
        """Inicializa a nave e define sua posição inicial.

        Parâmetros:
        ai_game — instância da classe principal do jogo (AlienInvasion),
                  usada para acessar a tela (screen), configurações (settings),
                  e retângulo da janela.
        """
        # Referência à superfície da tela onde a nave será desenhada
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Retângulo da tela (usado para evitar sair dos limites)
        self.screen_rect = self.screen.get_rect()

        # Carrega a imagem da nave
        self.image = pygame.image.load('images/spaceship/ship_1.png')

        # Redimensiona a imagem para 60x60 pixels
        self.image = pygame.transform.scale(self.image, (60, 60))

        # Rotaciona a imagem 90 graus (para apontar para cima)
        self.image = pygame.transform.rotate(self.image, 90)

        # Obtém o retângulo da imagem da nave para posicionamento
        self.rect = self.image.get_rect()

        # Posiciona a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena a posição horizontal como float para movimentos suaves
        self.x = float(self.rect.x)

        # Flags de movimento — controlam se a nave está se movendo
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Atualiza a posição da nave com base nas flags de movimento.

        Evita que a nave ultrapasse os limites da tela.
        """

        # Movimento para a direita (sem ultrapassar a borda direita)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Movimento para a esquerda (sem ultrapassar a borda esquerda)
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Movimento para cima
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed

        # Movimento para baixo
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed

        # Atualiza o valor inteiro de x no rect (posição real da imagem)
        self.rect.x = self.x

    def blitme(self):
        """Desenha a imagem da nave na tela, na posição atual."""
        self.screen.blit(self.image, self.rect)
