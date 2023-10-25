
from conta  import Conta
from conta_poupanca import ContaPoupanca
from conta_especial import ContaEspecial


class Bbanco:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta: Conta):
        self.contas.append(conta)

    def cadastrar_Poupanca(self, conta: ContaPoupanca):
        self.contas.append(conta)

    def cadastrar_Especial(self, conta: ContaEspecial):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
            else:
                None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)

        if conta:
            conta.creditar(valor)
        else:
            conta = None

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        saldoso = Conta.get_saldo(numero)
        if conta:
            if saldoso > valor:
                conta.debitar(valor)
            else:
                conta = None

    def saldo(self, numero):
        conta = self.procurar_conta(numero)

        if conta:
            conta.get_saldo()
        else:
            conta = None

    def transferir(self, origem, destino, valor):
        conta0 = self.procurar_conta(origem)
        conta1 = self.procurar_conta(destino)
        saldoso = Conta.get_saldo(origem)

        if saldoso > valor:
            if conta0 and conta1:
                conta0.debitar(valor)
                conta1.creditar(valor)
            else:
                conta = None
        else:
            print('sem saldo')

    def render_juros(self, numero, taxa=0.01):
        conta = self.procurar_conta(numero)

        if conta:
            if isinstance(conta, ContaPoupanca):
                conta.render_juros(taxa)
            else:
                print('Operação Indisponível')
        else:
            conta = None

        def render_bonus(self, numero, bonus=0.01):
            conta = self.procurar_conta(numero)

            if conta:
                if isinstance(conta, ContaEspecial):
                    conta.render_bonus()
                else:
                    print('Operação Indisponível')
            else:
                conta = None

        def renderBonus(self, numero):
            self.procurar_conta(numero)
            conta.renderBonus()
