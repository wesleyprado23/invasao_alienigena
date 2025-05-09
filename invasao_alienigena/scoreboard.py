import pygame.font
from pygame.sprite import Group
from ship import Ship  # Importa a nave para representar vidas restantes

class Scoreboard:
    """Classe responsável por exibir informações de pontuação na tela.

    Mostra:
    - Pontuação atual
    - Pontuação máxima (recorde)
    - Nível atual
    - Vidas restantes como ícones de naves
    """

    def __init__(self, ai_game):
        """Inicializa os atributos de exibição da pontuação."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Configuração visual: cor do texto e fonte
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara as imagens iniciais dos placares
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Converte a pontuação atual em uma imagem renderizada."""
        rounded_score = round(self.stats.score, -1)  # Arredonda para a dezena
        score_str = f"{rounded_score:,}"            # Adiciona separador de milhar

        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Exibe no canto superior direito
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def _check_high_score(self):
        """Verifica se um novo recorde foi alcançado e o atualiza."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def _check_high_score(self):
        """Verifica se um novo recorde foi alcançado e o atualiza."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_ships(self):
        """Cria ícones de naves representando as vidas restantes."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10  # Parte superior esquerda da tela
            self.ships.add(ship)

    def prep_high_score(self):
        """Converte a pontuação máxima em uma imagem centralizada."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"

        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        # Centraliza a pontuação máxima no topo da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def show_score(self):
        """Desenha as informações de pontuação na tela."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_level(self):
        """Converte o nível atual em uma imagem renderizada e posiciona abaixo da pontuação."""
        level_str = str(self.stats.level)

        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Posiciona o nível abaixo da pontuação atual
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
