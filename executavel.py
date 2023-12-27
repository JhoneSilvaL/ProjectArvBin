from arvBinaria import ArvBinaria
from no import No
from aluno import Aluno

import sys
import os
import time

arvoreBinaria = ArvBinaria()

def pressionar_enter_limpar():
    # Aguardar pelo Enter
    input("\tPressione Enter para limpar a tela...")
    
    # Limpar a tela
    if os.name == 'nt':  # Verifica se é Windows
        os.system('cls')
    else:  # Outros sistemas (Unix)
        os.system('clear')

while (True):
    print("")
    print("\t --------------------------------------- ")
    print("\t| 1. Adicionar um aluno\t\t\t|")  #FEITO
    print("\t| 2. Listar todos os alunos\t\t|") #FEITO
    print("\t| 3. Remover aluno pela matrícula\t|") #FEITO
    print("\t| 4. Buscar aluno pela matrícula\t|") #FEITO
    print("\t| 5. Total de alunos cadastrados\t|") 
    print("\t| 6. Cadastrar notas de um aluno\t|") 
    print("\t| 7. Calcular média de um aluno\t\t|") 
    print("\t| 0. Sair\t\t\t\t|")
    print("\t --------------------------------------- ")
    
    opcao = input("\n\t\t|   Digite uma opção   |\n\t\t--->:")

    if opcao == '1': #OKAY, TESTADO E APROVADO COM SELO.
        # #inserido alunos de maneira manual e direta #TESTE
        # aluno1 = Aluno("Jhone", 2077, 100.0, 100.0)
        # aluno2 = Aluno("Marcos", 2076, 79.0, 45.0)
        # aluno3 = Aluno("Laura", 2075, 87.0, 76.0)
        # aluno4 = Aluno("Vinícios", 2074, 95.0, 65.0)
        # #UTILIZANDO O METODO INSERIR DA ARVORE BINÁRIA
        # arvoreBinaria.inserirAluno(aluno1)
        # arvoreBinaria.inserirAluno(aluno2)
        # arvoreBinaria.inserirAluno(aluno3)
        # arvoreBinaria.inserirAluno(aluno4)
        # #EXIBINDO MENSAGEM DE CONFIRMAÇÃO
        # print("Alunos adicionados")

        while True:
            nome = input("Insira o nome do aluno (ou 'sair' para encerrar): ")
            if nome.lower() == 'sair':
                break

            elif nome.strip() == '':
                print("Nome não pode estar vazio. Por favor, insira o nome do aluno.")
                continue

            matricula_input = input("Insira a matrícula do aluno: ")
            if matricula_input.strip() == '':
                print("Matrícula não pode estar vazia. Por favor, insira a matrícula.")
                continue

            matricula = int(matricula_input)

            nota1_input = input("Insira a primeira nota do aluno: ")
            nota2_input = input("Insira a segunda nota do aluno: ")

            if nota1_input.strip() == '' or nota2_input.strip() == '':
                print("As notas não podem estar vazias. Por favor, insira as notas.")
                continue

            nota1 = float(nota1_input)
            nota2 = float(nota2_input)

            novo_aluno = Aluno(nome, matricula, nota1, nota2)
            arvoreBinaria.inserirAluno(novo_aluno)

            print("Aluno adicionados")

    elif opcao == '2': #OKAY, TESTADO E APROVADO COM SELO.
        #CRIANDO VARIÁVEL QUE RECEBE O MÉTODO EXIBIRTODOS OS ALUNOS 
        exibir_em_ordem = arvoreBinaria.exibirTodosAlunos()
        #exibindo as informações encontrada
        print(exibir_em_ordem)

    elif opcao == '3': #OKAY, TESTADO E APROVADO COM SELO.
        #matrícula inserida pelo usuario é passada como argumento para a função busca.
        #O resultado da busca é armazenado na variável aluno encontrado.
        matricula = input("Insira a matrícula do aluno: ")
        #criando variável que recebe o resultado do método buscar matrícula.
        aluno_encontrado = arvoreBinaria.buscarMatricula(matricula)

        if aluno_encontrado:
            #criando variável que recebe o resultado do método remover matrícula.
            removido_com_sucesso = arvoreBinaria.removeMatricula(matricula)
            if removido_com_sucesso:
                print("Aluno encontrado na árvore binária e suas informações foram deletadas.")
            else:
                print("Erro ao deletar informações do aluno encontrado na árvore binária.")
        else:
            print("Aluno não encontrado na árvore binária.")
        
    elif opcao == '4': #OKAY, TESTADO E APROVADO COM SELO.
        #matrícula inserida pelo usuario é passada como argumento para a função busca.
        #O resultado da busca é armazenado na variável aluno encontrado.
        matricula = input("Insira a matrícula do aluno: ")
        #criando variável que recebe o resultado do método buscar matrícula.
        aluno_encontrado = arvoreBinaria.buscarMatricula(matricula) 
        
        #condicionais
        if aluno_encontrado:
            print("Nome:", aluno_encontrado.nome)
            print("Matrícula:", aluno_encontrado.matricula)
            print("Nota 1:", aluno_encontrado.nota1)
            print("Nota 2:", aluno_encontrado.nota2)
        else:
            print("Aluno não encontrado na árvore binária.")

    elif opcao == '5':
        exibir_quantidade = arvoreBinaria.totalNO()
        print("Total de alunos cadastrados são: ",exibir_quantidade)

    elif opcao == '6':
        matricula = input("Insira a matrícula do aluno: ")
        aluno_encontrado = arvoreBinaria.buscarMatricula(matricula)

        if aluno_encontrado:
            print("Aluno encontrado na árvore binária.")
            nota1 = float(input("Insira a primeira nota do aluno: "))
            nota2 = float(input("Insira a segunda nota do aluno: "))
            aluno_encontrado.inserirNotas(nota1,nota2)

        else:
            print("Aluno não encontrado na árvore binária.")
      
    elif opcao == '7':
        # matricula = input("Insira a matrícula do aluno: ")
        # aluno_encontrado = arvoreBinaria.buscarMatricula(matricula)

        # if aluno_encontrado:
        #     media_aluno = aluno_encontrado.calcularMedia()
        #     print("Média do aluno: ",media_aluno)
        # else:
        #     print("Aluno não encontrado na árvore binária.") 
        matricula = input("Insira a matrícula do aluno: ")
        aluno_encontrado = arvoreBinaria.buscarMatricula(matricula)

        if aluno_encontrado:
            print("Aluno encontrado na árvore binária.")
            if aluno_encontrado.nota1 is not None and aluno_encontrado.nota2 is not None:
                media_aluno = aluno_encontrado.calcularMedia(aluno_encontrado.nota1, aluno_encontrado.nota2)
                print("Média do aluno:", media_aluno)
            else:
                print("Notas não foram inseridas para calcular a média.")
        else:
            print("Aluno não encontrado na árvore binária ou objeto inválido.")

    elif opcao == '0':
        print("\n\t ----------------------------- ")
        print("\t|     PROGRAMA ENCERRADO      |")
        print("\t ----------------------------- ")
        time.sleep(2)
        sys.exit()
    else:
        print("\t ----------------------------- ")
        print("\t| Digite a opção corretamente |")
        print("\t ----------------------------- ")

    pressionar_enter_limpar()