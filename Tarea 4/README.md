# Tarea 4 - Programación dinámica en LeetCode

**Curso:** Análisis de algoritmos · ITM · 2026-2
**Tema:** programación dinámica (tabulación)

Los dos ejercicios están resueltos con **tabulación**, no con greedy ni con enumeración
de subconjuntos. En cada uno se nombra el estado, la recurrencia y los casos base.

| Ejercicio | Problema | Carpeta del código | Evidencia |
| --- | --- | --- | --- |
| 1 | [322. Coin Change](https://leetcode.com/problems/coin-change/) | [`coin-change/coin_change.py`](coin-change/coin_change.py) | [Accepted](evidencias/coin-change-accepted.png) |
| 2 | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [`partition-equal-subset-sum/partition_equal_subset_sum.py`](partition-equal-subset-sum/partition_equal_subset_sum.py) | [Accepted](evidencias/partition-equal-subset-sum-accepted.png) |

---

## 322. Coin Change

**Problema:** [322. Coin Change](https://leetcode.com/problems/coin-change/)
**Código:** [`coin-change/coin_change.py`](coin-change/coin_change.py)

### Estado

`dp[x]` = **mínimo número de monedas que suman exactamente `x`**, usando las denominaciones
disponibles. Si todavía no se puede armar `x`, `dp[x]` vale `IMPOSIBLE` (`amount + 1`, un
centinela mayor que cualquier respuesta posible, porque el peor caso válido es `amount`
monedas de valor 1).

### Casos base

- `dp[0] = 0`: armar el monto 0 no cuesta ninguna moneda (el subconjunto vacío).
- `dp[x] = IMPOSIBLE` para todo `x > 0`: antes de empezar a calcular, ningún monto se
  considera armable. Este es el "estado inicial" de la tabla.

### Recurrencia

Para cada monto `x` y cada moneda `c` tal que `c ≤ x`:

```
dp[x] = min(dp[x], 1 + dp[x - c])
```

Se prueba **todas** las monedas que alcanzan el monto `x` y se escoge la que deja el
resto `x - c` más barato. Como `x - c < x`, la entrada `dp[x - c]` ya está calculada: por eso
el monto se recorre **hacia adelante** (de 1 a `amount`) y no hace falta recursión.

Al final: si `dp[amount]` sigue siendo `IMPOSIBLE`, la respuesta es `-1`.

### Mochila no acotada: las monedas sí se reusan

El enunciado dice que hay **infinitas piezas** de cada denominación, así que el mismo
`for moneda in coins` puede volver a elegir la misma `moneda` en montos distintos. Eso es
lo que hace que `dp[x]` mire a `dp[x - c]` ya calculado **sin** desplazar nada: al calcular
`dp[6]` con `coins = [1, 3, 4]` se está reusing la moneda 3 que ya se usó en `dp[3]`.

Contraste obligatorio: con `{1, 3, 4}` y monto 6, el **greedy** "siempre la moneda más
grande" arma `4 + 1 + 1` = 3 piezas, mientras que DP arma `3 + 3` = **2 piezas**. El greedy
falla porque el sistema `{1, 3, 4}` no es canónico: no basta con tomar la denominación
inmediata, hay que considerar todas las que caben.

### Complejidad

Con `k = coins.length` y `X = amount`:

- **Tiempo: Θ(k · X)** — `X` montos por `k` monedas.
- **Espacio: Θ(X)** — el arreglo `dp` de `amount + 1` entradas.

Es **pseudo-polinomial en `X`**: es lineal en el *valor* del monto, no en el número de
bits que lo representan, que es el mismo aviso que da la guía.

### Evidencia de Accepted

![Accepted - 322. Coin Change](evidencias/coin-change-accepted.png)

---

## 416. Partition Equal Subset Sum

**Problema:** [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
**Código:** [`partition-equal-subset-sum/partition_equal_subset_sum.py`](partition-equal-subset-sum/partition_equal_subset_sum.py)

### Reducción a mochila 0/1

Si el arreglo se parte en dos subconjuntos de igual suma `W`, entonces cada subconjunto
suma `W` y `2W = S`, donde `S = sum(nums)`. O sea:

- Si `S` es **impar**, es imposible de entrada: se devuelve `False` sin tocar la tabla.
- Si `S` es par, basta preguntar **¿existe un subconjunto cuya suma sea exactamente
  `W = S / 2`?** Si existe, el complemento también suma `W` y ya está la partición.

Aquí el "valor" coincide con el "peso": no hay que maximizar nada, solo llenar la
capacidad exacta. Es la mochila 0/1 de la maleta (ejercicio 3 de la guía), pero en vez de
partir el frasco se decide si el subconjunto cabe.

### Estado

`dp[w]` = **¿existe un subconjunto de los números ya considerados cuya suma sea exactamente
`w`?** (booleano, no un mínimo: solo importa alcanzarlo o no).

### Casos base

- `dp[0] = True`: el subconjunto **vacío** suma 0. Sin este caso base nada sería alcanzable,
  porque todos los `dp[w]` con `w > 0` empiezan en `False`.

### Recurrencia (0/1)

Al considerar el número `nums[i]`, para todo `w ≥ nums[i]`:

```
dp[w] = dp[w] OR dp[w - nums[i]]
```

Es decir: la suma `w` es alcanzable si **ya lo era** sin tomar `nums[i]`, o si lo era la
suma `w - nums[i]` **añadiendo** este número.

### Cada número una vez: por eso el for va hacia atrás

`nums` no se puede reusar: es 0/1. Eso se refleja directamente en la dirección del for de
capacidad:

```
for w in range(objetivo, numero - 1, -1):   # W -> numero   (hacia adelante NO sirve)
```

- **Hacia atrás (`W → 0`)**: cuando se lee `dp[w - numero]`, esa posición **todavía no fue
  modificada en esta vuelta del for**, así que refleja los números previos. El número
  actual entra una sola vez.
- **Hacia adelante (`0 → W`)**: `dp[w - numero]` ya se actualizó con este mismo número, o
  sea el `numero` actual se contaría varias veces. Eso lo convertiría en el **ejercicio 1**
  (monedas reusables) y daría respuestas falsas.

Reutilizar el mismo número no está permitido; enumerar los `2^n` subconjuntos tampoco
(n puede ser 200, no corre).

### Complejidad

Con `n = nums.length` y `W = S / 2`:

- **Tiempo: Θ(n · W)** — `n` números por hasta `W` capacidades. No es `O(n²)`: `W` crece
  con el *valor* de la suma, no con la cantidad de elementos.
- **Espacio: Θ(W)** — el arreglo 1D de `W + 1` booleanos (Θ(n·W) solo si se deja la
  matriz completa; aquí se comprime a una sola fila).

### Evidencia de Accepted

![Accepted - 416. Partition Equal Subset Sum](evidencias/partition-equal-subset-sum-accepted.png)