# Questão 06:

"""
Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser MAIORES que 7.Considere
que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
"""

materia1 = float(input('Digite a primeira nota:'))
materia2 = float(input('Digite a segunda nota:'))
materia3 = float(input('Digite a terceira nota:'))


if materia1 > 7 and materia2 > 7 and materia3 > 7:
    print ('Aprovado')
else:
    print ('Reprovado')
