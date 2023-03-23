print("Olá,bem-vindo(a) ao cérebro:hemisfério esquerdo") 
print("Vamos começar,as seguinte variáveis:Raciocínio,números e linguagems")      
input(">Pressione Enter")

input("Um exemplo simples de raciocínio:(Press Enter)")
x=float(input("Se tenho x laranjas(digite o valor de x): "))
y=float(input("E colho mais y(Digite um valor novamento):")) 
calculo = x+y
print("Tenho",calculo,"Laranjas")

input("Agora representaremos o conhecimento que um aluno de ensino médio sabe sobre conjuntos números inteiros,ok?(Pressione Enter)")
print("O conjunto dos números inteiros é representado por Z. Reúne todos os elementos dos números naturais (N) e seus opostos. Assim, conclui-se que N é um subconjunto de Z (N ⊂ Z): Subconjuntos dos Números Inteiros: Z* = {..., –4, –3, –2, –1, 1, 2, 3, 4, ...} ou Z* = Z–[0]: conjuntos dos números inteiros não-nulos, ou seja, sem o zero. Z+ = {0, 1, 2, 3, 4, 5, ...}: conjunto dos números inteiros e não-negativos. Note que Z+ = N. Z*+ = {1, 2, 3, 4, 5, ...}: conjunto dos números inteiros positivos e sem o zero. Z – = {..., –5, –4, –3, –2, –1, 0}: conjunto dos números inteiros não-positivos.Z*– = {..., –5, –4, –3, –2, –1}: conjunto dos números inteiros negativos e sem o zero.")

input(print("Agora uma demonstração da capacidade de capacidade de linguagem(Pressione Enter novamente)"))

import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome},estou muito bem {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome},133.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000 átomos .{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome},Pratique exercícios,medite,alimente-se corretamente,reconheça pequenas conquistas,consulte um profissional especializado{os.linesep}')    
    else:
        print('Digite apenas as opções 1, 2 ou 3')    


def start():
    
    print('Olá, Bem vindo a Demostração de Linguagem do Hemisfério Direito')

    
    nome = input('Digite seu nome: ')
    
    while True:

        
        resposta = input(
            f'O que gostaria de saber hoje? {os.linesep}[1] - Oi como vai? {os.linesep}[2] - Quantas átomos há no universo? {os.linesep}[3] - E como acabar com o stress?{os.linesep}')
        
        
        processar_resposta(resposta, nome)


if __name__ =='__main__':
    start()
