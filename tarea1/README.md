# Tarea 1 - Algoritmos Greedy

## 860. Lemonade Change

**Problema:**  
https://leetcode.com/problems/lemonade-change/

**Criterio greedy:**  
Para cada cliente se entrega el cambio usando la combinación de billetes que menos comprometa los billetes pequeños disponibles. Cuando se debe entregar 15, se prefiere usar un billete de 10 y uno de 5, reservando los billetes de 5 cuando sea posible. Si no es posible dar el cambio exacto, se retorna `False`.

**Complejidad:**
- Tiempo: O(n), donde n es el número de clientes.
- Espacio: O(1).

**Evidencia de Accepted:**

![Accepted - Lemonade Change](evidencias/lemonade-change-accepted.jpg)


## 455. Assign Cookies

**Problema:**  
https://leetcode.com/problems/assign-cookies/

**Criterio greedy:**  
Se ordenan los niños y las galletas de menor a mayor. Para cada niño se intenta asignar la galleta más pequeña que sea suficiente para satisfacerlo. De esta forma se reservan las galletas grandes para los niños que realmente las necesitan.

**Complejidad:**
- Tiempo: O(n log n + m log m), por ordenar las listas de niños y galletas.
- Espacio: O(1) de espacio auxiliar.

**Evidencia de Accepted:**

![Accepted - Assign Cookies](evidencias/assign-cookies-accepted.jpg)
