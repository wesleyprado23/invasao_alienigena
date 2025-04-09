class Settings:
    """Classe para armazenar todas as configurações do jogo.
    
    Essa classe centraliza os parâmetros ajustáveis do jogo,
    como tamanho da tela e cores.
    Isso facilita futuras alterações sem precisar modificar diretamente
    outras partes do código.
    """

    def __init__(self):
        """Inicializa os atributos estáticos de configuração do jogo.
        
        Esses valores permanecem fixos durante a execução, 
        mas podem ser modificados aqui para alterar o comportamento do jogo
        como um todo (por exemplo, mudar o tamanho da tela).
        """

        # Configuração da tela:
        # Define a largura da janela do jogo, em pixels
        self.screen_width = 1200

        # Define a altura da janela do jogo, em pixels
        self.screen_height = 800

        # Cor de fundo da tela (background), no formato RGB
        self.bg_color = (230, 230, 230)

