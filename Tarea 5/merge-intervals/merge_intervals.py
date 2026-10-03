from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lista = self._ordenar(intervals, 0, len(intervals) - 1)
        return self._fusionar(lista)

    def _ordenar(self, v, i, j):
        if i == j:
            return [v[i]]
        if i > j:
            return []
        k = (i + j) // 2
        return self._mezclar(self._ordenar(v, i, k), self._ordenar(v, k + 1, j))

    def _mezclar(self, a, b):
        salida = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i][0] <= b[j][0]:
                salida.append(a[i])
                i += 1
            else:
                salida.append(b[j])
                j += 1
        while i < len(a):
            salida.append(a[i])
            i += 1
        while j < len(b):
            salida.append(b[j])
            j += 1
        return salida

    def _fusionar(self, lista):
        if not lista:
            return []

        salida = [lista[0][:]]
        for i in range(1, len(lista)):
            inicio, fin = lista[i]
            if inicio <= salida[-1][1]:
                salida[-1][1] = max(salida[-1][1], fin)
            else:
                salida.append([inicio, fin])
        return salida