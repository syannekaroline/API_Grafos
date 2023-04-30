

"""
API - Disponibiliza recursos e funcionalidades
1- objetivo:
    Criar uma api que Represente grafos e consulte informações sobre os grafos criados.
    Disponibilizar a representação de grafos, consulta, edição e exclusão
    2. representações computaciona de Grafos por meio de Listas de Adjacências e Matrizes de Adjacências.
     a) V() retorna o número de vértices; 
     b) A() retorna o número de arestas; 
     c) AddArestas() - Adiciona arestas; 
     d) Adj() retorna arestas adjacentes.

2. url base
    localhost
4. endpoints

5. Quais recursos
"""


class Grafo:

    def __init__(self, vertices): #, direcionado=False
        self.vertices = vertices
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)] # cria a representação matriz de adjacência
        self.grafo_lista = [[] for i in range(self.vertices)] # cria a representação lista de adjacência
        # self.direcionado = direcionado
        # self.ArestasList=[]

    def AddAresta(self, u, v):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro."""

        #adiciona na lista de arestas
        # self.ArestasList.append((u,v))

        # if self.direcionado:
        #     # grafos direcionados simples
        self.grafo_matriz[u-1][v-1] = 1  # trocar = por += ser for grafo múltiplo
        self.grafo_lista[u-1].append(v)
        # else:
        # (caso o grafo não seja direcionado)
        self.grafo_matriz[v-1][u-1] = 1 
        self.grafo_lista[v-1].append(u)
        # self.ArestasList.append((v,u))

        
    def mostra_lista(self):
        """Mostra a representação do grafo matriz de adjacencia."""


        for i in range(self.vertices):
            print(f'{i+1}:', end='  ')
            for j in self.grafo_lista[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def mostra_matriz(self):
        """Mostra a representação do grafo em lista de adjacência"""
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo_matriz[i])

    def V(self):
        """Retorna o número de Vértices do Grafo"""
        return self.vertices

### Plus - não solicitado
    # def ArestasList(self):
    #     """"Retorna a lista do conjunto de Arestas"""
    #     return self.ArestasList
    
####################### 

    def A(self):
        """Retorna o número de Arestas do grafo"""
        n_arestas=0

        ## contagem na matriz de adjacencia 
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo_matriz[i][j] == 1:
                    n_arestas+=1
        
        # ## Contagem na lista de adjacencia
        # for i in range(self.vertices):
        #     n_arestas+=len(self.grafo_lista[i])

        return n_arestas/2



    def V_Adj(self,v):
        """Retorna os vértices adjacentes a v."""

        # arestas adjacentes são aquelas que compartilham de um mesmo vértices

        ##verificação na lista de adjacencia
        return self.grafo_lista[v-1]
    

    # def Arestas_Adj(self,a):
    #     """Retorna as Arestas adjacentes."""

    #     # arestas adjacentes são aquelas que compartilham de um mesmo vértices

    #     adjacentes = dict()

    #     for a in self.ArestasList:
    #         adjacentes[f"Adjacentes a {a}"]=[]

    #         for b in self.ArestasList:
    #             if a[0] == b[1] or a[1] == b[0]:
    #                 adjacentes[f"Adjacentes a {a}"].append(b)

    #     return adjacentes

g = Grafo(4)
# g.mostra_matriz()

g.AddAresta(1,2)
g.AddAresta(1,3)
g.AddAresta(1,4)
g.AddAresta(2,3)

g.mostra_matriz()
n_vertices = g.V()
print(f"Número de vértices = {n_vertices}")
n_Arestas = g.A()
print(f"Número de Arestas = {n_Arestas}")
# Arestas = g.ArestasList
# print(f"Conjunto de Arestas = {Arestas}")

print(f"Vértices adjacentes a 1: {g.V_Adj(1)}")
print(f"Vértices adjacentes a 2: {g.V_Adj(2)}")

g.mostra_lista()