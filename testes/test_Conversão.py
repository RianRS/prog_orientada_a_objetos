from p.conta.conta import Conta
from p.conta.conta_especial import ContaEspecial


# Criando uma conta do tipo Conta e creditando 20 reais
conta = Conta('31.345-X')
conta.creditar(20)
print(type(conta))

# Criando uma conta do tipo Conta Especial e creditando 70 reais
especial = ContaEspecial('31.547-X')
especial.creditar(70)
print(type(especial))

# Creditando 20 reais em conta e convertendo para Conta Especial
conta.creditar(20)
conta = especial
print(type(conta))
conta.creditar(20)

#Exibindo o saldo da conta
print(conta.get_saldo())