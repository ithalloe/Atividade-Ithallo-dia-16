# coding=utf-8
#aqui acontece a criação da função e suas variaveis
def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
total_notas = 0
num_alunos = len(notas)
aprovados = []
reprovados = []
#aqui foi criadop uma estrutura para definir se o aluno foi aprovado ou reprovado, de acordo com sua nota
for aluno, nota in notas.items():
total_notas += nota
if nota >= nota_minima_aprovacao:
aprovados.append(aluno)
else:
reprovados.append(aluno)
#aqui define que a media da turma é a divisão de total notas e num alunos
media_turma = total_notas / num_alunos
return media_turma, aprovados, reprovados
#aqui é onde esta os valores para nota de cada aluno
notas = {
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}
#aqui é definido um valor para nota minima de aprovação
nota_minima_aprovacao = 70
media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)
#aqui é onde o usuario ve os resultados das media
print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")