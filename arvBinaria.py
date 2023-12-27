from no import No

class ArvBinaria:
    def __init__(self):
        self.__raiz = None

    def vazia(self):
        if (self.__raiz == None):
            return True
        else:
            return False
#---------------------------------------------------------------------
    def totalNO(self): # (JÁ UTILIZADO JUNTO COM _TOTALNO)
        if (self.__raiz == None):
            return 0
        else:
            return self._totalNO(self.__raiz)

    def _totalNO(self, raiz):
        if (raiz == None):
            return 0

        total_esquerda = self._totalNO(raiz.esquerda)
        total_direita = self._totalNO(raiz.direita)
        return (total_esquerda + total_direita + 1)
#---------------------------------------------------------------------
    def altura(self): #CONTRIBUI PARA EXIBIR O TOTAL DE ALUNOS.
        if (self.__raiz == None):
            return 0
        else:
            return self.__altura(self.__raiz)

    def __altura(self, raiz):
        if (raiz == None):
            return 0
        
        alt_esquerda = self.__altura(raiz.esquerda)
        alt_direita = self.__altura(raiz.direita)
        if (alt_esquerda > alt_direita):
            return alt_esquerda + 1
        else:
            return alt_direita + 1
#---------------------------------------------------------------------
    def inserirAluno(self, aluno): # (JÁ UTILIZADO)
        novo = No(aluno)

        if (self.__raiz == None):
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while (atual != None):
                ant = atual
                if (aluno.matricula == atual.info.matricula):
                    return False  # elemento já existe

                if (aluno.matricula > atual.info.matricula):
                    atual = atual.direita
                else:
                    atual = atual.esquerda

            if (aluno.matricula > ant.info.matricula):
                ant.direita = novo
            else:
                ant.esquerda = novo

        return True

    def buscarMatricula(self,  matricula): # (JÁ UTILIZADO)
        if self.__raiz is None:
            return None  # Árvore vazia

        matricula = int(matricula)

        atual = self.__raiz
        while atual != None:
            if matricula == atual.info.matricula:  # Comparando matrículas dos alunos
                return atual.info  # Retorna o aluno encontrado

            if matricula > atual.info.matricula:
                atual = atual.direita
            else:
                atual = atual.esquerda

        return None  # Aluno não encontrado na árvore
#---------------------------------------------------------------------            
    def removeMatricula(self, matricula): # (JÁ UTILIZADO COM __REMOVER MATRICULA E __MINVALORNO)
        if self.__raiz is None:
            return False

        matricula = int(matricula)
        self.__raiz = self.__removerMatricula(self.__raiz, matricula)
        return True

    def __removerMatricula(self, no, matricula): #OKAY
       
        if no is None:
            return None

        if matricula < no.info.matricula:
            no.esquerda = self.__removerMatricula(no.esquerda, matricula)
        elif matricula > no.info.matricula:
            no.direita = self.__removerMatricula(no.direita, matricula)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            temp = self.__minValorNo(no.direita)
            no.info = temp.info
            no.direita = self.__removerMatricula(no.direita, temp.info.matricula)

        return no

    def __minValorNo(self, no): #OKAY
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual
#---------------------------------------------------------------------
    def __emOrdem(self, raiz):
        if raiz is not None:
            self.__emOrdem(raiz.esquerda)
            print("\nNome:", raiz.info.nome)
            print("Matrícula:", raiz.info.matricula)
            print("Nota 1:", raiz.info.nota1)
            print("Nota 2:", raiz.info.nota2)
            self.__emOrdem(raiz.direita)

    def exibirTodosAlunos(self):
        if self.__raiz is None:
            print("Árvore vazia")
        else:
            self.__emOrdem(self.__raiz)
