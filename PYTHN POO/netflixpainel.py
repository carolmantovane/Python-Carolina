# Criar uma classe para clientes Netflix

class Cliente ():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["Básico", "Premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")   
    
    
    # def ver_filmes(self, filme):

cliente = Cliente("João", "joao@mail.com", "Básico")
print(cliente.nome)
print(cliente.plano)


#Botão mudar de plano
cliente.mudar_plano("Premium")
print(cliente.nome)
print(cliente.plano)