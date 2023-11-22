from faker import Faker
from wordcloud import WordCloud
from num2words import num2words
import matplotlib.pyplot as plt
import threading

## Classe pessoas ##
class Pessoas:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

## Função para gerar os dados ##
def fazDados():
    fake = Faker('pt_BR')
    lista = []
    for a in range(10):
        nota = fake.random_int(1, 10)
        nome = fake.name()
        dados = Pessoas(nome, nota)
        lista.append(dados)
    return lista

# variável que recebe nossa lista com arquivos random ##
lista = fazDados()

## Função que grava os dados no arquivo txt ##
def gravar(lista):
    arquivo = open('Dados.txt', 'w+')
    for dados in lista:
        arquivo.write(dados.nome + "," + str(dados.nota) + "\n")

    arquivo.close()

gravar(lista)

## Função para importar dados do nosso arquivo txt
def importar():
    arquivo = open('Dados.txt', 'r')
    lista = arquivo.read().splitlines()
    lista_random = []
    for NomesNotas in lista:
        lista2 = NomesNotas.split(',')
        dados = Pessoas(lista2[0], lista2[1])
        lista_random.append(dados)
    arquivo.close()

    return lista_random

## Função que gera o Histograma ##
def fazHistograma(lista):
    plt.hist(lista, density=True, facecolor='blue', alpha=0.80)
    plt.xlabel('Pontuações')
    plt.ylabel('Probabilidade')
    plt.title('Histograma das Pontuações')
    plt.grid(True)
    plt.show()

## Gerando o dados para o Histograma ##
lista1 = importar()
listaNotas = []
listaOrdenada = []
for i in lista1:
    numero = int(i.nota)
    listaNotas.append(numero)
    num_ptbr = num2words(numero, lang='pt-br')
    listaOrdenada.append(num_ptbr)

## Criando uma variável para começar a nuvem de palavras ##
texto = (" ").join(listaOrdenada)