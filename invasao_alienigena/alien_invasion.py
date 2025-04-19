import sys          # Para encerrar o jogo
import pygame       # Biblioteca principal de jogos 2D
from time import sleep  # Para pausar após colisões

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Classe principal que gerencia o estado e comportamento do jogo."""
    
    def __init__(self):
        """Inicializa a janela, recursos, estados e elementos do jogo."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Invasão Alienígena")

        # Estatísticas e placar
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Fundo
        self.bg_image = pygame.image.load('images/backgrounds/space_bg.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image,
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Jogador e entidades
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.clock = pygame.time.Clock()

        self.game_active = False
        self.play_button = Button(self, "Play")

    def _check_events(self):
        """Verifica entrada do jogador: teclado, mouse, saída do jogo."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stats.save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(pygame.mouse.get_pos())

    def _check_play_button(self, mouse_pos):
        """Inicia uma nova partida se o botão Play for clicado."""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.game_active = True

            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Ativa movimento ou ações ao pressionar teclas."""
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
            self.stats.save_high_score()
            sys.exit()

    def _check_keyup_events(self, event):
        """Para o movimento quando as teclas são liberadas."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Cria um novo projétil se o limite não for atingido."""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        """Atualiza a posição dos projéteis e verifica colisões."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Gerencia as colisões entre balas e alienígenas."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens_hit in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens_hit)
            self.sb.prep_score()
            self.sb._check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

    def _ship_hit(self):
        """Responde ao impacto de um alien na nave."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Verifica se algum alien chegou à parte inferior da tela."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _update_aliens(self):
        """Atualiza a frota e detecta colisões com a nave ou base."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Inverte direção se algum alien tocar a borda da tela."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move a frota para baixo e inverte sua direção horizontal."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Organiza alienígenas em linhas e colunas na tela."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            current_x = alien_width
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Cria e posiciona um alienígena individual."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_screen(self):
        """Desenha o fundo, entidades, HUD e botão Play (se inativo)."""
        self.screen.blit(self.bg_image, (0, 0))

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def run_game(self):
        """Loop principal do jogo — ativa atualizações e renderização."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
