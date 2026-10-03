from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        filas = len(grid)
        columnas = len(grid[0])
        islas = 0

        for f in range(filas):
            for c in range(columnas):
                if grid[f][c] != '1':
                    continue
                islas += 1
                self._hundir(grid, f, c, filas, columnas)

        return islas

    def _hundir(self, grid, f, c, filas, columnas):
        pasos = ((-1, 0), (1, 0), (0, -1), (0, 1))
        pila = [(f, c)]
        grid[f][c] = '0'

        while pila:
            f, c = pila.pop()
            for df, dc in pasos:
                nf = f + df
                nc = c + dc
                if 0 <= nf < filas and 0 <= nc < columnas and grid[nf][nc] == '1':
                    grid[nf][nc] = '0'
                    pila.append((nf, nc))