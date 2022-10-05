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

def criaListaAdjacencias(matriz):
    lista = {}
    for i in range(np.shape(matriz)[0]):
        lista[i] = []

    for i in range(np.shape(matriz)[0]):
        for j in range(np.shape(matriz)[1]) :
            if matriz[i][j] != 0:
                for x in range(matriz[i][j]):
                    lista[i].append(j)
    print(lista)
    return lista


def verificaAdjacenciaLista(listaAdj, vi, vj):
    if vj in listaAdj[vi]:
        print("True")
        return True
    elif vi in listaAdj[vj]:
        print("True")
        return True
    else:
        print("False")
        return False

def tipoGrafoAdj(listaAdj):
    size = len(listaAdj)
    tipo = 0
    for i in range(size):
        for x in listaAdj[i]:
            if i not in listaAdj[x]:
                tipo = 1
    aux = -1
    for i in range(size):
        if i in listaAdj[i] and tipo ==1:
            tipo = 31
        elif i in listaAdj[i] and tipo ==0:
            tipo = 30
        for x in listaAdj[i]:
            
            if x == aux  and tipo ==1:
                tipo = 21
            elif x == aux and tipo ==0:
                tipo = 20
            aux = x
    return tipo

def calcDensidadeLista(listaAdj):
    arestas = 0
    size = len(listaAdj)
    for i in range(size):
        for x in listaAdj[i]:
            arestas += 1
    if int(repr(tipoGrafoAdj(listaAdj))[-1]) == 0:
        dens = arestas/(size*(size-1))
        print(dens)
    elif int(repr(tipoGrafoAdj(listaAdj))[-1]) == 1:
        dens = (arestas/2)/(size*(size-1))
        print(dens)

    print(dens)
    return

def insereArestaLista(listaAdj,vi,vj):
    size = len(listaAdj)
    for i in range(size):
        if i == vi:
            listaAdj[i].append(vj)
            listaAdj[i].sort()
        elif i == vj:
            listaAdj[i].append(vi)
            listaAdj[i].sort()
    print(listaAdj)
    return listaAdj

def removeArestaLista(listaAdj,vi,vj):
    if int(repr(tipoGrafoAdj(listaAdj))[-1]) == 0:
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)
    elif int(repr(tipoGrafoAdj(listaAdj))[-1]) == 1:
        listaAdj[vi].remove(vj)
    print(listaAdj)

def insereVerticeLista(listaAdj):
    size = len(listaAdj)
    listaAdj[size]= []
    print(listaAdj)
    return

def removeVerticeLista(listaAdj,vi):
    size = len(listaAdj)
    for i in range(size):
        listaAdj[i] = list(filter((vi).__ne__,listaAdj[i]))
    del listaAdj[vi]
    print(listaAdj)
    return