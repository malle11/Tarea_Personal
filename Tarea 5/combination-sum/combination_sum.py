from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidatos = sorted(candidates)
        combinaciones = []
        self._buscar(candidatos, target, 0, [], combinaciones)
        return combinaciones

    def _buscar(self, candidatos, resto, inicio, actual, combinaciones):
        if resto == 0:
            combinaciones.append(actual[:])
            return

        for i in range(inicio, len(candidatos)):
            if candidatos[i] > resto:
                break

            actual.append(candidatos[i])
            self._buscar(candidatos, resto - candidatos[i], i, actual, combinaciones)
            actual.pop()