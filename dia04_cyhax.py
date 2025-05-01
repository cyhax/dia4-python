# DIA 4 (01/05/2025) - Strings, módulos e manipulação de dados

# Exercício 16 - Parte inteira de um número
import math
num = float(input('Digite um numero '))
inteiro = math.trunc(num)
print(f'o numero inteiro é {inteiro}')

# Exercício 17 - Cálculo da hipotenusa
import math
n1 = float(input('Qual é o cateto oposto? '))
n2 = float(input('Qual é o cateto adjacente? '))
n3 = math.pow(n1,2)
n4 = math.pow(n2, 2)
op = n3 + n4
hipotenusa = math.sqrt(op)
print(f'A hipotenusa é = {hipotenusa:.2f}')

# Exercício 18 - Cálculo de seno, cosseno e tangente
import math
a1 = int(input('Digite um angulo '))
r1 = math.radians(a1)
s1 = math.sin(r1)
c1 = math.cos(r1)
t1 = math.tan(r1)
print(f'O seno é {s1:.2f}\nO cosseno é {c1:.2f}\nA tangente é {t1:.2f}')

# Exercício 19 - Sorteio de um aluno
import random
nome1 = input('Digite o nome do primeiro aluno ')
nome2 = input('Digite o nome do segundo aluno ')
nome3 = input('Digite o nome do terceiro aluno ')
nome4 = input('Digite o nome do quarto aluno ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'A pessoa escolhida para limpar para apagar a lousa é {escolhido}')

# Exercício 20 - Ordem de apresentação dos alunos
import random
nome1 = input('Digite o nome do primeiro aluno ')
nome2 = input('Digite o nome do segundo aluno ')
nome3 = input('Digite o nome do terceiro aluno ')
nome4 = input('Digite o nome do quarto aluno ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f'A ordem de apresentação é {lista}')

# Exercício 21 - Tocar música MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ha.mp3')
pygame.mixer.music.play()
input('Aperte ENTER para parar a música')

# Exercício 22 - Analisador de nome
nome = input('Digite seu nome: ').strip()
print(f'Nome em maiusculas {nome.upper()}')
print(f'Nome em minusculas {nome.lower()}')
print(f'Total de letras :{len(nome.replace(" ",""))}')
primeiro_nome =nome.split()
print(f'seu primeiro nome tem {len(primeiro_nome[0])} letras')

# Exercício 23 - Decomposição de número
num = input('Digite um numero de 1 a 9999: ').zfill(4)
print(f'Milhar: {num[0]}')
print(f'Centena: {num[1]}')
print(f'Dezena: {num[2]}')
print(f'Unidade: {num[3]}')

# Exercício 24 - Nome da cidade começa com SANTO
cidade = input('Digite o nome da cidade: ').strip()
print(cidade.upper().startswith('SANTO'))

# Exercício 25 - Verifica se nome contém SILVA
nome = input('Digite o seu nome: ').strip()
n1 = nome.upper()
print('SILVA' in n1)

# Exercício 26 - Análise da letra A
v1 = input('Digite uma frase: ').strip()
v2 = v1.upper()
print(f'A letra A aparece {v2.count("A")} vezes')
print(f'A primeira vez ela aparece na posição {v2.find("A")}')
print(f'A ultima vez ela aparece na posição {v2.rfind("A")}')

# Exercício 27 - Primeiro, segundo e último nome
n1 = input('Digite seu nome: ').strip()
v1 = n1.split()
print(f'O seu primeiro nome é {v1[0]}')
print(f'O seu segundo nome é {v1[1]}')
print(f'O seu ultimo nome é {v1[-1]}')
