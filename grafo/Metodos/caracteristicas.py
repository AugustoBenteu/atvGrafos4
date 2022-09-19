'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

from re import T
import numpy as np

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

def criaListaAdjacencias(matriz):
    lista = ''
    aux= 0
    for i in range(np.shape(matriz)[0]):
        lista += '\nv'+ str(i)
        for j in range(np.shape(matriz)[1]) :
            if matriz[i][j] != 0:
                while aux < matriz[i][j]:
                    lista += "->v"+ str(j)
                    aux += 1
                aux = 0
    print(lista)
                

def tipoGrafo(matriz):
    tipo = 0;
    for i in range(np.shape(matriz)[0]):
        if matriz[i][i] == 1:
            tipo = 3;
            return tipo #Checando se existe algum laço atraves da diagonal se tiver ->peudografo
        for j in range(np.shape(matriz)[1]) :
            if matriz[i][j] > 1 and tipo != 1:
                tipo =  2 #Se qualquer adjacencia possuir mais de uma aresta -> Multigrafo
            if matriz[i][j] != matriz[j][i] :
                tipo = 1 #Se existir algum ponto na matriz que seu oposto não seja igual ela é um digrafo

    return tipo #Se não possui laço, não possui arestas paralelas e todos os pontos opostos são iguais Grafo simples.
    
    
def calcDensidade(matriz):
    if tipoGrafo(matriz) == 0 :
        qtdVert = np.shape(matriz)[0]
        qtdAres = 0
        for i in range(np.shape(matriz)[0]):
            for j in range(np.shape(matriz)[1]):
                if (matriz[i][j] != 0):
                    qtdAres += matriz[i][j]
                
        dens = (qtdAres ) / (qtdVert *(qtdVert-1))
        print('densidade = ', dens)
    else:
        qtdVert = np.shape(matriz)[0]
        qtdAres = 0
        for i in range(np.shape(matriz)[0]):
            for j in range(np.shape(matriz)[1]):
                if (matriz[i][j] != 0):
                    qtdAres += matriz[i][j]
                
        dens = (qtdAres/2 ) / (qtdVert *(qtdVert-1))
        print('densidade = ', dens)

def insereAresta(matriz,vi,vj):
    if tipoGrafo(matriz) == 1 :
        matriz[vi][vj] += 1
    else :
        matriz[vi][vj] += 1
        matriz[vj][vi] += 1
    return matriz

def removeAresta(matriz,vi,vj):
    if tipoGrafo(matriz) == 1 :
        if matriz[vi][vj] != 0:
            matriz[vi][vj] -= 1
        else:
            print("Essa aresta já não existe")
    else :
        if matriz[vi][vj] != 0:
            matriz[vi][vj] -= 1
            matriz[vj][vi] -= 1
        else:
            print("Essa aresta já não existe")
    return matriz
    
def insereVertice(matriz,vi):
    matriz = np.hstack((matriz,np.zeros((matriz.shape[1],1), dtype=matriz.dtype  )))
    matriz = np.vstack((matriz,np.zeros((1,(matriz.shape[0])+1), dtype=matriz.dtype  )))
    return matriz 
    

    

def removeVertice(matriz,vi):
    pass 
