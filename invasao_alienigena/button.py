import pygame.font  # Módulo para lidar com fontes e renderização de texto

class Button:
    """Classe responsável por criar e gerenciar botões no jogo.

    Usado principalmente para iniciar o jogo com o botão "Play",
    mas pode ser reutilizado para outros botões como "Reiniciar", "Sair", etc.
    """

    def __init__(self, ai_game, msg):
        """Inicializa os atributos do botão e prepara a mensagem.

        Parâmetros:
        ai_game — instância de AlienInvasion (para acessar a tela)
        msg — texto exibido dentro do botão
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # ===============================
        # Propriedades visuais do botão
        # ===============================
        self.width, self.height = 200, 50                # Dimensões do botão
        self.button_color = (0, 132, 0)                  # Cor do botão (verde escuro)
        self.text_color = (255, 255, 255)                # Cor do texto (branco)
        self.font = pygame.font.SysFont(None, 48)        # Fonte padrão (tamanho 48)

        # Cria o rect do botão e centraliza na tela
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepara a mensagem como imagem para renderização
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Transforma o texto em uma imagem renderizada e centraliza no botão."""
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color
        )

        # Centraliza a imagem de texto dentro do botão
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Desenha o botão na tela com a mensagem centralizada."""
        # Desenha o retângulo do botão
        self.screen.fill(self.button_color, self.rect)

        # Desenha o texto sobre o botão
        self.screen.blit(self.msg_image, self.msg_image_rect)
