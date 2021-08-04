from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.aresta import *


grafo = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

grafo.adicionaAresta('1','A','B') 
grafo.adicionaAresta('2','A','G')
grafo.adicionaAresta('3','A','J')
grafo.adicionaAresta('4','K','G')
grafo.adicionaAresta('5','K','J')
grafo.adicionaAresta('6','J','G')
grafo.adicionaAresta('7','J','I')
grafo.adicionaAresta('8','I','G')
grafo.adicionaAresta('9','G','H')
grafo.adicionaAresta('10','H','F')
grafo.adicionaAresta('11','F','B')
grafo.adicionaAresta('12','G','B')
grafo.adicionaAresta('13','B','C')
grafo.adicionaAresta('14','C','D')
grafo.adicionaAresta('15','D','E')
grafo.adicionaAresta('16','B','D')
grafo.adicionaAresta('17','B','E')
grafo.adicionaAresta('18','B','E')

grafo2 = MeuGrafo(['A','B','C'])
grafo2.adicionaAresta('1','A','B')
grafo2.adicionaAresta('2','A','C')
grafo2.adicionaAresta('3','B','C')

print(grafo2.eh_completo())
