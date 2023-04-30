
# Syanne Karoline Moreira Tavares - 202104940029 - API grafos 

class Grafo_listaAdj:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo_lista = [[] for i in range(self.vertices)] # cria a representação lista de adjacência

    def AddAresta(self, u, v):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro."""

        self.grafo_lista[u-1].append(v)
        self.grafo_lista[v-1].append(u)
        
    def ToString(self):
        """Mostra a representação do grafo matriz de adjacencia."""

        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo_lista[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def V(self):
        """Retorna o número de Vértices do Grafo"""
        return self.vertices

    def A(self):
        """Retorna o número de Arestas do grafo"""
        n_arestas=0

        ## Contagem na lista de adjacencia
        for i in range(self.vertices):
            n_arestas+=len(self.grafo_lista[i])

        return n_arestas/2

    def V_Adj(self,v):
        """Retorna os vértices adjacentes a v."""
        ##verificação na lista de adjacencia
        return self.grafo_lista[v-1]

class Grafo_MatrizAdj:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)] # cria a representação matriz de adjacência

    def AddAresta(self, u, v):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro."""
        self.grafo_matriz[u-1][v-1] = 1  # trocar = por += ser for grafo múltiplo
        # (caso o grafo não seja direcionado)
        self.grafo_matriz[v-1][u-1] = 1 
      

    def ToString(self):
        """Mostra a representação do grafo em matriz de adjacência"""
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo_matriz[i])

    def V(self):
        """Retorna o número de Vértices do Grafo"""
        return self.vertices

    def A(self):
        """Retorna o número de Arestas do grafo"""
        n_arestas=0

        ## contagem na matriz de adjacencia 
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo_matriz[i][j] == 1:
                    n_arestas+=1

        return n_arestas/2



    def V_Adj(self,v):
        """Retorna os vértices adjacentes a v."""

        vAdj = list()

        for i,j in enumerate(self.grafo_matriz[v-1]):
            if j ==1 and i != v-1:
                vAdj.append(i+1)

        return vAdj

# g = Grafo_MatrizAdj(4)
# # g.ToString()

# g.AddAresta(1,2)
# g.AddAresta(1,3)
# g.AddAresta(1,4)
# g.AddAresta(2,3)

# g.ToString()
# n_vertices = g.V()
# print(f"Número de vértices = {n_vertices}")
# n_Arestas = g.A()
# print(f"Número de Arestas = {n_Arestas}")
# # Arestas = g.ArestasList
# # print(f"Conjunto de Arestas = {Arestas}")

# print(f"Vértices adjacentes a 1: {g.V_Adj(1)}")
# print(f"Vértices adjacentes a 2: {g.V_Adj(2)}")