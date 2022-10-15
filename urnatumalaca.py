from funcoes import *

candidatos_lista = [('Lula', 13), ('Bolsonaro', 22), ('Ciro Gomes', 12),
('Simone Tebet', 15), ('Leonardo Péricles', 80), ('Luiz Felipe d’Avila', 30), ('Vera Lúcia', 16), 
('Sofia Manzano', 21), ('Eymael', 27), ('Soraya Thronicke', 44), ('Pablo Marçal', 90), ('Roberto Jefferson', 14)]

candidatos = dict(candidatos_lista)

votos = []

mn = 'URNA ELETRÔNICA'
end = '| Presidente Eleito 2022 |'  
tamn = len(mn) + 25

opcao = 0
vlula = []
vbolso = []
vciro = []
vsimone = []
vleo = []

while (opcao != 4):
    print('~' * tamn)
    print(mn.center(tamn-2))
    print('~' * tamn)
    print('1 - Votar (Escolha o candidato)')
    print('2 - Branco')
    print('3 - Nulo')
    print('4 - Resultado da Eleição')
    print('~' * tamn)

    opcao = int(input('Digite a opção desejada: '))
    print('~' * tamn)
    print()

    if (0 < opcao < 5):

        if (opcao == 1):
            print('Bem Vindo! Faça seu voto, basta escolher o número do candidato :)\n')

            cand = int(input('Digite o número do candidato escolhido: '))
            print()

            if (cand == 13):
                lula(candidatos, vlula)
            elif (cand == 22):
                bolsonaro(candidatos, vbolso)
            elif (cand == 12):
                ciro(candidatos, vciro)
            elif (cand == 15):
                simone(candidatos, vsimone)
            elif (cand == 80):
                leo(candidatos, vleo)
            else:
                print('*Digite um número válido')
        
        elif (opcao == 2):
            print('Voto em branco efetuado com sucesso!\n')
        elif (opcao == 3):
            print('Voto nulo efetuado com sucesso!\n')
    
    else:
        print('*Digite uma opção válida')

result(candidatos, votos, vlula, vbolso, vciro, vsimone, vleo, end, tamn)