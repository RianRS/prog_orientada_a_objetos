from p.conta.conta import Conta
from p.conta.conta_poupanca import ContaPoupanca
from p.conta.conta_especial import ContaEspecial
from p.conta.conta_abstrata import ContaAbstrata
from p.exception import CIExpection
from p.expection.new_expection import SIExpection


class BancoLista:
    def __init__(self):
        self.contas = []

    def cadastrar(self, ContaAbstrata):
        self.contas.append(ContaAbstrata)

    def procurar_conta(self, numero):

        for conta in self.contas:
            if conta.get_numero() == numero:
                return conta
            else:
                return None

    def debitar(self, numero, valor):
        try:
            conta = self.procurar_conta(numero)
            conta.debitar(valor)
        except CIExpection(numero) as erroci:
            print(erroci)

        except SIExpection(conta.get_saldo(), conta.get_numero()) as errorsi:
            print(errorsi)


    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        if isinstance(conta, ContaEspecial):
            self.render_bonus(numero)
        else:
            print("Conta Inexistente!")

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            return conta.get_saldo()
        else:
            print("Conta Inexistente!")

    def transferir(self, origem, destino, valor):
        origem = self.procurar_conta(origem)
        destino = self.procurar_conta(destino)

        if origem and destino:
            if self.saldo(origem.get_numero()) >= valor:
                origem.debitar(valor)
                destino.creditar(valor)
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo Insuficiente, faça um empréstimo")
        else:
            print('Transferência impossível! Conta inexistente.')

    def render_bonus(self, conta, valor):
        if isinstance(conta, ContaEspecial):
            conta.creditar(valor)
            conta.renderBonus()
            print('Saldo com bônus: {}'.format(conta.get_saldo()))
        else:
            return False

