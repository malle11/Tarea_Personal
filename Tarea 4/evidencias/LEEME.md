# Evidencias - qué falta colocar aquí

Estas dos imágenes **no se pueden generar automáticamente**: tienen que salir del
**Submit** en LeetCode con la sesión de Malelly iniciada. Cuando las tengas, copia los
archivos a esta carpeta con **estos nombres exactos** (el README ya los enlaza):

```
evidencias/
├── coin-change-accepted.png
└── partition-equal-subset-sum-accepted.png
```

Si tu captura queda en `.jpeg`, cambia la extensión en el enlace del `README.md`
(las tareas 1 y 2 de este repo usan `.jpeg`, así que ambos formatos sirven).

## Cómo sacar cada captura

Para cada problema, repite los pasos:

1. Entra a <https://leetcode.com/problems/coin-change/> (o `/problems/partition-equal-subset-sum/`)
   **con tu cuenta de LeetCode abierta**.
2. Pestaña **Submit** (esquina inferior derecha del editor).
3. Borra el código que aparece y pega el contenido del archivo correspondiente:

   | Problema | Archivo a pegar |
   | --- | --- |
   | 322. Coin Change | `../coin-change/coin_change.py` |
   | 416. Partition Equal Subset Sum | `../partition-equal-subset-sum/partition_equal_subset_sum.py` |

4. Elige el lenguaje **Python3** y presiona **Submit**. No uses "Run Code": el veredicto
   que cuenta es el del botón **Submit**.
5. Cuando aparezca el recuadro verde **Accepted**, toma la captura.

## Qué debe verse en la captura (sin recortar lo esencial)

- El **número y título del problema** (o el enunciado) arriba.
- El **Accepted** en verde.
- La frase de **todos los test cases pasaron** y la lista de casos con palomita verde.
- **Runtime / Memory** y los porcentajes `beats ...%` si la plataforma los muestra
  (esa es justo la segunda imagen opcional).
- Tu **usuario de LeetCode** visible (esquina superior derecha) o el correo de la cuenta.

## Orden de las capturas

1. `coin-change-accepted.png`
2. `partition-equal-subset-sum-accepted.png`

Cuando las coloques, bórralo (o este archivo) para que quede limpio y ejecuta:

```
git add "Tarea 4/evidencias/coin-change-accepted.png"
git add "Tarea 4/evidencias/partition-equal-subset-sum-accepted.png"
```

Sin las imágenes en el repositorio, el ejercicio no cuenta como entregado.