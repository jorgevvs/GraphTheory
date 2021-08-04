from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        vAdjacentes = []
        totalArestas = []

        for i in self.N:
            for j in self.N:
                if i != j and (j + '-' + i) not in totalArestas:
                    totalArestas.append(i + '-' + j)

        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) != 0 and self.M[i][j] != '-': 
                    for k in self.M[i][j].keys():
                        if (self.M[i][j].get(k).v1 + '-' + self.M[i][j].get(k).v2) not in vAdjacentes:
                            vAdjacentes.append(self.M[i][j].get(k).v1 + '-' + self.M[i][j].get(k).v2)

        for i in vAdjacentes:
            if i in totalArestas:
                totalArestas.remove(i)
            else:
                totalArestas.remove(i[-1] + '-' + i[0])
            
        return totalArestas

    def ha_laco(self):
        for i in range(len(self.M)):
            if len(self.M[i][i]) != 0:
                return True

        return False


    def grau(self, V=''):
        if V not in self.N:
            raise VerticeInvalidoException

        i_V = self.N.index(V)
        grau = 0

        for i in range(i_V, len(self.M)):
            if i_V == i:
                grau += len(self.M[i_V][i])*2
            else:
                grau += len(self.M[i_V][i])

        for i in range(i_V):
            grau += len(self.M[i][i_V])

        return grau

    def ha_paralelas(self):
        for i in range(len(self.M)):
             for j in range(len(self.M)):
                 if len(self.M[i][j]) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        if V not in self.N:
            raise VerticeInvalidoException

        arestas = []
    
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                    for k in self.M[i][j].keys():
                        if self.M[i][j].get(k).v1 == V or self.M[i][j].get(k).v2 == V:
                            arestas.append(self.M[i][j].get(k).rotulo)

        return arestas

    def eh_completo(self):
        if self.ha_laco():
            return False

        if self.ha_paralelas():
            return False

        totalArestas = []
        vAdjacentes = []

        for i in self.N:
            for j in self.N:
                if i != j and (j + '-' + i) not in totalArestas:
                    totalArestas.append(i + '-' + j)


        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[i][j]) != 0 and self.M[i][j] != '-': 
                    for k in self.M[i][j].keys():
                        if (self.M[i][j].get(k).v1 + '-' + self.M[i][j].get(k).v2) not in vAdjacentes:
                            vAdjacentes.append(self.M[i][j].get(k).v1 + '-' + self.M[i][j].get(k).v2)
                    
        for i in vAdjacentes:
            if i in totalArestas:
                totalArestas.remove(i)
            else:
                totalArestas.remove(i[-1] + '-' + i[0])
        
        if totalArestas == []:
            return True
        return False


        
            


