"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.

Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
telefonistas, para a computação dos votos.

Sua equipe foi contratada para
desenvolver este programa, utilizando a linguagem de programação C++.

Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.

Um número de jogador igual zero, indica que a votação foi encerrada.

Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de
aviso, e voltando a pedir outro número.

Após o final da votação, o programa deverá exibir:

O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente
com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos.
 O resultado aparece ordenado pelo número do jogador. O programa deve
 fazer uso de arrays.
 O programa deverá executar o cálculo do percentual
 de cada jogador através de uma função.
 Esta função receberá dois parâmetros:
 o número de votos de um jogador e o total de votos.
 A função calculará o percentual e retornará o valor calculado.
 Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais
 próxima possível ao exemplo. Os dados são fictícios e
 podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar
  os dados referentes ao resultado da votação em um arquivo texto no disco,
  obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""
jogadores = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
             6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
             11: 0, 12: 0, 13: 0, 14: 0, 15: 0,
             16: 0, 17: 0, 18: 0, 19: 0, 20: 0,
             21: 0, 22: 0, 23: 0}
def cal_top3():
    top3 = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)[:3]
    top1jogador = top3[0]
    top2jogador = top3[1]
    top3jogador = top3[2]
    percentagem1 = (top1jogador[1] / count) * 100
    percentagem2 = (top2jogador[1] / count) * 100
    percentagem3 = (top3jogador[1] / count) * 100
    print(f"""
    Resultado da votação: 

    Foram computados {count} votos.

    Jogador---Votos---Percentagem
    {top1jogador[0]}    {top1jogador[1]}    {percentagem1:.2f}
    {top2jogador[0]}    {top2jogador[1]}    {percentagem2:.2f}
    {top3jogador[0]}    {top3jogador[1]}    {percentagem3:.2f}

    O melhor jogador foi o {top1jogador[0]} com {top1jogador[1]} votos, correspondendo a {percentagem1:.2f}% dos votos.
    """)
count = 0
while True:
    while True:
        try:
            num = int(input("Número do jogador (0=fim): "))
            break
        except ValueError:
            continue
    while num < 0 or num > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        num = int(input("Número do jogador (0=fim): "))
    if num == 0:
        break
    else:
        count += 1
        jogadores[num] += 1
cal_top3()





