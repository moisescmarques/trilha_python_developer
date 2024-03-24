class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor..')

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado):
       super().__init__(cor, placa, numero_rodas)
       self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")

moto = Motocicleta("Vermelha", "EGH08H2", 2)
moto.ligar_motor()

carro = Carro("Preto", "SFA7H31", 4)
carro.ligar_motor()

caminhao = Caminhao("Azul", "GDJ7832", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)