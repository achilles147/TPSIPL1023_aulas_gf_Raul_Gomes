class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
class ArvoreBinaria:
    def __init__(self):
        self.root = None

    def adicionar(self,valor):
        if self.root is None:
            self.root = Node(valor)
        else:
            self.adicionar_recursivo(self.root, valor)
        print("Node "+ str(valor) +" adicionado com sucesso")

    def adicionar_recursivo(self, node, valor):
        if valor < node.valor:
            if node.esquerda is None:
                node.esquerda = Node(valor)
            else:
                self.adicionar_recursivo(node.esquerda, valor)
        else:
            if node.direita is None:
                node.direita = Node(valor)
            else:
                self.adicionar_recursivo(node.direita, valor)


arvore = ArvoreBinaria()
arvore.adicionar(5)