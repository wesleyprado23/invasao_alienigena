class Settings:
    """Classe para armazenar todas as configurações do jogo.
    
    Essa classe centraliza os parâmetros ajustáveis do jogo,
    como tamanho da tela, cores e velocidade dos elementos.
    Isso facilita a manutenção e a personalização do jogo.
    """

    def __init__(self):
        """Inicializa os atributos estáticos de configuração do jogo.
        
        Esses valores permanecem constantes durante a execução,
        mas podem ser ajustados facilmente aqui antes do jogo começar.
        """

        # ==========================
        # Configurações da tela
        # ==========================

        # Largura da janela do jogo (em pixels)
        self.screen_width = 1200

        # Altura da janela do jogo (em pixels)
        self.screen_height = 800

        # Cor de fundo da janela do jogo (RGB: cinza claro)
        self.bg_color = (230, 230, 230)

        # ==========================
        # Configurações da nave
        # ==========================

        # Velocidade de movimento da nave
        # Usado para determinar quanto a posição da nave muda por frame
        self.ship_speed = 1.5
