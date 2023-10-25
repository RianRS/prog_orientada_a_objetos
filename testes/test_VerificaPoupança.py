from p.conta.conta_poupanca import ContaPoupanca
from p.conta.conta import Conta


class VerificaPoupanca:
    if __name__ == '__main__':
        opcao = int(input('Escolha [1] para Conta ou [2] para Poupança: '))
        if opcao == 1:
            conta = Conta('21.342-7')
        else:
            conta = ContaPoupanca('21.342-7')

        conta.creditar(500.87)
        conta.debitar(45.00)


        if isinstance(conta, ContaPoupanca):
            conta.render_juros()
            print('Saldo com juros: {}'.format(conta.get_saldo()))