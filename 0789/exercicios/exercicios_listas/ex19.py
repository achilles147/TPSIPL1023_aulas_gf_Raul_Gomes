"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a
percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.

"""
so = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outro": 0
}
count = 0
while True:
    try:
        num = int(input("Qual o melhor Sistema Operacional para uso em servidores? "))
        if num == 0:
            break
        while num > 6 or num < 0:
            num = int(input("Erro. Tente denovo: "))
        voto = list(so.keys())[num - 1]
        if voto in so:
            count += 1
            so[voto] += 1
    except ValueError:
        continue

top = sorted(so.items(), key=lambda item: item[1], reverse=True)
os_nome1 = top[0]
os_nome2 = top[1]
os_nome3 = top[2]
os_nome4 = top[3]
os_nome5 = top[4]
os_nome6 = top[5]
percentagem1 = (os_nome1[1] / count) * 100
percentagem2 = (os_nome2[1] / count) * 100
percentagem3 = (os_nome3[1] / count) * 100
percentagem4 = (os_nome4[1] / count) * 100
percentagem5 = (os_nome5[1] / count) * 100
percentagem6 = (os_nome6[1] / count) * 100
somavotos = os_nome1[1] + os_nome2[1] + os_nome3[1] + os_nome4[1] + os_nome5[1] + os_nome6[1]
print(f"""
Sistema Operacional     Votos   %
-------------------     -----   ---
{os_nome1[0]}  {os_nome1[1]:>9}     {percentagem1:>7.2f}% 
{os_nome2[0]}  {os_nome2[1]:>19}    {percentagem2:>8.2f}%
{os_nome3[0]}  {os_nome3[1]:>18}    {percentagem3:>8.2f}%
{os_nome4[0]}  {os_nome4[1]:>16}    {percentagem4:>8.2f}%
{os_nome5[0]}  {os_nome5[1]:>17}    {percentagem5:>8.2f}%
{os_nome6[0]}  {os_nome6[1]:>18}    {percentagem6:>8.2f}%
---------------------------------------------------------
Total                   {somavotos}  

O Sistema Operacional mais votado foi o {os_nome1[0]}, com {os_nome1[1]} votos, correspondendo a {percentagem1:.2f}% dos votos.
""")