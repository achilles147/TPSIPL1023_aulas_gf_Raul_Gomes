from dataclasses import dataclass

@dataclass
class Relacao:
    nome: str

    def __str__(self):
        return f"{Relacao.nome}"


@dataclass
class Contacto:
    nome: str
    num: int
    relacao: Relacao

    def __str__(self):
        return f"{Contacto.nome}{Contacto.num}"
def novo_contacto():
    print("\n"+"."*5+"Adicionar Contacto"+5*".")
    nome = input("Nome: ")
    nome = nome.capitalize()
    while True:
        try:
            num = int(input("Número: "))
            break
        except:
            print("Erro.")
    relacao = input("Relação com contacto: ")
    relacao = relacao.capitalize()
    relacao = Relacao(relacao)
    contacto = Contacto(nome,num, relacao)
    lista_contactos.append(contacto)
    print("=" * 10 + "Contacto adicionado!" + "=" * 10)

def remover_contacto():
    rm = input("Nome do contacto a remover: ")
    rm = rm.capitalize()
    for obj in lista_contactos:
        if obj.nome == rm:
            lista_contactos.remove(obj)
    print(f"Contacto {rm} removido.\n")

def printlista():
    print()
    temp = sorted(lista_contactos, key=lambda obj: obj.nome)
    print("=" * 10 + "Lista de Contactos" + "=" * 10)
    if len(lista_contactos) == 0:
        print("Não existem contactos")
    else:
        for contacto in temp:
            print(f"{contacto.nome}\t{contacto.relacao.nome}\t\t{contacto.num}")
    print("=" * 12 + "Fim" + "=" * 12)


lista_contactos = [Contacto(nome='andré', num=123123132, relacao=Relacao(nome='chefe')),
                   Contacto(nome='jorge', num=123122332, relacao=Relacao(nome='mano')),
                   Contacto(nome='rogério', num=121223132, relacao=Relacao(nome='colega')),
                   Contacto(nome='filipe', num=123123132, relacao=Relacao(nome='colega')),
                   Contacto(nome='maria', num=123123132, relacao=Relacao(nome='amor'))]
while True:
    opc = input("\n1. Ver lista de contactos\n2. Adicionar contacto\n3. Remover contacto\n4.Sair\nOpção: ")
    while opc != '1' and opc != '2' and opc != '3' and opc != '4':
        print("\nErro. Tente denovo.")
        opc = input("Opção: ")
    match opc:
        case '1':
            printlista()
        case '2':
            novo_contacto()
        case '3':
            printlista()
            remover_contacto()
            printlista()
        case '4':
            break

