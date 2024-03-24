class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print("Removendo a instancia da classe.")


    def latir(self):
        print("auauau")

c = Cachorro("Pudim", "Preto")
c.latir()