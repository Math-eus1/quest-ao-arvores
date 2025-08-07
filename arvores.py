'''numero_casos = int(input())

for cases in numero_casos:
    quantidade_numeros = int(input())'''
class No(object):
    def __init__(self, chave, valor = None, direita = None, esquerda = None):
        self.chave = chave
        self.valor = valor
        self.direita = direita
        self.esquerda = esquerda

    def __str__(self):
        return f"{self.chave}"
    
    def travessia(self, visit, order = 'pre'):
        """Percorre a árvore na ordem fornecida como parâmetro (pre, pos ou in)
       visitando os nós com a função visit() recebida como parâmetro.
        """
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

    
    def remover(self, chave): #encontrar o nó
        #se a chave(valor que eu quero) é menor, vai pra esquerda, se é maior, vai pra direita
        if chave < self.chave:
            self.esquerda = self.esquerda.remover(chave)
        if chave > self.chave:
            self.direita = self.direita.remover(chave)

        else: #chave atual é igual ao que eu quero
            if self.esquerda is None:
                return self.direita
            if self.direita is None:
                return self.esquerda
        #agora a remoção de um nó com dois filhos
            tmp = self.direita._min()
            self.chave, self.valor = tmp.chave, tmp.valor
            self.direita._remover_min()
            return self
        
    def _min(self):
        #função para encontrar o valor minimo, que seja maior do que o nó a ser apagado
        #De início, é importante considerar que a chave do nó a ser removido
        #não será apagada, ela terá seu valor substituído pela value e key 
        #de quem irá substituir
        if self.esquerda is None:
            return self
        else:
            return self.esquerda._min()

    def _remover_min(self):
        #agora sim é o processo de remoção de quem serviu para substituire teve seu valor copiado
        #por quem seria substituido
        if self.esquerda is None:
            return self.direita
        else:
            self.esquerda = self.esquerda._remover_min()
            return self

    def get(self, chave):
        if self.chave == chave:
            return self
        node = self.esquerda if chave < self.chave else self.direita
        if node is not None:
            return node.get(chave)

    def adicionar(self, node):
        if node.chave < self.chave:
            if self.esquerda is None:
                self.esquerda = node
                return node
            else:
                return self.esquerda.adicionar(node)
        else:
            if self.direita is None:
                self.direita = node
                return node
            else:
                return self.direita.adicionar(node)

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