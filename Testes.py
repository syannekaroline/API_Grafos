from Grafos_SyanneTavares import Grafo_listaAdj as GL
from Grafos_SyanneTavares import Grafo_MatrizAdj as GM


g = GL(8)
# g.ToString()

g.AddAresta(1,2)
g.AddAresta(1,7)
g.AddAresta(1,8)
g.AddAresta(1,6)

g.AddAresta(2,8)

g.AddAresta(3,4)
g.AddAresta(3,6)

g.AddAresta(4,5)

g.AddAresta(7,8)

g.ToString()

g.DFS()
g.BFS(8)
