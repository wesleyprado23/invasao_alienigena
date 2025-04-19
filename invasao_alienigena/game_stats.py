import json

class GameStats:
    """Classe responsável por rastrear as estatísticas do jogo."""

    def __init__(self, ai_game):
        """Inicializa os dados persistentes e chamáveis durante o jogo."""
        self.settings = ai_game.settings

        # Pontuação máxima deve ser carregada do disco
        self.high_score = self.load_high_score()

        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Reinicializa estatísticas que mudam durante a partida."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Tenta carregar a pontuação máxima de um arquivo local."""
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0  # Se o arquivo não existir, começa do zero

    def save_high_score(self):
        """Salva a pontuação máxima atual em um arquivo local."""
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)
