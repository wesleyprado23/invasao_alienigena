class Settings:
    """Classe que armazena todas as configurações do jogo Invasão Alienígena.

    Centraliza os parâmetros ajustáveis do jogo, como:
    - Tamanho da tela
    - Cores
    - Velocidades de nave e projéteis

    Isso facilita manutenção, balanceamento e personalização futura.
    """

    def __init__(self):
        """Inicializa as configurações estáticas do jogo.

        Esses valores não mudam durante o gameplay, mas podem ser alterados
        facilmente para testar diferentes comportamentos e experiências.
        """

        # ==============================
        # Configurações da tela
        # ==============================

        # Largura da janela do jogo (em pixels)
        self.screen_width = 1200

        # Altura da janela do jogo (em pixels)
        self.screen_height = 800

        # Cor de fundo da janela — usada apenas se não houver imagem de fundo
        self.bg_color = (230, 230, 230)  # Cinza claro (R, G, B)

        # ==============================
        # Configurações da nave
        # ==============================

        # Velocidade de movimento da nave (quanto ela se move por frame)
        self.ship_speed = 1.5

        # ==============================
        # Configurações dos projéteis
        # ==============================

        # Velocidade com que o projétil se move verticalmente
        self.bullet_speed = 10.0

        # Largura do projétil (em pixels)
        self.bullet_width = 3

        # Altura do projétil (em pixels)
        self.bullet_height = 15

        # Cor do projétil (tom de ciano)
        self.bullet_color = (0, 200, 255)

        # Quantidade máxima de projéteis permitidos na tela ao mesmo tempo
        self.bullets_allowed = 5
