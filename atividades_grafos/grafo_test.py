import unittest
from meu_grafo_matriz_adjacencia_nao_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

    # Grafos DFS
        self.dfs = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])
        self.dfs.adicionaAresta('1','A','B')
        self.dfs.adicionaAresta('2','A','G')
        self.dfs.adicionaAresta('3','A','J')
        self.dfs.adicionaAresta('4','K','G')
        self.dfs.adicionaAresta('5','K','J')
        self.dfs.adicionaAresta('6','J','G')
        self.dfs.adicionaAresta('7','J','I')
        self.dfs.adicionaAresta('8','I','G')
        self.dfs.adicionaAresta('9','G','H')
        self.dfs.adicionaAresta('10','H','F')
        self.dfs.adicionaAresta('11','F','B')
        self.dfs.adicionaAresta('12','G','B')
        self.dfs.adicionaAresta('13','B','C')
        self.dfs.adicionaAresta('14','C','D')
        self.dfs.adicionaAresta('15','D','E')
        self.dfs.adicionaAresta('16','B','D')
        self.dfs.adicionaAresta('17','B','E')


        # Grafo DFS A
        self.dfs_a =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.dfs_a.adicionaAresta('1','A','B')
        self.dfs_a.adicionaAresta('11','B','F')
        self.dfs_a.adicionaAresta('10','F','H')
        self.dfs_a.adicionaAresta('9','H','G')
        self.dfs_a.adicionaAresta('4','G','K')
        self.dfs_a.adicionaAresta('5','K','J')
        self.dfs_a.adicionaAresta('7','J','I')
        self.dfs_a.adicionaAresta('13','B','C')
        self.dfs_a.adicionaAresta('14','C','D')
        self.dfs_a.adicionaAresta('15','D','E')

        # Grafo DFS D
        self.dfs_d =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.dfs_d.adicionaAresta('16','D','B')
        self.dfs_d.adicionaAresta('1','B','A')
        self.dfs_d.adicionaAresta('2','A','G')
        self.dfs_d.adicionaAresta('4','G','K')
        self.dfs_d.adicionaAresta('5','K','J')
        self.dfs_d.adicionaAresta('7','J','I')
        self.dfs_d.adicionaAresta('9','G','H')
        self.dfs_d.adicionaAresta('10','H','F')
        self.dfs_d.adicionaAresta('13','B','C')
        self.dfs_d.adicionaAresta('17','B','E')

        # Grafo DFS J
        self.dfs_j =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.dfs_j.adicionaAresta('3','J','A')
        self.dfs_j.adicionaAresta('1','A','B')
        self.dfs_j.adicionaAresta('11','B','F')
        self.dfs_j.adicionaAresta('10','F','H')
        self.dfs_j.adicionaAresta('9','H','G')
        self.dfs_j.adicionaAresta('4','G','K')
        self.dfs_j.adicionaAresta('8','G','I')
        self.dfs_j.adicionaAresta('13','B','C')
        self.dfs_j.adicionaAresta('14','C','D')
        self.dfs_j.adicionaAresta('15','D','E')

        # Grafo DFS K
        self.dfs_k =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.dfs_k.adicionaAresta('4','K','G')
        self.dfs_k.adicionaAresta('2','G','A')
        self.dfs_k.adicionaAresta('1','A','B')
        self.dfs_k.adicionaAresta('11','B','F')
        self.dfs_k.adicionaAresta('10','F','H')
        self.dfs_k.adicionaAresta('13','B','C')
        self.dfs_k.adicionaAresta('14','C','D')
        self.dfs_k.adicionaAresta('15','D','E')
        self.dfs_k.adicionaAresta('3','A','J')
        self.dfs_k.adicionaAresta('7','J','I')


    # Grafos BFS
        self.bfs = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])
        self.bfs.adicionaAresta('1','A','B')
        self.bfs.adicionaAresta('2','A','G')
        self.bfs.adicionaAresta('3','A','J')
        self.bfs.adicionaAresta('4','K','G')
        self.bfs.adicionaAresta('5','K','J')
        self.bfs.adicionaAresta('6','J','G')
        self.bfs.adicionaAresta('7','J','I')
        self.bfs.adicionaAresta('8','I','G')
        self.bfs.adicionaAresta('9','G','H')
        self.bfs.adicionaAresta('10','H','F')
        self.bfs.adicionaAresta('11','F','B')
        self.bfs.adicionaAresta('12','G','B')
        self.bfs.adicionaAresta('13','B','C')
        self.bfs.adicionaAresta('14','C','D')
        self.bfs.adicionaAresta('15','D','E')
        self.bfs.adicionaAresta('16','B','D')
        self.bfs.adicionaAresta('17','B','E')

    # Grafo BFS B
        self.bfs_b =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.bfs_b.adicionaAresta('1','B','A')
        self.bfs_b.adicionaAresta('11','B','F')
        self.bfs_b.adicionaAresta('12','B','G')
        self.bfs_b.adicionaAresta('13','B','C')
        self.bfs_b.adicionaAresta('16','B','D')
        self.bfs_b.adicionaAresta('17','B','E')
        self.bfs_b.adicionaAresta('3','A','J')
        self.bfs_b.adicionaAresta('10','F','H')
        self.bfs_b.adicionaAresta('4','G','K')
        self.bfs_b.adicionaAresta('8','G','I')

    # Grafo BFS D
        self.bfs_d =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.bfs_d.adicionaAresta('14','D','C')
        self.bfs_d.adicionaAresta('15','D','E')
        self.bfs_d.adicionaAresta('16','D','B')
        self.bfs_d.adicionaAresta('1','B','A')
        self.bfs_d.adicionaAresta('11','B','F')
        self.bfs_d.adicionaAresta('12','B','G')
        self.bfs_d.adicionaAresta('3','A','J')
        self.bfs_d.adicionaAresta('10','F','H')
        self.bfs_d.adicionaAresta('4','G','K')
        self.bfs_d.adicionaAresta('8','G','I')

    # Grafo BFS E
        self.bfs_e =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.bfs_e.adicionaAresta('15','E','D')
        self.bfs_e.adicionaAresta('17','E','B')
        self.bfs_e.adicionaAresta('14','D','C')
        self.bfs_e.adicionaAresta('1','B','A')
        self.bfs_e.adicionaAresta('11','B','F')
        self.bfs_e.adicionaAresta('12','B','G')
        self.bfs_e.adicionaAresta('3','A','J')
        self.bfs_e.adicionaAresta('10','F','H')
        self.bfs_e.adicionaAresta('4','G','K')
        self.bfs_e.adicionaAresta('8','G','I')

    # Grafo BFS I
        self.bfs_i =  MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K'])

        self.bfs_i.adicionaAresta('7','I','J')
        self.bfs_i.adicionaAresta('8','I','G')
        self.bfs_i.adicionaAresta('3','J','A')
        self.bfs_i.adicionaAresta('5','J','K')
        self.bfs_i.adicionaAresta('9','G','H')
        self.bfs_i.adicionaAresta('12','G','B')
        self.bfs_i.adicionaAresta('10','H','F')
        self.bfs_i.adicionaAresta('13','B','C')
        self.bfs_i.adicionaAresta('16','B','D')
        self.bfs_i.adicionaAresta('17','B','E')

    # Grafo Não Conexo A
        self.nao_conexo_a = MeuGrafo(['A','B','C','D','E','F','G','H','I','J','K','L','M'])
        
        self.nao_conexo_a.adicionaAresta('1','A','B')
        self.nao_conexo_a.adicionaAresta('2','A','G')
        self.nao_conexo_a.adicionaAresta('3','A','J')
        self.nao_conexo_a.adicionaAresta('4','K','G')
        self.nao_conexo_a.adicionaAresta('5','K','J')
        self.nao_conexo_a.adicionaAresta('6','J','G')
        self.nao_conexo_a.adicionaAresta('7','J','I')
        self.nao_conexo_a.adicionaAresta('8','I','G')
        self.nao_conexo_a.adicionaAresta('9','G','H')
        self.nao_conexo_a.adicionaAresta('10','H','F')
        self.nao_conexo_a.adicionaAresta('11','F','B')
        self.nao_conexo_a.adicionaAresta('12','G','B')
        self.nao_conexo_a.adicionaAresta('13','B','C')
        self.nao_conexo_a.adicionaAresta('14','C','D')
        self.nao_conexo_a.adicionaAresta('15','D','E')
        self.nao_conexo_a.adicionaAresta('16','B','D')
        self.nao_conexo_a.adicionaAresta('17','B','E')

    # Grafo Não Conexo B
        self.nao_conexo_b = MeuGrafo(['A','B','C','D'])
        
        self.nao_conexo_b.adicionaAresta('1','A','B')
        self.nao_conexo_b.adicionaAresta('2','B','C')
        self.nao_conexo_b.adicionaAresta('3','C','A')
        


    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.dfs.dfs('A'), self.dfs_a)
        self.assertEqual(self.dfs.dfs('D'), self.dfs_d)
        self.assertEqual(self.dfs.dfs('J'), self.dfs_j)
        self.assertEqual(self.dfs.dfs('K'), self.dfs_k)
       
    def test_bfs(self):
        self.assertEqual(self.bfs.bfs('B'), self.bfs_b)
        self.assertEqual(self.bfs.bfs('D'), self.bfs_d)
        self.assertEqual(self.bfs.bfs('E'), self.bfs_e)
        self.assertEqual(self.bfs.bfs('I'), self.bfs_i)
        
    
    def test_conexo(self):
        self.assertEqual(self.g_p_sem_paralelas.conexo(), True)
        self.assertEqual(self.g_p.conexo(), True)
        self.assertEqual(self.dfs.conexo(), True)
        self.assertEqual(self.bfs.conexo(), True)
        self.assertEqual(self.bfs_d.conexo(), True)
        self.assertEqual(self.nao_conexo_a.conexo(), False)
        self.assertEqual(self.nao_conexo_b.conexo(), False)
        self.assertEqual(self.dfs_d.conexo(), True)
        self.assertEqual(self.dfs_a.conexo(), True)
        self.assertEqual(self.dfs_k.conexo(), True)

    def test_caminho(self):
        self.assertEqual(self.nao_conexo_b.caminho(3), ['A', '1' , 'B', '2', 'C', '3', 'A'])
        self.assertEqual(self.nao_conexo_b.caminho(2), ['A', '1' , 'B', '2', 'C'])
        self.assertEqual(self.bfs.bfs('J').caminho(4), ['K', '5', 'J', '3', 'A', '1', 'B', '11', 'F'])
        self.assertEqual(self.g_p.caminho(3), ['Z', 'a9', 'T', 'a6', 'C', 'a2', 'E'])
        self.assertEqual(self.g_p_sem_paralelas.caminho(3), ['Z', 'a7', 'T', 'a4', 'C', 'a2', 'E'])