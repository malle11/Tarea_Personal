# Taller de algoritmos en LeetCode — 5 familias

**Curso:** Análisis de algoritmos · ITM · 2026-2
**Lenguaje:** Python 3
**Cuenta de LeetCode:** la misma con la que se hizo *Submit* en cada problema (ver las evidencias).

Los cinco ejercicios se resuelven **uno por uno**, cada uno con la familia que pide el enunciado:
ordenamiento, grafos, programación dinámica, greedy y backtracking. En cada caso el algoritmo
está implementado a mano (no se llama a `sort()` de la librería donde el ejercicio **es** el
ordenamiento, ni se hace backtracking sin retractarse, ni se pega código que no se pueda explicar).

| # | Problema | Familia | Carpeta del código | Evidencia |
| --- | --- | --- | --- | --- |
| 1 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Ordenamiento | [`merge-intervals/merge_intervals.py`](merge-intervals/merge_intervals.py) | [Accepted](evidencias/merge-intervals-accepted.png) |
| 2 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Grafos | `number-of-islands/` | _pendiente_ |
| 3 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Programación dinámica | `longest-common-subsequence/` | _pendiente_ |
| 4 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy | `non-overlapping-intervals/` | _pendiente_ |
| 5 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | `combination-sum/` | _pendiente_ |

---

## 1. 56. Merge Intervals

**Problema:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) · Medium
**Familia:** ordenamiento (merge sort) + una pasada lineal de fusión
**Código:** [`merge-intervals/merge_intervals.py`](merge-intervals/merge_intervals.py)

### Idea en dos frases

Se elige como **clave el extremo izquierdo** (`start`) y se ordena el arreglo de intervalos con
un **merge sort propio** (divide y vencerás por mitades), no con el `sort()` de la librería;
después, sobre la corrida ya ordenada, **una sola pasada de izquierda a derecha** mantiene el
intervalo "abierto" actual: si el siguiente empieza antes o justo cuando termina el actual
(`inicio <= actual[1]`), se **ensancha** el `end`; si no, se **cierra** el actual y se abre otro.

### Por qué una sola pasada basta (la justificación que se pide)

Después de ordenar por `start`, los inicios son no decrecientes. Al llegar al intervalo
`[inicio, fin]`:

- Si `inicio <= actual[1]`, ambos se solapan (o se tocan) y su unión es
  `[min(inicio, actual[0]), max(fin, actual[1])]`. Como `actual` ya está ordenado y es el último,
  solo hay que **subir el `end`** a `max(actual[1], fin)`.
- Si `inicio > actual[1]`, entonces `actual` **ya no puede crecer más**: ningún intervalo que
  venga después puedestarts por debajo de `inicio > actual[1]`, así que ninguno lo solapa. Se
  puede **cerrar** de una vez y empezar el siguiente.

Por eso no hace falta repetir la pasada ni comparar todos contra todos (lo que sería O(n²)).

### Lo que NO es la solución

- No se concatenan los extremos sueltos y se ordenan esos números: aquí se ordenan **intervalos
  enteros** por su inicio, y la fusión se hace sobre la corrida de intervalos ya ordenada.
- No se usa `intervals.sort(key=...)` de la librería: el ordenamiento **es parte** del ejercicio,
  por eso `_ordenar_por_inicio` / `_mezclar` están escritos a mano (merge sort de verdad).
- La entrada no se modifica: se trabaja sobre una copia (`ordenados[0][:]` al abrir el primer
  intervalo fusionado), así que el `intervals` que recibe `Solution.merge` queda intacto.

### Complejidad

Con `n = intervals.length` y `k = número de intervalos fusionados` (`k ≤ n`):

- **Tiempo: Θ(n log n).** El merge sort cumple `T(n) = 2·T(n/2) + Θ(n)`, que por el teorema
  maestro da `Θ(n log n)`; la pasada de fusión es solo `Θ(n)`. El término dominante es el
  ordenamiento, no la fusión.
- **Espacio: Θ(n).** La lista `ordenados` con los `n` intervalos (más la lista `fusionados` con
  `k ≤ n`), y la recursión del merge sort es `Θ(log n)` de profundidad. En el peor caso, sin
  tabla hash y sin colisiones, no hay factor extra.

### Evidencia de Accepted

![Accepted - 56. Merge Intervals](evidencias/merge-intervals-accepted.png)

<!-- Evidencia opcional del detalle de runtime/memoria -->
<!-- ![Runtime y memoria - 56. Merge Intervals](evidencias/merge-intervals-runtime.png) -->