
# Syanne Karoline Moreira Tavares - 202104940029 - API grafos

"""
Classe:

Grafo_MatrizAdj

"""
# Endpoints/ métodos:
"""
AddAresta(u,v) -> Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro. Caso seja ponderado recebe o peso w.

ToString -> Mostra a representação do grafo matriz de adjacencia.

V -> Retorna o número de Vértices do Grafo.

A-> Retorna o número de Arestas do grafo.

V_Adj -> Retorna os vértices adjacentes a v.

DFS -> Realiza o algoritmo DFS do grafo mostrando os vetores de distâncias e antecessores de cada vértice.

dfs_visit ->Método auxiliar do Algoritmo DFS. Atualiza as informações do vetor.

BFS -> Realiza o algoritmo BFS do grafo mostrando os vetores de distâncias e antecessores de cada vértice.

Inicialize_Single_Source -> Inicializa os vetores de distâncias e antecessores para o algoritmo Dijkstra

Relax(u,v,w) -> Função que realiza o relaxamento de um vértice u até v com peso w.

Dijkstra(s) -> Função que realiza o algoritmo de dijkstra iniciado pelo vértice s recebido por parâmetro.
                Retorno:\n
                lista  conjunto S de vértices, onde para todo v ∈ S, temos d[v] = δ(s, v).
                dicionário pi com os antecessores de cada vértice
                dicionário d com distâncias mínimas de s até cada vértice.

Belman_ford(s) ->  Realiza o aloritmo de Bellman-ford.
                    Retorno:
                    retorna o valor boleano indicando se foi ou não encontrado ciclo negativo.
                    Caso não tenha ciclo negativo retorna uma tupla com respectivos valores:
                    valor boleano indicando se foi ou não encontrado ciclo negativo.
                    dict d -> dicionário com os caminhos mínimos de s até cada vértice.
                    dict pi -> dicionário com os antecessores de cada vértice.

Floyd_Warshall -> Realiza o algoritmo de floyd-Warshall
                    Retorno:
                    FW_matriz = Matriz de caminhos mínimos entre todos os pares de vértice.
                    self.pi = dicionários com antecessores de cada vértice.
Encontrar_Componentes_Conectados- > Algoritmos pra encontrar os componentes conectados com auxilio do BFS adaptado.\n
                                Retorna um dicionário onde a chave é o id do componente e o valor são com componentes conectados.

FechoTransitivo_Warshall-> Método que aplica o Alg. de Warshall para retornar o Fecho Transitivo                                             
"""




import math
import numpy as np

class Grafo_MatrizAdj:

    def __init__(self, vertices, N_orientado=True, Ponderado=False):

        # Número de vértices
        self.vertices = vertices
        self.N_orientado = N_orientado
        self.Ponderado = Ponderado

        self.Q_prioridades = dict()
        if Ponderado:

            self.grafo_ponderado = [
                [0]*self.vertices for i in range(self.vertices)]

        # cria a representação matriz de adjacência
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)]
        self.grafo_boleano = [
            [False]*self.vertices for i in range(self.vertices)]

        # DFS
        self.pi = dict()
        self.cor = dict()
        self.d = dict()
        self.f = dict()
        self.time = 0

        # BFS
        self.Fila_Q = list()

    def AddAresta(self, u, v, w=None):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro. Se for pondera w é o peso entre os vértices"""

        # trocar = por += ser for grafo múltiplo
        self.grafo_matriz[u-1][v-1] = 1
        self.grafo_boleano[u-1][v-1] = True
        if self.N_orientado:
            # (caso o grafo não seja direcionado)
            self.grafo_matriz[v-1][u-1] = 1
            self.grafo_boleano[u-1][v-1] = True

        if self.Ponderado:
            self.grafo_ponderado[u-1][v-1] = w
            if self.N_orientado:
                self.grafo_ponderado[v-1][u-1] = w

    def ToString(self):
        """Mostra a representação do grafo em matriz de adjacência"""
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo_matriz[i])

        if self.Ponderado:
            print('A matriz do grafo ponderado:')
            for i in range(self.vertices):
                print(self.grafo_ponderado[i])

    def V(self):
        """Retorna o número de Vértices do Grafo"""
        return self.vertices

    def A(self):
        """Retorna o número de Arestas do grafo"""
        n_arestas = 0

        # contagem na matriz de adjacencia
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo_matriz[i][j] == 1:
                    n_arestas += 1

        return n_arestas/2

    def V_Adj(self, v):
        """Retorna os vértices adjacentes a v."""

        vAdj = list()

        for i, j in enumerate(self.grafo_matriz[v-1]):
            if j == 1 and i != v-1:
                vAdj.append(i+1)

        return vAdj

    def DFS(self):
        """Realiza o algoritmo DFS do grafo mostrando os vetores de distâncias e antecessores de cada vértice."""
        for v in range(self.vertices):
            self.pi[v+1] = None
            self.cor[v+1] = "BRANCO"
        for v in range(self.vertices):
            if self.cor[v+1] == "BRANCO":
                self.dfs_visit(v+1)

        print("DSF\nTempos iniciais d[v] =", self.d)
        print("Tempos Finais f[v] =", self.f)
        print("Lista de antecessores pi[v] =", self.pi)

    def dfs_visit(self, u):
        """Método auxiliar do Algoritmo DFS. Atualiza as informações do vetor."""

        self.cor[u] = "CINZA"
        self.time = self.time+1
        self.d[u] = self.time

        for v in self.V_Adj(u):
            if self.cor[v] == "BRANCO":
                self.pi[v] = u
                self.dfs_visit(v)
        self.cor[u] = "PRETO"
        self.time = self.time+1
        self.f[u] = self.time

    # bfs
    def BFS(self, s):
        """Realiza o algoritmo BFS do grafo mostrando os vetores de distâncias e antecessores."""
        for u in range(self.vertices):
            if u+1 != s:
                self.cor[u+1] = "BRANCO"
                self.d[u+1] = None
                self.pi[u+1] = None
            else:
                continue
        self.cor[s] = "CINZA"
        self.d[s] = 0
        self.pi[s] = None
        self.Fila_Q.append(s)

        while len(self.Fila_Q) != 0:
            u = self.Fila_Q[0]
            self.Fila_Q.pop(0)
            for v in self.V_Adj(u):
                if self.cor[v] == "BRANCO":
                    self.cor[v] = "CINZA"
                    self.d[v] = self.d[u] + 1
                    self.pi[v] = u
                    self.Fila_Q.append(v)
            self.cor[u] = "PRETO"

        print("BSF\nTempos iniciais d[v] =", self.d)
        print("Lista de antecessores pi[v] =", self.pi)

    ############################## Algoritmos caminhos mínimos###################################

    def Inicialize_Single_Source(self, s):
        """Função que inicializa as variáveis auxiliares na execução do algoritmo de caminhos mínimo."""
        for i in range(self.vertices):
            self.d[i+1] = math.inf
            self.pi[i+1] = None
        self.d[s] = 0

    def Relax(self, u, v, w):
        """Função que realiza o relaxamento de um vértice u até v com peso w."""

        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.pi[v] = u
            self.Q_prioridades[v] = w + self.d[u]

    def Dijkstra(self, s):
        """Função que realiza o algoritmo de dijkstra iniciado pelo vértice s recebido por parâmetro.\n
        Retorno:\n
        lista  conjunto S de vértices, onde para todo v ∈ S, temos d[v] = δ(s, v).\n
        dicionário pi com os antecessores de cada vértice\n
        dicionário d com distâncias mínimas de s até cada vértice."""

        if not self.Ponderado:
            print("Dijkstra não é implementado para grafos não Ponderados!")
        else:
            self.Inicialize_Single_Source(s)
            S_list = list()
            self.Q_prioridades[s] = 0

            while len(self.Q_prioridades) > 0:
                # extract min -> v
                v = [key for key in self.Q_prioridades if self.Q_prioridades[key] == min(
                    self.Q_prioridades.values())][0]
                S_list.append(v)
                del self.Q_prioridades[v]
                for i in self.V_Adj(v):
                    self.Relax(v, i, self.grafo_ponderado[v-1][i-1])

            return S_list, self.pi, self.d

    def Bellman_Ford(self, s):
        """Realiza o aloritmo de Bellman-ford.\n
        Retorno:
        retorna o valor boleano indicando se foi ou não encontrado ciclo negativo.\n
        Caso não tenha ciclo negativo retorna uma tupla com respectivos valores:\n
        valor boleano indicando se foi ou não encontrado ciclo negativo.\n
        dict d -> dicionário com os caminhos mínimos de s até cada vértice.\n
        dict pi -> dicionário com os antecessores de cada vértice."""

        self.Inicialize_Single_Source(s)

        for _ in range(1, self.vertices):
            for v in range(1, self.vertices+1):
                for i in self.V_Adj(v):

                    self.Relax(v, i, self.grafo_ponderado[v-1][i-1])

        for u in range(1, self.vertices+1):
            for v in self.V_Adj(u):
                # print(f"{self.d[v] } > {self.d[u]} + w({u},{v}-> {self.grafo_ponderado[u-1][v-1]}) ")

                if self.d[v] > self.d[u] + self.grafo_ponderado[u-1][v-1]:
                    print("Existe Ciclo Negativo!")
                    return True
        return False, self.d, self.pi

    def Floyd_Warshall(self):
        """Realiza o algoritmo de floyd-Warshall\n
        Retorno:\n
        FW_matriz = Matriz de caminhos mínimos entre todos os pares de vértice.\n
        self.pi = dicionários com antecessores de cada vértice."""

        FW_matriz = [[0]*self.vertices for i in range(self.vertices)]
        self.pi = [[None]*self.V() for i in range(self.V())]

        for v in range(1, self.vertices+1):
            for w in range(1, self.vertices+1):
                if v != w:
                    FW_matriz[v-1][w-1] = self.grafo_ponderado[v-1][w -
                                                                    1] if self.grafo_ponderado[v-1][w-1] != 0 else math.inf
                    self.pi[v-1][w-1] = v

        for k in range(self.vertices):
            for v in range(self.vertices):
                for w in range(self.vertices):
                    if FW_matriz[v][k] + FW_matriz[k][w] < FW_matriz[v][w]:
                        FW_matriz[v][w] = FW_matriz[v][k] + FW_matriz[k][w]
                        self.pi[v+1][w+1] = self.pi[k-1][w-1]

        return FW_matriz, self.pi

    def Encontrar_Componentes_conectados(self):
        """Algoritmos pra encontrar os componentes conectados com auxilio do BFS adaptado.\n
            Retorna um dicionário onde a chave é o id do componente e o valor são com componentes conectados."""

        Componentes_Conectados = dict()
        visitados = set()  # Conjunto de vertices visitados pelo DFS
        count = 0  # Contador de componentes conectados

        def DFS(vertice, componente):
            """Algoritmo DFS chamado recursivamente"""
            visitados.add(
                vertice)  # adiciona o atual vertice no conjunto dos visitados
            componente.append(vertice)
            for adj in self.V_Adj(vertice):
                if adj not in visitados:
                    DFS(adj, componente)

        for vertice in range(1, self.vertices+1):
            id_componente = count
            if vertice not in visitados:
                count += 1
                componentes = []
                DFS(vertice, componentes)
                Componentes_Conectados[id_componente] = componentes

        return Componentes_Conectados

    def FechoTransitivo_Warshall(self):
        """ Método que aplica o Alg. de Warshall para retornar o Fecho Transitivo."""

        M_fechoTransitivo = np.array(self.grafo_boleano)

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    M_fechoTransitivo[i][j] = M_fechoTransitivo[i][j] or (M_fechoTransitivo[i][k] and M_fechoTransitivo[k][j])

        # conversão de valores boleanos
        M_fechoTransitivo= M_fechoTransitivo.tolist()

        for i in range(self.vertices):
            for j in range(self.vertices):
                M_fechoTransitivo[i][j] = int(M_fechoTransitivo[i][j] == True)
     
        return M_fechoTransitivo

# Exemplo - Encontrar componentes conectados - Matrizes de adjacência

print("{:=^60}".format("Exemplo 1 - Fecho Transitivo - Matrizes de adjacência"))

g = Grafo_MatrizAdj(5, N_orientado=False)

g.AddAresta(1, 2)
g.AddAresta(2, 3)
g.AddAresta(3, 1)
g.AddAresta(3, 4)
g.AddAresta(5, 1)
g.AddAresta(5, 3)

g.ToString()

print("\nMatriz do fecho transitivo:\n")
for i in g.FechoTransitivo_Warshall():
    print(i)
