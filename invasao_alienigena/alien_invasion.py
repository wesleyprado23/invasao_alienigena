import sys  # Importa o módulo sys
            # usado para encerrar o programa de forma segura
import pygame  # Importa a biblioteca pygame, que permite criar jogos em Python

from settings import Settings # Importa a classe de configurações do jogo
                              # definida em um arquivo separado

class AlienInvasion:
    """Classe principal do jogo Invasão Alienígena.
    Gerencia a janela do jogo, eventos e a lógica principal do loop do jogo.
    """

    def __init__(self):
        """Inicializa o jogo e define os recursos iniciais."""
        pygame.init()  # Inicializa todos os módulos do Pygame 
                       # (som, vídeo, fonte, etc.)
        
        # Cria uma instância da classe Settings com as configurações do jogo
        self.settings = Settings()

        # Cria a janela do jogo com tamanho 1200x800 pixels
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                              self.settings.screen_height))

        # Define o título da janela
        pygame.display.set_caption("Invasão Alienígena")

        # Cria um relógio para definir o fps do jogo
        self.clock = pygame.time.Clock()

        # Define a cor do background
        self.screen.fill(self.settings.bg_color)

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            # Verifica e trata os eventos do teclado, mouse e sistema
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Encerra o programa ao clicar no botão de fechar (X)
                    sys.exit()

            # Redesenha a tela a cada passagem pelo loop
            self.screen.fill(self.settings.bg_color)

            # Atualiza a tela com os elementos desenhados
            pygame.display.flip()

            # Define o frame rate em 60 fps
            self.clock.tick(60)

# O bloco abaixo garante que o jogo só será iniciado se este arquivo for 
# executado diretamente
if __name__ == '__main__':
    # Cria uma instância do jogo
    ai = AlienInvasion()
    # Inicia o loop principal do jogo
    ai.run_game()
