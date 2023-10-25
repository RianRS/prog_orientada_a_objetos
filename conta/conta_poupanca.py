from p.conta.conta import Conta

class ContaPoupanca(Conta):

    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa = 0.01):
        self.creditar(self.get_saldo() * taxa)