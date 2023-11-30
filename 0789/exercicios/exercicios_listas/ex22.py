"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática,
com a intenção de fazer um levantamento nas sucatas encontradas nesta área.

A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá,
testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo:

um número de identificação do mouse
o tipo de defeito:
    necessita da esfera;
    necessita de limpeza;
    a.necessita troca do cabo ou conector;
    a.quebrado ou inutilizado
Uma identificação igual a zero encerra o programa.
Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""


defeitos = {
    'Necessita da esfera': 0,
    'Necessita de limpeza': 0,
    'Necessita troca do cabo ou conector': 0,
    'Quebrado ou inutilizado': 0
}

count = 0
while True:
    i = 1
    print("\nDefeitos: \n")
    for key, value in defeitos.items():
        print(f"{i} - {key}")
        i += 1
    esc = input("Opção: ")

    while esc != '1' and esc != '2' and esc != '3' and esc != '4' and esc != '0':
        esc = input("Erro. Tente denovo. Opção: ")
    if esc == '0':
        break
    match esc:
        case '1':
            defeitos['Necessita da esfera'] += 1
        case '2':
            defeitos['Necessita de limpeza'] += 1
        case '3':
            defeitos['Necessita troca do cabo ou conector'] += 1
        case '4':
            defeitos['Quebrado ou inutilizado'] += 1
    count += 1

defeitos_sorted = sorted(defeitos.items(), key=lambda item: item[1], reverse=True)
print(f"""
Quantidade de mouses: {count}

Situação                Quantidade          Percentagem
1- {defeitos_sorted[0][0]}\t\t\t{defeitos_sorted[0][1]}\t\t\t{(defeitos_sorted[0][1] / count) * 100:.1f}%
2- {defeitos_sorted[1][0]}\t\t\t{defeitos_sorted[0][1]}\t\t\t{(defeitos_sorted[1][1] / count) * 100:.1f}%
3- {defeitos_sorted[2][0]}\t\t\t{defeitos_sorted[0][1]}\t\t\t{(defeitos_sorted[2][1] / count) * 100:.1f}%
4- {defeitos_sorted[3][0]}\t\t\t{defeitos_sorted[0][1]}\t\t\t{(defeitos_sorted[3][1] / count) * 100:.1f}%
""")