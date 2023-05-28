
# Syanne Karoline Moreira Tavares - 202104940029 - API grafos

"""
Classes:

Grafo_listaAdj
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
Inicialize_Single_Source -> Inicializa os vetores de distâncias e antecessores para o algoritmo Dijkstra.
Relax(u,v,w) -> Função que realiza o relaxamento de um vértice u até v com peso w.

Dijkstra(s) -> Função que realiza o algoritmo de dijkstra iniciado pelo vértice s recebido por parâmetro.\n
                Retorno:\n
                lista  conjunto S de vértices, onde para todo v ∈ S, temos d[v] = δ(s, v).\n
                dicionário pi com os antecessores de cada vértice\n
                dicionário d com distâncias mínimas de s até cada vértice.
"""

import math

class Grafo_listaAdj:

    def __init__(self, vertices, N_orientado=True, Ponderado=False):
        self.vertices = vertices
        self.N_orientado = N_orientado
        self.Ponderado = Ponderado
        self.Q_prioridades = dict()  # usado no Dijkstra


        # cria a representação lista de adjacência
        self.grafo_lista = [[] for i in range(self.vertices)]
        # DFS
        self.pi = dict()
        self.cor = dict()
        self.d = dict()
        self.f = dict()
        self.time = 0
        # bfs
        self.Fila_Q = list()

    def AddAresta(self, u, v, w=None):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro. Caso seja ponderado recebe o peso w."""

        if self.Ponderado:
            self.grafo_lista[u-1].append({v: w})
            if self.N_orientado:
                self.grafo_lista[v-1].append({u: w})
        else:
            self.grafo_lista[u-1].append(v)
            if self.N_orientado:
                self.grafo_lista[v-1].append(u)

    def ToString(self):
        """Mostra a representação do grafo matriz de adjacencia."""

        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo_lista[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def V(self):
        """Retorna o número de Vértices do Grafo."""
        return self.vertices

    def A(self):
        """Retorna o número de Arestas do grafo"""
        n_arestas = 0

        # Contagem na lista de adjacencia
        for i in range(self.vertices):
            print(self.grafo_lista[i])
            n_arestas += len(self.grafo_lista[i])

        return n_arestas/2

    def V_Adj(self, v):
        """Retorna os vértices adjacentes a v."""
        # verificação na lista de adjacencia
        if self.Ponderado:
            vAdj = list()
            for i in self.grafo_lista[v-1]:
                vAdj.append(list(i.keys())[0])
            return vAdj
        return self.grafo_lista[v-1]

    def DFS(self):

        """Realiza o algoritmo DFS do grafo mostrando os vetores de distâncias e antecessores de cada vértice"""
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
        """Método auxiliar do Algoritmo DFS. Atualiza as informações do vetor alcançado"""
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
        """Realiza o algoritmo BFS do grafo mostrando os vetores de distâncias e antecessores de cada vértice."""
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
        """Inicializa os vetores de distâncias e antecessores para o algoritmo Dijkstra."""
        for i in range(self.vertices):
            self.d[i+1] = math.inf
            self.pi[i+1] = None
        self.d[s] = 0

    def Relax(self, u, v, w):
        """Função que realiza o relaxamento de um vértice u até v com peso w."""

        if self.d[v] > self.d[u] + w:
            self.d[v] = self.d[u] + w
            self.pi[v] = u
            self.Q_prioridades[v]=w + self.d[u]

    def Dijkstra(self, s):
        """Função que realiza o algoritmo de dijkstra iniciado pelo vértice s recebido por parâmetro.\n
        Retorno:\n
        lista  conjunto S de vértices, onde para todo v ∈ S, temos d[v] = δ(s, v).\n
        dicionário pi com os antecessores de cada vértice\n
        dicionário d com distâncias mínimas de s até cada vértice."""

        if not self.Ponderado:
            print("Dijkstra não é implementado para grafos não Ponderados!")
        else:
            S_list=list()
            self.Inicialize_Single_Source(s)
            self.Q_prioridades[s]=0

            while len(self.Q_prioridades) > 0:
                #ExtractMin -> v
                v = [key for key in self.Q_prioridades if self.Q_prioridades[key] == min(self.Q_prioridades.values()) ][0]
                S_list.append(v)
                del self.Q_prioridades[v]

                for i in range(len(self.V_Adj(v))):

                    self.Relax(v,list(self.grafo_lista[v-1][i].keys())[0],list(self.grafo_lista[v-1][i].values())[0])

            return S_list,self.pi,self.d


class Grafo_MatrizAdj:

    def __init__(self, vertices, N_orientado=True, Ponderado=False):
        self.vertices = vertices
        self.N_orientado = N_orientado
        self.Ponderado = Ponderado

        self.Q_prioridades=dict()
        if Ponderado:

            self.grafo_ponderado = [
                [0]*self.vertices for i in range(self.vertices)]

        # cria a representação matriz de adjacência
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)]

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
        if self.N_orientado:
            # (caso o grafo não seja direcionado)
            self.grafo_matriz[v-1][u-1] = 1

        if self.Ponderado:
            self.grafo_ponderado[v-1][u-1] = w
            if self.N_orientado:
                self.grafo_ponderado[u-1][v-1] = w

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
            self.Q_prioridades[v]=w + self.d[u]

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
            S_list=list()
            self.Q_prioridades[s]=0

            while len(self.Q_prioridades) > 0:
                #extract min -> v
                v = [key for key in self.Q_prioridades if self.Q_prioridades[key] == min(self.Q_prioridades.values()) ][0]
                S_list.append(v)
                del self.Q_prioridades[v]
                for i in self.V_Adj(v):
                    self.Relax(v,i,self.grafo_ponderado[v-1][i-1])

            return S_list,self.pi,self.d

#Exemplo Dijkstra

# g = Grafo_MatrizAdj(7, Ponderado=True)


# g.AddAresta(1, 2, 5)
# g.AddAresta(1, 3, 6)
# g.AddAresta(1, 4, 10)
# g.AddAresta(2, 5, 13)
# g.AddAresta(3, 4, 3)
# g.AddAresta(3, 5, 11)
# g.AddAresta(3, 6, 6)
# g.AddAresta(4, 5, 6)
# g.AddAresta(4, 6, 4)
# g.AddAresta(5, 7, 3)
# g.AddAresta(6, 7, 8)

# g.ToString()

# print(g.Dijkstra(1))

