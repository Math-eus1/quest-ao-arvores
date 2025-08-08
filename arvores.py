class No(object):
    def __init__(self, valor, direita = None, esquerda = None):
        self.valor = valor
        self.direita = direita
        self.esquerda = esquerda

    def __str__(self):
        return f"{self.valor}"
    
    def travessia(self, visit, order):
        if order == 'pre':
            visit(self)
        if self.esquerda is not None:
            self.esquerda.travessia(visit, order)
        if order == 'in':
            visit(self)
        if self.direita is not None:
            self.direita.travessia(visit, order)
        if order == 'post':
            visit(self)

    def get(self, valor):
        if self.valor == valor:
            return self
        node = self.esquerda if valor < self.valor else self.direita
        if node is not None:
            return node.get(valor)

    def adicionar2(node, valor):
        if node is None:
            return No(valor)
        if valor < node.valor:
            node.esquerda = No.adicionar2(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = No.adicionar2(node.direita, valor)
        return node
            
numero_casos = int(input())

for casos in range(numero_casos):
    quantidade_numeros = int(input())
    numeros = list(map(int, input().split()))
    node = None
    for valor in numeros:
        node = No.adicionar2(node, valor)
    pre_ordem = []
    em_ordem = []
    pos_ordem = []

    node.travessia(visit=lambda No: pre_ordem.append(str(No.valor)), order='pre')
    node.travessia(visit=lambda No: em_ordem.append(str(No.valor)), order='in')
    node.travessia(visit=lambda No: pos_ordem.append(str(No.valor)), order='post')
    
    print(f"Case {casos+1}:")
    print("Pre.:", ' '.join(pre_ordem))
    print("In..:", ' '.join(em_ordem))
    print("Post:", ' '.join(pos_ordem))
    print("")
        


# ------------ Lógica da Questão --------------#
'''
1. Inicialmente, um input de um inteiro para ditar quantos casos 
de teste serão feitos, possivelmente, dentro de um loop (creio que 'for')

2. Cada teste terá duas duas linhas distintas.

3. A primeira dessas duas linhas, contem um input de um inteiro
para saber quantos número terá aquela árvore, referente ao caso.

4. A segunda dessas duas linhas, contém os números que compõem 
essa árvore, creio que também um input de inteiros positivos e distintos
utilizando o 'map(int, input().split())'

5. O objetivo e função principal para aresolução da questão é, 
provavelmente e unicamente a travessia, uma vez que é como 
as árvores são percorridas de distintas maneiras: pre, in, post.

6. A saída seria exatamente o resultado de cada um desses percurssos,
sendo exibido em três linhas distintas.

7. Por conclusão, creio que talvez as funções de inserção e remoção 
talvez não venham a ser de fundamental uso, somente as funções:
__init__, __str__, travessia e get; valendo a ressalva de que a 
função 'travessia' requer o funcionamento do parâmetro 'visit',
que suponho que ainda, pelo menos nas minhas anotações da função, 
não foi declarado ou especificado, fazendo-se necessária.
Com isso, irei pesquisar mais sobre o atributo visit, para a conclusão
da travessia, e em teoria, seguindo o resto da lógica com os elementos Python, 
dá para resolver a questão. 
'''