# Cinco familias en LeetCode

**Curso:** Análisis de algoritmos · ITM · 2026-2
**Lenguaje:** Python 3
**Cuenta de LeetCode:** la misma con la que se hizo *Submit* en cada problema (ver las evidencias).

Los cinco ejercicios se resuelven **uno por uno**, cada uno con la familia que pide el enunciado:
ordenamiento, grafos, programación dinámica, greedy y backtracking. En cada caso el algoritmo
está implementado a mano (no se llama a `sort()` de la librería donde el ejercicio **es** el
ordenamiento, ni se hace backtracking sin retractarse, ni se pega código que no se pueda explicar).

Cada ejercicio vive en una carpeta nombrada por su **familia**, y el archivo se llama como el
problema, para que quede claro cuál es cuál.

```
Tarea 5/
├── README.md
├── Ordenamiento/              ← ejercicio 1 · ordenamiento
│   └── merge_intervals.py
├── Grafos/                    ← ejercicio 2 · grafos
├── ProgramacionDinamica/      ← ejercicio 3 · programación dinámica
├── Greedy/                    ← ejercicio 4 · greedy
├── Backtracking/              ← ejercicio 5 · backtracking
└── evidencias/                ← capturas Accepted (una por problema)
```

| # | Problema | Familia | Carpeta del código | Evidencia |
| --- | --- | --- | --- | --- |
| 1 | [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Ordenamiento | [`Ordenamiento/merge_intervals.py`](Ordenamiento/merge_intervals.py) | [Accepted](evidencias/merge-intervals-accepted.jpeg) |
| 2 | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | Grafos | `Grafos/number_of_islands.py` | _pendiente_ |
| 3 | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Programación dinámica | `ProgramacionDinamica/longest_common_subsequence.py` | _pendiente_ |
| 4 | [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Greedy | `Greedy/non_overlapping_intervals.py` | _pendiente_ |
| 5 | [39. Combination Sum](https://leetcode.com/problems/combination-sum/) | Backtracking | `Backtracking/combination_sum.py` | _pendiente_ |

---

## 1. 56. Merge Intervals

**Problema:** [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) · Medium
**Familia:** ordenamiento (merge sort) + una pasada lineal de fusión
**Código:** [`Ordenamiento/merge_intervals.py`](Ordenamiento/merge_intervals.py)

### Idea en dos frases

Se elige como **clave el extremo izquierdo** (`start`) y se ordena el arreglo de intervalos con
un **merge sort propio** (divide y vencerás por mitades), no con el `sort()` de la librería;
después, sobre la corrida ya ordenada, **una sola pasada de izquierda a derecha** mantiene el
intervalo "abierto" que es el último de `salida`: si el siguiente empieza antes o justo cuando
termina (`inicio <= salida[-1][1]`), se **ensancha** el `end`; si no, se **cierra** y se abre otro.

### Por qué una sola pasada basta (la justificación que se pide)

Después de ordenar por `start`, los inicios son no decrecientes. Al llegar al intervalo
`[inicio, fin]`:

- Si `inicio <= salida[-1][1]`, ambos se solapan (o se tocan) y su unión es
  `[salida[-1][0], max(salida[-1][1], fin)]`. Como el intervalo abierto ya está ordenado y es el
  último, solo hay que **subir el `end`**.
- Si `inicio > salida[-1][1]`, entonces el intervalo abierto **ya no puede crecer más**: ningún
  intervalo que venga después puede empezar por debajo de `inicio > salida[-1][1]`, así que
  ninguno lo solapa. Se puede **cerrar** de una vez y abrir el siguiente.

Por eso no hace falta repetir la pasada ni comparar todos contra todos (lo que sería O(n²)).

### Lo que NO es la solución

- No se concatenan los extremos sueltos y se ordenan esos números: aquí se ordenan **intervalos
  enteros** por su inicio, y la fusión se hace sobre la corrida de intervalos ya ordenada.
- No se usa `intervals.sort(key=...)` de la librería: el ordenamiento **es parte** del ejercicio,
  por eso `_ordenar` / `_mezclar` están escritos a mano (merge sort de verdad).
- La entrada no se modifica: `_fusionar` solo lee `lista[i]` y crea los intervalos fusionados
  nuevos (`[lista[0][:]]`, `[inicio, fin]`), así que el `intervals` que recibe
  `Solution.merge` queda intacto.

### Complejidad

Con `n = intervals.length` y `k = número de intervalos fusionados` (`k ≤ n`):

- **Tiempo: Θ(n log n).** El merge sort cumple `T(n) = 2·T(n/2) + Θ(n)`, que por el teorema
  maestro da `Θ(n log n)`; la pasada de fusión es solo `Θ(n)`. El término dominante es el
  ordenamiento, no la fusión.
- **Espacio: Θ(n).** La lista `lista` con los `n` intervalos (más `salida` con `k ≤ n`), y la
  recursión del merge sort es `Θ(log n)` de profundidad: en todo momento las listas vivas son
  segmentos disjuntos del arreglo original, así que nunca hay más de `n` intervalos en memoria.

### Evidencia de Accepted

![Accepted - 56. Merge Intervals](evidencias/merge-intervals-accepted.jpeg)

<!-- Evidencia opcional del detalle de runtime/memoria -->
<!-- ![Runtime y memoria - 56. Merge Intervals](evidencias/merge-intervals-runtime.jpeg) -->