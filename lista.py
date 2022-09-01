# Respostas da Lista

""" 1) O Python trabalha tipos de valores. Com os valores abaixo, dê o nome de seus tipos:

a = 1
print(type(a))

b = 12.6
print(type(b))

c = True
print(type(c))

d = False
print(type(d))

e = 543
print(type(e))

f = -5.78
print(type(f))

g = "copo"
print(type(g))

h = 'Belo dia'
print(type(h))
"""

"""2-Digite cada linha abaixo no shell do Python e informe quais estão corretos e quais
apresentam erro:

1 imprime 1
1a imprime erro
a1 imprime erro
1. imprime 1.
.2 imprime 0,2
-.3 imprime -0,3
'agua"limpa' imprime agua"limpa
"agua"" não imprime nada (erro)
aspas triplas teste 1 2 3 aspas triplas imprime aspas triplas teste 1 2 3 aspas triplas
"""

"""3) Determine qual é o resultado dos seguintes cálculos no Python: 
a. Operadores matemáticos

i = 10 + 3
print(i)

ii = 10 - 3
print(ii)

iii = 10 * 3
print(iii)

iv = 10 / 3
print(iv)

v = 10 / 3.0
print(v)

vi = 13 / 3
print(vi)

vii = 13 / 3.0
print(vii)

viii = 13 // 3.0
print(viii)

b. Ordem dos operadores

i = 5 + 30 * 20
print(i)

ii = (5 + 30) * 20
print(ii)

iii = ((5 + 30) * 20) / 10
print(iii)

iv = 5 + 30 * 20 / 10
print(iv)

c. Operadores comparação

i = 2 < 3
print(i)

ii = 9 > 8
print(ii)

iii = 1 == 1
print(iii)

iv = 1 != 2
print(iv)

v = 1 != 1
print(v)

vi = 4 <= 4
print(vi)

vii = 5 >= 6
print(vii)

viii = 1 < 2 < 3
print(viii)

ix = 1 < 2 < 2
print(ix)

x = 1 + 2 < 25 / 5
print(x) 

d. Mais operadores matemáticos:

i = 2 ** 4
print(i)

ii = 26 % 5
print(ii)

e. Operadores lógicos

i = not True
print(i)

ii = not False
print(ii)

iii = True and True
print(iii)

iv = True and False
print(iv)

v = False and True
print(v)

vi = False and False
print(vi)

vii = True or True
print(vii)

viii = True or False
print(viii)

ix = False or True
print(ix)

x = False or False
print(x)

xi = True or True and False
print(xi)

xii = (True or True) and False
print(xii)

xiii = not True or False
print(xiii)

xiv = not (True or False)
print(xiv)

xv = not (True and False) and (True or False)
print(xv)

xvi = 1 > 2 and 3 > 4
print(xvi)

xvii = 1 > 2 and 3 < 4
print(xvii)

xviii = 1 < 2 and 3 < 4
print(xviii)

xix = 1 + 2 and 3 + 4
print(xix)

xx = 1 + 2 or 3 + 4
print(xx)

xxi = True and 3 > 5
print(xxi)

xxii = False and 3 >5
print(xxii)

4) Qual será o valor final de x?

x = 10
x = x + 10
x = 100 - x

print(x)
Resposta= x=80

5) Resolva estes problemas em Python, guardando os valores e seus resultados em
variáveis diferentes.
a. Calcule a área de um quadrado cujo lado seja 2 cm.
l = 2
a = l ** 2

print(a)

b. Uma mala custa R$120,00. Esta recebeu 5% de desconto. Quanto você irá pagar
por ela.
valor_da_mala = 120
valor_do_desconto = 0.05

valor_final_mala = valor_da_mala - (valor_da_mala * valor_do_desconto)
print(valor_final_mala)

c. Um carro está viajando a uma velocidade média de 100 Km/h, o trecho de viagem
será 200 Km. Quantas horas irá demorar a viagem.
v_media = 100
percurso = 200

h_de_viagem = percurso / v_media
print(h_de_viagem)

d. João tem 2 pirulitos, Maria 3 pirulitos e Sofia 1 pirulito. Calcule o total de pirulitos e
sua média.
qtd_pirulitos_joao = 2
qtd_pirulitos_maria = 3
qtd_pirulitos_sofia = 1

qtd_de_criacas = 3

qtd_total_pirulitos = qtd_pirulitos_joao + qtd_pirulitos_maria + qtd_pirulitos_sofia
print(qtd_total_pirulitos)

qtd_media_pirulitos = qtd_total_pirulitos / qtd_de_criacas
print(qtd_media_pirulitos)

e. Davi tem 13 anos e sua irmã tem 7 anos. Guarde na variável eh_mais_velho a
verificação se a idade de Davi é maior que a idade de sua irmã.

idadeDavi = 13
idadeIrma = 7


if (idadeDavi > idadeIrma):
    eh_mais_velho = idadeDavi
if (idadeIrma > idadeDavi):
    eh_mais_velho = idadeIrma
print(eh_mais_velho)

6) Qual será o valor de z? Qual seria outra forma de escrever este trecho de código?
z = 3
z += 2
z *= 6
z /= 5

Resposta: z = 6

z = 3
acrescentar_2 = z + 2
multiplicar_6 = acrescentar_2 * 6
dividir_5 = multiplicar_6 / 5

print(dividir_5)

7) Considere as seguintes variáveis:
ovo = 3.4
caju = 12.4
Qual será o valor de resposta em cada linha:
resposta = ovo if 1 > 2 else caju - R = 
resposta = ovo if ovo > caju else caju
resposta = ovo if ovo < caju else caju
resposta = 100 if ovo + caju > 15 else 200
resposta = 100 if ovo == 3 else 0

"""



"""15). Para o programa Python no arquivo ex15.py: Em uma casa, uma família decidiu dividir
o valor da conta de energia entre os moradores da casa. No programa eles informam o
valor da conta de energia e quantos que irão pagar a conta no mês. O programa calculará
quanto cada um deverá contribuir com a conta de energia.


valor_energia = float(input("Informe o valor da conta de enrgia: "))
qtd_moradores = int(input("Quantos moradores: "))

print(type(valor_energia))

valor_cada_morador = float(valor_energia / qtd_moradores)

print(valor_cada_morador) 

Exemplos da aula:
lista = ['banana', 'caju', 'melão', 5, 'pera', 10]


for index, elemento in enumerate(lista):
    if elemento = int:
        lista.pop()
    print(index)

    """
""" result = map(lambda x: desconto(x),lista) """


