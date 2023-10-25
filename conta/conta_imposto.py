from conta_abstrata import ContaAbstrata

class ContaImposto(ContaAbstrata):

    def __init__(self, numero):
        super().__init__(numero)

    def debitar(self, valor):
        self.saldo = self.saldo - (valor + (valor * 0.001))