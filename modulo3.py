from ast import Import
import functools


from functools import reduce

""" nome = 'Siomara'
idade = 33
peso = 84.4
feriado = True

print('Os tipos das variáveis acima são: ',(type(nome)),(type(idade)),(type(peso)),
(type(feriado))) """

#Variável:
"""velocidade_do_carro = 200
print(velocidade_do_carro)

gosta_de_batata = True
print(gosta_de_batata)

luiza_code = "Sejam bem-vindas"
print(luiza_code)

sua_idade = 33
print(sua_idade)"""

#Comentário
"""São com o caracter jogo da velha, no início da linha ou 3 aspas duplas antes 
e depois das linhas que deseja comentar.
A tecla de atalho no meu vc code é shift + alt + A.
O comentário sobe no git push, mas para o deploy é melhor tirar. É melhor tirar
os comentários também na hora de fazer review.
O Comentário não é interpretado no terminal."""

#Operadores

"""Operadores aritméticos
Serve para fazer operações matemáticas comuns

Exemplos:

num1 = 4
num2 = 2

soma = num1 + num2
print(soma)

subtração = num1 - num2
print(subtração)

multiplicação = num1 * num2
print(multiplicação)

divisao = num1 / num2
print(divisao)

divisao_interna = num1 // num2
print(divisao_interna)

modulo = num1 % num2
print(modulo)

exponenciacao = num1 ** num2
print(exponenciacao)"""

"""Operadores comparativos
São usados para fazerem as comparações entre as variáveis"""

""" num3 = 5

if num3 == 5:
    print('Valor é igual a 5')

if num3 !=7:
    print('Valores são diferentes')    

if num3 > 2:
    print('Valor maior que 2')

if num3 < 7:
    print('Valor menor que 7')

if num3 <= 5:
    print('Valor é menor ou igual a 5')

if num3 >= 5:
    print('Valor é maior ou igual a 5') """

"""Operadores de atribuição
São usados parar atribuir valores as variáveis e controlam como a atribuição será
realizada"""

""" num4 = 5
num4 += 7
print(num4)

num4 = 5
num4 -= 3
print(num4)

num4 = 5
num4 *= 2
print(num4)

num4 = 5
num4 /= 4
print(num4)

num4 = 5
num4 %= 2
print(num4) """

""" Operadores lógicos
para usar em construção lógica
- and: retorna true se ambas as informações são verdadeiras
- or: uma das condições é verdadeira
- not: inverte o resultado da condição entre os parâmetros"""

""" num6 = 7
num7 = 4

if num6 > 3 and num7 < 8:
    print('As duas condições são verdadeiras')

if num6 > 4 or num7 <= 8:
    print('Uma ou duas das condições são verdadeiras')

if not (num6 < 30 and num7 < 8): #as duas condições precisa ser verdadeiras ou falsas
    print('Inverte o resultado da condição entre os parâmetros')
else:
    print(True)

lista = ['a', 'b', 'c', 'd'] 
if 'c' not in lista:
    print('não tem o c na lista')
else:
    print('tem o c na lista')"""

#Questão 9 da lista:

"""valor = input("Informe um valor: ")
print("Valor informado: ", valor)
tipo = type(valor)
x_str = "123"
x = int(x_str)
xf = float(x_str)
sao_iguais = x == xf
print("Um float é igual a um int?", sao_iguais)"""

# Resposta do Quiz - Pergunta 3
""" a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a.pop(),a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.pop()
print(a)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
b = a.pop()
print(b) #Foi o método correto para o quiz """

# Resposta do Quiz - Pergunta 4
""" a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.append('too')
print(a) """

#Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
#verificação se a idade de Davi é maior que a idade de sua irmã.

""" list = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

print(len(list)) """

""" Final da aula sobre tuplas e funções:
def foo (value):
    print(f'Olá, esse é o parâmetro: {value}')

foo('Luiza Code') 

Lições extras sobre funções:

Map:
lista = [100, 248.90, 88, 124.90]

def desconto(preco):
    return preco * (1-0.1)

lista_de_desconto = list(map(desconto, lista))
print(lista_de_desconto)

Filter:
maior_que_100 = list(filter (lambda x: x > 100, lista))
print(maior_que_100)

Reduce: 
nova_lista = []

for i in lista:
    nova_lista.append(float(i))
    
print(nova_lista)

reducao_lista = reduce(lambda x, y: x + y, nova_lista, 0)
print(reducao_lista)"""