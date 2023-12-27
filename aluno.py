class Aluno:
    def __init__(self, nome, matricula, nota1, nota2):
        self.nome = nome
        int = self.matricula = matricula
        float = self.nota1 = nota1
        float = self.nota2 = nota2

    def calcularMedia(self, nota1, nota2):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def __lt__(self, other):
        return self.matricula < other.matricula

    def __eq__(self, other):
        return self.matricula == other.matricula
    
    def inserirNotas(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2