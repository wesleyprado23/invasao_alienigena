import sys  # Módulo usado para encerrar o programa
import pygame  # Biblioteca para desenvolvimento de jogos em Python

from settings import Settings         # Importa as configurações do jogo
from ship import Ship                 # Importa a nave do jogador
from bullet import Bullet             # Importa a classe dos projéteis

class AlienInvasion:
    """Classe principal do jogo Invasão Alienígena.

    Responsável por:
    - Inicializar o jogo
    - Gerenciar a janela e recursos principais
    - Lidar com entrada do jogador e atualizações visuais
    - Executar o loop principal do jogo
    """

    def __init__(self):
        """Inicializa o jogo e define os recursos iniciais."""
        pygame.init()

        # Carrega configurações gerais do jogo (tela, nave, projéteis etc.)
        self.settings = Settings()

        # Cria a janela com tamanho definido nas configurações
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Invasão Alienígena")

        # Carrega e ajusta a imagem de fundo do jogo
        self.bg_image = pygame.image.load('images/backgrounds/space_bg.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Cria a nave do jogador
        self.ship = Ship(self)

        # Grupo de projéteis disparados
        self.bullets = pygame.sprite.Group()

        # Controlador de taxa de atualização da tela
        self.clock = pygame.time.Clock()

    def _check_events(self):
        """Lida com eventos do sistema e do teclado (input do jogador)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde às teclas pressionadas."""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde às teclas soltas (interrompe o movimento)."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Cria um novo projétil (se permitido) e o adiciona ao grupo de projéteis."""
        # Verifica se ainda é permitido disparar mais projéteis
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Atualiza a tela com os elementos do jogo."""
        # Desenha o fundo
        self.screen.blit(self.bg_image, (0, 0))

        # Desenha todos os projéteis ativos
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Desenha a nave do jogador
        self.ship.blitme()

        # Atualiza a tela com o novo conteúdo desenhado
        pygame.display.flip()

    def run_game(self):
        """Loop principal do jogo — roda até o jogador sair."""
        while True:
            self._check_events()       # Processa entrada do jogador
            self.ship.update()         # Atualiza posição da nave
            self.bullets.update()      # Atualiza posição dos projéteis

            # Remove projéteis que saíram da tela
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()      # Desenha tudo na tela
            self.clock.tick(60)        # Mantém o jogo em 60 FPS

# Executa o jogo apenas se este arquivo for executado diretamente
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
