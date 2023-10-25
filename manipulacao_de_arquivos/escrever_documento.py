# Escrevendo em um arquivo de texto e lendo
arq = open ('texto.txt', 'w')
arq.write('Olá visitante')
arq.close()
arq = open('texto.txt')
x = arq.read()
print(x)
print('\n')

# Sobrescrevendo o arquivo anterior
f = open('texto.txt', 'w')
f.write('Olá mundo!\nOlá Python')
f.close()
print('\n')

# Lendo até chegar em um limite
f = open('texto.txt') # r é default
ler = f.read(4)
restante = f.read()
f.close()
print(ler)
print(restante)
print('\n')

# Lendo linha por linha
f = open('texto.txt', 'r')
linha1 = f.readline()
linha2 = f.readline()
f.close()

print(linha1)
print(linha2)
print('\n')