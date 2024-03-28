print('Bem-vindo ao programa de avaliação de candidatos. Insira as notas minimas de um candidato em uma das etapas do processo - entrevista, teste teórico, teste prático e avaliação de soft skills.')
candidatos = [
    ["Candidato 1", "e3_t4_p2_s5"],
    ["Candidato 2", "e4_t3_p5_s2"],
    ["Candidato 3", "e2_t5_p3_s4"],
    ["Candidato 4", "e5_t5_p6_s8"],
    ["Candidato 5", "e7_t8_p6_s10"]
]

def buscar_candidatos(candidatos, crit_e, crit_t, crit_p, crit_s):
    candidatos_compativeis = []

    for candidato in candidatos:
        notas = [int(nota[1:]) for nota in candidato[1].split('_')]
        if (notas[0] >= crit_e and
            notas[1] >= crit_t and
            notas[2] >= crit_p and
            notas[3] >= crit_s):
            candidatos_compativeis.append(candidato[0])

    return candidatos_compativeis

crit_e = int(input("Digite a nota mínima desejada para a entrevista: "))
crit_t = int(input("Digite a nota mínima desejada para o teste teórico: "))
crit_p = int(input("Digite a nota mínima desejada para o teste prático: "))
crit_s = int(input("Digite a nota mínima desejada para a avaliação de soft skills: "))

candidatos_compativeis = buscar_candidatos(candidatos, crit_e, crit_t, crit_p, crit_s)

if candidatos_compativeis:
    print("Candidatos compatíveis com os critérios inseridos:")
    for candidato in candidatos_compativeis:
        print(candidato)
else:
    print("Nenhum candidato encontrado com os critérios inseridos.")