class Settings:
    """Classe que armazena todas as configurações do jogo Invasão Alienígena.

    Essa classe centraliza os parâmetros ajustáveis do jogo, como:
    - Tamanho da janela
    - Cores de fundo
    - Velocidades da nave, dos projéteis e dos alienígenas

    Permite fácil manutenção e balanceamento da jogabilidade.
    """

    def __init__(self):
        """Inicializa as configurações estáticas do jogo.

        Esses valores não mudam durante uma partida, mas podem ser ajustados
        no início para alterar a dificuldade, o estilo visual, etc.
        """

        # ==============================
        # Configurações da tela
        # ==============================

        self.screen_width = 1200   # Largura da janela (px)
        self.screen_height = 800   # Altura da janela (px)
        self.bg_color = (230, 230, 230)  # Cor de fundo (cinza claro, RGB)

        # ==============================
        # Configurações da nave
        # ==============================

        self.ship_speed = 5.5      # Velocidade da nave
        self.ship_limit = 3        # Número de vidas (naves restantes)

        # ==============================
        # Configurações dos projéteis
        # ==============================

        self.bullet_speed = 10.0   # Velocidade vertical do projétil
        self.bullet_width = 3      # Largura do projétil
        self.bullet_height = 15    # Altura do projétil
        self.bullet_color = (0, 200, 255)  # Cor do projétil (ciano)
        self.bullets_allowed = 3   # Limite de projéteis ativos simultaneamente

        # ==============================
        # Configurações dos alienígenas
        # ==============================

        self.alien_speed = 3.5         # Velocidade de deslocamento horizontal
        self.fleet_drop_speed = 10     # Distância que a frota desce ao atingir borda

        # Direção da frota:
        # 1 = direita, -1 = esquerda
        self.fleet_direction = 1
