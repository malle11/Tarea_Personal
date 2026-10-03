from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ordenados = self._ordenar_por_inicio(intervals, 0, len(intervals) - 1)
        return self._fusionar(ordenados)

    def _ordenar_por_inicio(self, intervalos, i, j):
        if i == j:
            return [intervalos[i]]
        if i > j:
            return []

        k = (i + j) // 2
        izquierda = self._ordenar_por_inicio(intervalos, i, k)
        derecha = self._ordenar_por_inicio(intervalos, k + 1, j)
        return self._mezclar(izquierda, derecha)

    def _mezclar(self, a, b):
        resultado = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i][0] <= b[j][0]:
                resultado.append(a[i])
                i += 1
            else:
                resultado.append(b[j])
                j += 1
        while i < len(a):
            resultado.append(a[i])
            i += 1
        while j < len(b):
            resultado.append(b[j])
            j += 1
        return resultado

    def _fusionar(self, ordenados):
        if not ordenados:
            return []

        fusionados = [ordenados[0][:]]
        for i in range(1, len(ordenados)):
            inicio, fin = ordenados[i]
            actual = fusionados[-1]
            if inicio <= actual[1]:
                actual[1] = max(actual[1], fin)
            else:
                fusionados.append([inicio, fin])
        return fusionados