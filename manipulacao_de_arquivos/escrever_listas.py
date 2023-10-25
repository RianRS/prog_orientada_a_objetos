# Escrevendo em listas
lista = ['Olá mundo\n', 'Olá Python\n', 'Olá UFC']
f = open('texto.txt', 'w')
f.writelines(lista)
f = open('texto.txt', 'r')
cont = f.readlines()
print(cont)
f.close()
print('\n')

# Retornando todas as palavras em caixa alta
for linha in cont:
    print(linha.upper())