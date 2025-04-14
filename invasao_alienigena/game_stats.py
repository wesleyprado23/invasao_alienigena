class GameStats:
    """Classe responsável por rastrear as estatísticas do jogo.

    Isso inclui dados como:
    - Quantas vidas restam
    - Se o jogo está ativo
    - Pontuação e recordes (pode ser adicionado depois)
    """

    def __init__(self, ai_game):
        """Inicializa os dados de estatísticas do jogo.

        Parâmetros:
        ai_game — instância da classe principal (AlienInvasion),
                  usada para acessar configurações do jogo.
        """
        self.settings = ai_game.settings
        self.reset_stats()  # Inicializa as variáveis que mudam durante a execução

        # O jogo começa inativo (pode ser ativado por um botão "Play")
        self.game_active = False

    def reset_stats(self):
        """Reinicializa estatísticas que mudam durante o jogo ativo.

        Deve ser chamado ao começar uma nova partida.
        """
        self.ships_left = self.settings.ship_limit
