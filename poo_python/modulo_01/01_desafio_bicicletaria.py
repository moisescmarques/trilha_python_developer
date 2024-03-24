class Bicicleta:
    
    #Construtor
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Tlim Tlim...")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")

    def acelerar(self):
        print("Vruuummmm...")

    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
        
    
KSW = Bicicleta("Laranja", "MTB", 2024, 1200)

KSW.acelerar()
KSW.buzinar()
KSW.parar()
print(KSW.cor, KSW.modelo, KSW.ano, KSW.valor)
print (KSW)