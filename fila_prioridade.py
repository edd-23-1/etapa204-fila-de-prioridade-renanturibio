# -*- coding:UTF-8 -*-
from no import No

class FilaPrioridade:
    """
    Implementação de Fila de Prioridade com Capacidade
    A fila de prioridade a ser implementada deverá ser em ordem crescente
    Os itens com maior prioridade devem ocupar as primeiras posições
    Itens com prioridades iguais devem ser ordenados conforme ordem de inserção
    """

    def _init_(self, capacidade=5):
        self.__inicio = None
        self.__capacidade = capacidade
        self.__qtdItens = 0
        print(f"Criada EDD Fila de Prioridade com capacidade: {capacidade}")

    def is_empty(self) -> bool:
        return self.__qtdItens == 0

    def is_full(self) -> bool:
        return self._qtdItens == self._capacidade

    def first(self) -> No:
        return self.__inicio

    def add(self, valor, prioridade) -> bool:
        
        novo_no = No(valor, prioridade)

        if self.is_full():
            raise Exception("A fila de prioridade está cheia!")

        if self.is_empty() or prioridade > self.__inicio.prioridade:
            novo_no.prox = self.__inicio
            self.__inicio = novo_no
        else:
            atual = self.__inicio
            while atual.prox is not None and atual.prox.prioridade >= prioridade:
                atual = atual.prox

            novo_no.prox = atual.prox
            atual.prox = novo_no

        self.__qtdItens += 1
        return True

    def remove(self) -> No:
        if self.is_empty():
            raise Exception("A fila de prioridade está vazia!")

        no_removido = self.__inicio
        self._inicio = self._inicio.prox
        self.__qtdItens -= 1
        return no_removido

    def display(self) -> list[tuple()]:
        if self.is_empty():
            print("A fila de prioridade está vazia!")
            return []

        lista_itens = []
        atual = self.__inicio
        while atual is not None:
            lista_itens.append((atual.dado, atual.prioridade))
            atual = atual.prox

        print(lista_itens)
        return lista_itens

    def size(self) -> int:
        return self.__qtdItens
