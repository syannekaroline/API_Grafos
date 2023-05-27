
# Syanne Karoline Moreira Tavares - 202104940029 - API grafos 

class Grafo_listaAdj:

    def __init__(self, vertices, N_orientado=False):
        self.vertices = vertices
        self.N_orientado=N_orientado
        self.grafo_lista = [[] for i in range(self.vertices)] # cria a representação lista de adjacência
        # DFS
        self.pi=dict()
        self.cor = dict()
        self.d=dict()
        self.f=dict()
        self.time=0
        #bfs
        self.Fila_Q=list()

    def AddAresta(self, u, v):
        """Adiciona no grafo uma aresta ligando os vértices u e v passados por parâmetro."""

        self.grafo_lista[u-1].append(v) if self.N_orientado else self.grafo_lista[v-1].append(u)

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
    
    def DFS(self):

        for v in range(self.vertices): 
            self.pi[v+1]=None
            self.cor[v+1]="BRANCO"
        for v in range(self.vertices):
            if self.cor[v+1]=="BRANCO":
                self.dfs_visit(v+1)

        print("DSF\nTempos iniciais d[v] =",self.d)
        print("Tempos Finais f[v] =",self.f)
        print("Lista de antecessores pi[v] =",self.pi)


    def dfs_visit(self, u):
        self.cor[u] = "CINZA"
        self.time=self.time+1
        self.d[u]=self.time

        for v in self.V_Adj(u):
            if self.cor[v]=="BRANCO":
                self.pi[v]=u
                self.dfs_visit(v)
        self.cor[u]="PRETO"
        self.time=self.time+1
        self.f[u]= self.time
        
    ############ bfs
    def BFS(self,s):
       
        for u in range(self.vertices):
            if u+1 != s:
                self.cor[u+1]="BRANCO"
                self.d[u+1]=None
                self.pi[u+1]=None
            else:
                continue
        self.cor[s]="CINZA"
        self.d[s]=0
        self.pi[s]=None
        self.Fila_Q.append(s)

        while len(self.Fila_Q) != 0:
            u =self.Fila_Q[0]
            self.Fila_Q.pop(0)
            for v in self.V_Adj(u):
                if self.cor[v] =="BRANCO":
                    self.cor[v]="CINZA"
                    self.d[v] = self.d[u] +1
                    self.pi[v] = u
                    self.Fila_Q.append(v)
            self.cor[u]="PRETO"
         

        print("BSF\nTempos iniciais d[v] =",self.d)
        print("Lista de antecessores pi[v] =",self.pi)

class Grafo_MatrizAdj:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo_matriz = [[0]*self.vertices for i in range(self.vertices)] # cria a representação matriz de adjacência
        # DFS
        self.pi=dict()
        self.cor = dict()
        self.d=dict()
        self.f=dict()
        self.time=0

        #BFS
        self.Fila_Q=list()

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
    
    def DFS(self):

        for v in range(self.vertices): 
            self.pi[v+1]=None
            self.cor[v+1]="BRANCO"
        for v in range(self.vertices):
            if self.cor[v+1]=="BRANCO":
                self.dfs_visit(v+1)

        print("DSF\nTempos iniciais d[v] =",self.d)
        print("Tempos Finais f[v] =",self.f)
        print("Lista de antecessores pi[v] =",self.pi)

    def dfs_visit(self, u):
        self.cor[u] = "CINZA"
        self.time=self.time+1
        self.d[u]=self.time

        for v in self.V_Adj(u):
            if self.cor[v]=="BRANCO":
                self.pi[v]=u
                self.dfs_visit(v)
        self.cor[u]="PRETO"
        self.time=self.time+1
        self.f[u]= self.time


    ############ bfs
    def BFS(self,s):
       
        for u in range(self.vertices):
            if u+1 != s:
                self.cor[u+1]="BRANCO"
                self.d[u+1]=None
                self.pi[u+1]=None
            else:
                continue
        self.cor[s]="CINZA"
        self.d[s]=0
        self.pi[s]=None
        self.Fila_Q.append(s)

        while len(self.Fila_Q) != 0:
            u =self.Fila_Q[0]
            self.Fila_Q.pop(0)
            for v in self.V_Adj(u):
                if self.cor[v] =="BRANCO":
                    self.cor[v]="CINZA"
                    self.d[v] = self.d[u] +1
                    self.pi[v] = u
                    self.Fila_Q.append(v)
            self.cor[u]="PRETO"
         

        print("BSF\nTempos iniciais d[v] =",self.d)
        print("Lista de antecessores pi[v] =",self.pi)

g = Grafo_listaAdj(8,True)
# g.ToString()

g.AddAresta(1,2)
g.AddAresta(1,7)
g.AddAresta(1,8)
g.AddAresta(1,6)

g.AddAresta(2,1)
g.AddAresta(2,8)

g.AddAresta(3,4)
g.AddAresta(3,6)

g.AddAresta(4,5)

g.AddAresta(5,4)

g.AddAresta(6,1)
g.AddAresta(6,3)

g.AddAresta(7,1)
g.AddAresta(7,8)

g.AddAresta(8,1)
g.AddAresta(8,2)
g.AddAresta(8,7)


g.ToString()

g.DFS()
g.BFS(8)