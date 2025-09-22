# Características do controle:
# - Cor
# - Altura
# - Profundidade
# - Largura

# #Métodos (funções que exerce):
# - Power
# - Mexernovolume
# - Mute
# - Menu

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def mudar_volume(self, botao):
        if botao == "+":
            print("Aumentar o volume")
        elif botao == "-":
            print("Diminuir o volume!")   


controle1 = ControleRemoto("branca", "10cm", "2cm", "3cm")
controle1.mudar_volume("+")
controle2 = ControleRemoto("preto", "15cm", "5cm", "5cm")
print(f"\nA cor do controle 1 é {controle1.cor} e a sua altura é de {controle1.altura}")

