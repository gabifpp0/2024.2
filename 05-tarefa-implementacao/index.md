# Implementação de tarefas

## Informações gerais

- Capítulo: [Implementação de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-05.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Gabrielle Fernandes Paiva Pereira
- matrícula: 20241014040003

## Respostas dos exercícios

## Soma com 4 tarefas - Implentação com threads

import threading

class MinhaThread(threading.Thread):
    def __init__(self, numeros):
        threading.Thread.__init__(self)
        self.numeros = numeros
        self.resultado = 0

    def run(self):
        self.resultado = sum(self.numeros)

def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

nome_arquivo = 'numeros_aleatorios.txt'
numeros = ler_numeros_do_arquivo(nome_arquivo)

tamanho_parte = len(numeros) // 4
partes = [numeros[i:i + tamanho_parte] for i in range(0, len(numeros), tamanho_parte)]

if len(partes) > 4:
    partes[3] += partes[4:]
    partes = partes[:4]

threads = [MinhaThread(parte) for parte in partes]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

resultados = [thread.resultado for thread in threads]
soma_final = sum(resultados)

print(f"A soma dos números com 4 tarefas é: {soma_final}")

## Soma com 10 tarefas - Implementação com ThreadPoolExecuter

from concurrent.futures import ThreadPoolExecutor

def soma_numeros(numeros):
    return sum(numeros)

def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

nome_arquivo = 'numeros_aleatorios.txt'
numeros = ler_numeros_do_arquivo(nome_arquivo)

tamanho_parte = len(numeros) // 10
partes = [numeros[i:i + tamanho_parte] for i in range(0, len(numeros), tamanho_parte)]

if len(partes) > 10:
    partes[9] += partes[10:]
    partes = partes[:10]

with ThreadPoolExecutor(max_workers=10) as executor:
    futuros = [executor.submit(soma_numeros, parte) for parte in partes]
    resultados = [futuro.result() for futuro in futuros]

soma_final = sum(resultados)

print(f"A soma dos números com 10 tarefas é: {soma_final}")