import sys  # Módulo usado para encerrar o programa com sys.exit()
import pygame  # Biblioteca de desenvolvimento de jogos 2D em Python

from settings import Settings  # Importa a classe com as configurações do jogo
from ship import Ship  # Importa a classe da nave do jogador

class AlienInvasion:
    """Classe principal do jogo Invasão Alienígena.

    Responsável por:
    - Inicializar o Pygame
    - Criar e configurar a janela
    - Gerenciar os objetos principais do jogo (como a nave)
    - Executar o loop principal do jogo
    """

    def __init__(self):
        """Inicializa o jogo e define os recursos iniciais."""
        pygame.init()  # Inicializa os módulos principais do pygame

        # Instancia as configurações do jogo
        self.settings = Settings()

        # Cria a tela com largura e altura definidos nas configurações
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Define o título da janela
        pygame.display.set_caption("Invasão Alienígena")

        # Carrega e redimensiona a imagem de fundo para caber na tela
        self.bg_image = pygame.image.load('images/backgrounds/space_bg.png')
        self.bg_image = pygame.transform.scale(self.bg_image, 
                                               (self.settings.screen_width, 
                                                self.settings.screen_height))

        # Cria a nave do jogador (objeto Ship)
        self.ship = Ship(self)

        # Objeto para controlar o FPS (frames por segundo)
        self.clock = pygame.time.Clock()

    def _check_events(self):
        """Verifica e responde a eventos de teclado e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Fecha o programa ao clicar no botão X
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                # Pressionou tecla
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_s:
                    self.ship.movinf_down = True

            elif event.type == pygame.KEYUP:
                # Soltou tecla
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
                elif event.key == pygame.K_w:
                    self.ship.moving_up = False
                elif event.key == pygame.K_s:
                    self.ship.movinf_down = False

    def _update_screen(self):
        """Atualiza a imagem da tela com cada passagem do loop."""
        # Preenche o fundo da tela
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_image, (0, 0))  # Desenha o fundo na posição (0, 0)

        # Desenha a nave na posição atual
        self.ship.blitme()

        # Atualiza a tela exibindo tudo que foi desenhado
        pygame.display.flip()

    def run_game(self):
        """Executa o loop principal do jogo.

        O loop:
        - Verifica entradas do jogador
        - Atualiza a nave
        - Atualiza a tela
        - Controla a taxa de quadros (FPS)
        """
        while True:
            self._check_events()
            self.ship.update()  # Atualiza a posição da nave, se necessário
            self._update_screen()
            self.clock.tick(60)  # Limita o jogo a 60 quadros por segundo

# Executa o jogo somente se este script for executado diretamente
if __name__ == '__main__':
    ai = AlienInvasion()  # Cria a instância principal do jogo
    ai.run_game()         # Inicia o loop do jogo
