import sys  # Módulo usado para encerrar o programa com sys.exit()
import pygame  # Biblioteca de desenvolvimento de jogos 2D em Python

from settings import Settings  # Importa a classe com as configurações gerais do jogo
from ship import Ship  # Importa a classe responsável pela nave do jogador

class AlienInvasion:
    """Classe principal do jogo Invasão Alienígena.

    Responsável por:
    - Inicializar o Pygame
    - Criar a janela
    - Gerenciar os objetos principais do jogo (como a nave)
    - Executar o loop principal do jogo
    """

    def __init__(self):
        """Inicializa os atributos do jogo."""
        pygame.init()  # Inicializa todos os módulos do pygame (som, tela, fonte, etc.)

        # Cria uma instância das configurações do jogo (screen size, cor, etc.)
        self.settings = Settings()

        # Cria a tela do jogo com dimensões definidas nas configurações
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Define o título da janela
        pygame.display.set_caption("Invasão Alienígena")

        # Cria a nave do jogador, passando a instância do jogo como argumento
        self.ship = Ship(self)

        # Cria um objeto para controlar o FPS (frames por segundo)
        self.clock = pygame.time.Clock()

    def _check_events(self):
        """Verifica e responde a eventos de teclado e mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Fecha a janela quando o jogador clica no botão de fechar (X)
                sys.exit()

    def _update_screen(self):
        """Atualiza a tela a cada iteração do loop principal."""
        # Preenche o fundo da tela com a cor definida nas configurações
        self.screen.fill(self.settings.bg_color)

        # Desenha a nave na posição atual
        self.ship.blitme()

        # Torna a tela atual visível, atualizando tudo que foi desenhado
        pygame.display.flip()

    def run_game(self):
        """Executa o loop principal do jogo.

        Esse loop:
        - Verifica eventos (como pressionamento de teclas)
        - Atualiza os elementos da tela
        - Controla o tempo de execução (FPS)
        """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)  # Limita o jogo a 60 frames por segundo

# Este bloco garante que o jogo será executado apenas se o arquivo for rodado diretamente
if __name__ == '__main__':
    ai = AlienInvasion()  # Cria uma instância do jogo
    ai.run_game()         # Inicia o loop principal do jogo

