from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        nao_adjacentes = []

        for i in self.N:
            adjacentes = []

            for j in self.A:
                v1 = self.A[j].v1
                v2 = self.A[j].v2
                if v1 == i:
                    adjacentes.append(v2)
                elif v2 == i:
                    adjacentes.append(v1)
            
            for k in self.N:
                if k != i and k not in adjacentes:
                    aresta1 = f'{i}-{k}'
                    aresta2 = f'{k}-{i}'
                    if aresta1 not in nao_adjacentes and aresta2 not in nao_adjacentes:
                        nao_adjacentes.append(f'{i}-{k}')

            adjacentes = []

        return nao_adjacentes

    def ha_laco(self):
        for i in self.A:
            if self.A[i].v1 == self.A[i].v2:
                return  True
        return False

    def grau(self, V=''):
        grau = 0
        verticeExiste = False
        for i in self.N:
            if i == V:
                verticeExiste = True

        for i in self.A:
            if self.A[i].v2 == V:
                grau += 1
            if self.A[i].v1 == V:
                grau += 1

        if verticeExiste == False and grau == 0:
            raise VerticeInvalidoException("Não existe um vértice" , V, " neste self.")
        return grau


    def ha_paralelas(self):
        for i in self.A:
            paralela = 0
            for j in self.A:
                if (self.A[i].v1 + self.A[i].v2) == (self.A[j].v1 + self.A[j].v2):
                    paralela += 1
                    if paralela >= 2:
                        return True

        return False


    def arestas_sobre_vertice(self, V):
        arestas = []
        ha_vertice = False

        for i in self.N:
            if i == V:
                ha_vertice = True

        if not ha_vertice:
            raise VerticeInvalidoException("Não existe um vértice" , V, " neste grafo.")

        for i in self.A:
            if self.A[i].v1 == V or self.A[i].v2 == V:
                arestas.append(self.A[i].rotulo)

        print(arestas ,"oi")
        return arestas

    def eh_completo(self):
        
        if self.ha_laco():
            return False

        if self.ha_paralelas():
            return False

        numV = len(self.N)

        for i in self.N:
            grau = self.grau(i)

            if grau != numV - 1:
                return False 
        return True

    def vertices_adjacentes(self):
        '''
        Função que devolve uma lista com os vértices adjacentes no seguinte formato: ['V-A-V'] V = Vértice A = Aresta
        '''
        adjacentes = []

        for v in self.N:
            for a in self.A:
                if self.A[a].v2 == v and ( not adjacentes.count(f'{self.A[a].v1}-{self.A[a].rotulo}-{v}') and not adjacentes.count(f'{v}-{self.A[a].rotulo}-{self.A[a].v1}')) :
                    adjacentes.append(f'{self.A[a].v1}-{self.A[a].rotulo}-{v}')

                elif self.A[a].v1 == v and ( not adjacentes.count(f'{self.A[a].v2}-{self.A[a].rotulo}-{v}') and  not adjacentes.count(f'{v}-{self.A[a].rotulo}-{self.A[a].v2}')):
                    adjacentes.append(f'{v}-{self.A[a].rotulo}-{self.A[a].v2}')

        return adjacentes


    def dfsRecursive(self, V, dfs, percorrido, adjacentes):
        '''
        Função recursiva para passar em todos vertices adjacentes do vértice atual e verificar
        se ele ja foi percorrido ou não, adicionando ou não uma nova aresta ao grafo dfs.
        '''
        percorrido.append(V)

        vAdjacentes = []
        for i in adjacentes:
            if i.split('-')[0] == V:
                vAdjacentes.append(i)
            elif i.split('-')[-1] == V:
                if len(i) > 5:
                    vAdjacentes.append((i.split('-')[-1] + '-' + i.split('-')[1] + '-' + i.split('-')[0]))
                else:
                    vAdjacentes.append((i.split('-')[-1],'-',i.split('-')[1], '-', i.split('-')[0]))

        for a in vAdjacentes:
            if len(a) > 5:
                if a[-1] not in percorrido:
                    dfs.adicionaAresta(str(a[2] + a[3]),a[0],a[-1])
                    self.dfsRecursive( a[-1],dfs,percorrido,adjacentes) 
            else:
                if a[-1] not in percorrido:
                    dfs.adicionaAresta(str(a[2]),a[0],a[-1])
                    self.dfsRecursive( a[-1],dfs,percorrido,adjacentes) 
        


    def dfs(self, V=''):
        verticeExiste = False
        for i in self.N:
            if i == V:
                verticeExiste = True

        if verticeExiste == False:
                raise VerticeInvalidoException("Não existe um vértice" , V, " neste grafo.")

        adjacentes = self.vertices_adjacentes()
        percorrido = []

        dfs = MeuGrafo(self.N[::])

        self.dfsRecursive(V, dfs, percorrido, adjacentes)

        return dfs

    def bfs(self, V=''):
        verticeExiste = False
        for i in self.N:
            if i == V:
                verticeExiste = True

        if verticeExiste == False:
                raise VerticeInvalidoException("Não existe um vértice" , V, " neste grafo.")

        bfs = MeuGrafo()

        verticesVisitados = [V]
        lista = [V]


        while(len(lista) != 0):

            for a in self.A:
                v1 = self.A[a].v1
                v2 = self.A[a].v2

                vertice = lista[0]

                if v1 == vertice or v2 == vertice:

                    if v1 not in bfs.N:
                        bfs.adicionaVertice(v1)
                    if v2 not in bfs.N:
                        bfs.adicionaVertice(v2)

                    vertice_adjacente = v2 if vertice == v1 else v1

                    if vertice_adjacente not in verticesVisitados:

                        lista.append(vertice_adjacente)
                        verticesVisitados.append(vertice_adjacente)
                        bfs.adicionaAresta(a, vertice, vertice_adjacente)

            lista.pop(0)
        return(bfs)
    
   

    def caminho_total(self, V=''):
        lista = []
        first = True

        vPercorrido = [V]

        for i in range(len(self.N)):
            for j in self.A:
                if self.A[j].rotulo not in lista and self.A[j].v2 == vPercorrido[0]:
                    if self.A[j].v1 == V:
                        if first:
                            lista.append(self.A[j].v1)
                            first = False
                        lista.append(self.A[j].rotulo)
                        lista.append(self.A[j].v2)
                        V = self.A[j].v2
                        vPercorrido.append(V)
                        break

                    elif self.A[j].v2 == V:
                        if first:
                            lista.append(self.A[j].v2)
                            first = False
                        lista.append(self.A[j].rotulo)
                        lista.append(self.A[j].v1)
                        V = self.A[j].v1
                        break

                if self.A[j].rotulo not in lista and (self.A[j].v2 not in lista):
                    if self.A[j].v1 == V:
                        if first:
                            lista.append(self.A[j].v1)
                            first = False
                        lista.append(self.A[j].rotulo)
                        lista.append(self.A[j].v2)
                        V = self.A[j].v2
                        vPercorrido.append(V)
                        break

                    elif self.A[j].v2 == V:
                        if first:
                            lista.append(self.A[j].v2)
                            first = False
                        lista.append(self.A[j].rotulo)
                        lista.append(self.A[j].v1)
                        V = self.A[j].v1
                        break

        return lista

    def caminho(self, n):
        '''
        Função que retorna lista com caminho de tamanho n
        :n: tamanho do caminho
        :return: lista com caminho
        '''
        lista = []
        for i in self.N:
            if len(self.caminho_total(i)) > len(lista):
                lista = self.caminho_total(i)

        if len(lista) < n*2+1:
            return ("Não existe caminho de tamanho " , n)

        return lista[0:(n*2)+1]

    def conexo(self):
        grafo_bfs = self.bfs(self.N[0])

        if len(self.N) == len(grafo_bfs.N):
            return True
        else:
            return False

    