class CIException(Exception):
    def __init__(self,saldo,numero,message='Conta Inexistente!'):
        self.saldo = saldo
        self.numero = numero
        self.message = message
        super().__init__(self.message)

    def numeroConta(self):
        return self.numero

