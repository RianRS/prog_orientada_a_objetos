class SIExpection(Exception):
    def __init__(self,saldo,numero,message = 'Saldo insuficiente'):
        self.saldo = saldo
        self.numero = numero
        self.message = message
        super().__init__(self.message)

    def saldoConta(self):
        return self.saldo