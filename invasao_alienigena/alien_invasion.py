import sys  # Usado para encerrar o jogo com sys.exit()
import pygame  # Biblioteca principal de desenvolvimento de jogos 2D
from time import sleep

from settings import Settings       # Configurações gerais do jogo
from game_stats import GameStats
from ship import Ship               # Classe da espaçonave do jogador
from bullet import Bullet           # Classe dos projéteis
from alien import Alien             # Classe dos alienígenas

class AlienInvasion:
    """Classe principal do jogo Invasão Alienígena.

    Responsável por:
    - Inicializar e configurar recursos
    - Processar entradas do jogador
    - Atualizar a lógica do jogo
    - Desenhar os elementos na tela
    - Executar o loop principal
    """

    def __init__(self):
        """Inicializa o jogo e os recursos principais."""
        pygame.init()

        self.settings = Settings()

        # Cria a janela do jogo
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Invasão Alienígena")

        # Cria uma instância para armazenar estatísticas do jogo
        self.stats = GameStats(self)

        # Carrega e redimensiona a imagem de fundo
        self.bg_image = pygame.image.load('images/backgrounds/space_bg.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()  # Cria a frota inicial de alienígenas
        self.clock = pygame.time.Clock()  # Controla o FPS

        # Inicializa o jogo em um estado ativo
        self.game_active = True

    def _check_events(self):
        """Lida com eventos do sistema (teclado, saída do jogo etc.)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Lida com teclas pressionadas."""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Lida com teclas liberadas (interrompe movimento da nave)."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Cria um novo projétil (se ainda não atingiu o limite permitido)."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualiza a posição dos projéteis e remove os que saíram da tela."""
        self.bullets.update()

        # Remove projéteis que atingiram o topo da tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Verifica colisões entre projéteis e alienígenas."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if not self.aliens:
            # Se todos os alienígenas forem destruídos, recria a frota
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Responde à espaçonave sendo abatida"""
        # Decrementa ships_left
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            # Descarta quaisquer projéteis e aliens restantes
            self.bullets.empty()
            self.aliens.empty()

            # Cria uma frota nova e centraliza a espaçonave
            self._create_fleet()
            self.ship.center_ship()

            # Pausa
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Verifica se algum alien chegou a borda inferior"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Trata isso como se a espaçonave tivesse sido abatida
                self._ship_hit()
                break

    def _update_aliens(self):
        """Atualiza a posição da frota de alienígenas e detecta colisões com a nave."""
        self._check_fleet_edges()
        self.aliens.update()

        # Verifica se algum alien colidiu com a nave
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Procura por aliens chegando a borda inferior
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Detecta se algum alienígena tocou a borda da tela."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move a frota para baixo e inverte a direção horizontal."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Cria uma frota de alienígenas dispostos em linhas e colunas."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            current_x = alien_width
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width  # Espaçamento horizontal
            current_y += 2 * alien_height      # Espaçamento vertical

    def _create_alien(self, x_position, y_position):
        """Cria e posiciona um alienígena individual."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Atualiza o visual da tela com todos os elementos do jogo."""
        self.screen.blit(self.bg_image, (0, 0))  # Fundo

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        """Loop principal do jogo — processa eventos, atualiza e desenha."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

# Executa o jogo apenas se este arquivo for executado diretamente
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
