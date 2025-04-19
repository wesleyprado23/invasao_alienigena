class Settings:
    """Classe que armazena todas as configurações do jogo Invasão Alienígena.

    Centraliza os parâmetros ajustáveis para facilitar manutenção e balanceamento:
    - Tamanho da janela
    - Cores
    - Velocidades da nave, projéteis e inimigos
    - Dificuldade progressiva e pontuação
    """

    def __init__(self):
        """Inicializa as configurações estáticas do jogo.

        Estas permanecem constantes durante a execução, a menos que ajustadas
        em métodos auxiliares como `increase_speed`.
        """
        # ==============================
        # Configurações da tela
        # ==============================
        self.screen_width = 1200               # Largura da janela (px)
        self.screen_height = 800               # Altura da janela (px)
        self.bg_color = (230, 230, 230)        # Cor de fundo (cinza claro)

        # ==============================
        # Configurações da nave
        # ==============================
        self.ship_speed = 5.5                  # Velocidade da nave
        self.ship_limit = 3                    # Quantidade de vidas

        # ==============================
        # Configurações dos projéteis
        # ==============================
        self.bullet_speed = 10.0               # Velocidade dos projéteis
        self.bullet_width = 3                  # Largura (px)
        self.bullet_height = 15                # Altura (px)
        self.bullet_color = (0, 200, 255)      # Cor do projétil (ciano)
        self.bullets_allowed = 10              # Limite de projéteis simultâneos

        # ==============================
        # Configurações dos alienígenas
        # ==============================
        self.alien_speed = 3.5                 # Velocidade horizontal
        self.fleet_drop_speed = 10             # Queda vertical ao tocar a borda
        self.fleet_direction = 1               # 1 = direita, -1 = esquerda

        # ==============================
        # Dificuldade dinâmica
        # ==============================
        self.speedup_scale = 2.1               # Acelerador de dificuldade
        self.score_scale = 1.5                 # Aumento progressivo da pontuação

        # Inicializa configurações que mudam durante o jogo
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam com a progressão do jogo.

        Chamado no início de cada nova partida.
        """
        self.ship_speed = 5.5
        self.bullet_speed = 10.0
        self.alien_speed = 1.0

        self.fleet_direction = 1               # 1 = direita, -1 = esquerda
        self.alien_points = 50                 # Pontos por alien destruído

    def initialize_dynamic_settings(self):
        """Inicializa as configurações que mudam com a progressão do jogo.

        Chamado no início de cada nova partida.
        """
        self.ship_speed = 5.5
        self.bullet_speed = 10.0
        self.alien_speed = 1.0

        self.fleet_direction = 1               # 1 = direita, -1 = esquerda
        self.alien_points = 50                 # Pontos por alien destruído

    def increase_speed(self):
        """Aumenta progressivamente a dificuldade do jogo (velocidade e pontuação)."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
