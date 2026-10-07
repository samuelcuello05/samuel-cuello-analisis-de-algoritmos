# Laboratorio 1 — Fundamentos, complejidad y recurrencias

**Estudiante:** Samuel Cristobal Cuello Duque
**Curso:** Análisis de Algoritmos 190304006-1
**Laboratorio:** Fundamentos, complejidad y recurrencias

---

# Instrucciones de reproducción

El laboratorio fue desarrollado utilizando Python 3 y la biblioteca `matplotlib`.

La estructura del proyecto es:

```text
curso-analisis-algoritmos/
└── lab1-fundamentos-complejidad-recurrencias/
    ├── README.md
    ├── algoritmos.py
    ├── datos.py
    ├── parte3_casos.py
    ├── parte4_complejidad.py
    └── graficas/
        ├── parte3_comparaciones.png
        ├── parte3_tiempo.png
        └── parte4_tiempo.png
```

Para preparar el entorno se puede crear y activar un entorno virtual en la raíz del repositorio (`curso-analisis-algoritmos/`):

```bash
python -m venv .venv
```

En Git Bash:

```bash
source .venv/Scripts/activate
```

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Posteriormente se instalan las dependencias registradas en `requirements.txt` (incluye `matplotlib`):

```bash
python -m pip install -r requirements.txt
```

Los scripts se ejecutan desde la carpeta del laboratorio, porque guardan las gráficas en la ruta relativa `graficas/`:

```bash
cd lab1-fundamentos-complejidad-recurrencias
```

## Ejecutar la Parte 3

La implementación y el experimento de la Parte 3 se encuentran en:

* [Código de la Parte 3](parte3_casos.py)
* [Algoritmos de ordenamiento](algoritmos.py)
* [Generadores de datos](datos.py)

Para ejecutar:

```bash
python parte3_casos.py
```

El programa genera:

* `graficas/parte3_comparaciones.png`
* `graficas/parte3_tiempo.png`

## Ejecutar la Parte 4

La implementación y comparación de la Parte 4 se encuentran en:

* [Código de la Parte 4](parte4_complejidad.py)
* [Algoritmos de ordenamiento](algoritmos.py)
* [Generadores de datos](datos.py)

Para ejecutar:

```bash
python parte4_complejidad.py
```

El programa genera:

* `graficas/parte4_tiempo.png`
* En consola, los tiempos y comparaciones de los dos algoritmos por tamaño, y una tabla con ambos algoritmos sobre los tres escenarios para `n = 6400`.

En la Parte 4 cada medición se repite 3 veces sobre el mismo lote y se reporta la mediana del tiempo, para reducir el ruido del sistema operativo.

La generación de los datos se realiza antes de iniciar la medición. Por esta razón, el tiempo medido corresponde a la ejecución del algoritmo de ordenamiento y no al tiempo necesario para crear la entrada.

---

# Parte 1 — Corrección vs. eficiencia

La **corrección** de un algoritmo significa que este produce el resultado esperado para todas las entradas válidas. En el caso de la plataforma Tamiza, el algoritmo debe ordenar correctamente los registros de acuerdo con el índice de riesgo, de mayor a menor.

La **eficiencia** se refiere a los recursos utilizados para obtener ese resultado, principalmente el tiempo de ejecución y la memoria. Por esta razón, un algoritmo puede ser correcto y al mismo tiempo tardar demasiado para la restricción de tiempo de una situación real.

En Tamiza existe una restricción estricta: el proceso nocturno debe ejecutarse entre las **2:00 a. m. y las 6:00 a. m.**, por lo que existe una ventana máxima de **cuatro horas**. Si el algoritmo consigue ordenar correctamente los registros, pero tarda más de cuatro horas, el sistema no cumple con el requisito operativo.

La propuesta de utilizar un servidor con el doble de velocidad puede disminuir el tiempo de ejecución, pero no cambia la complejidad del algoritmo. Si el problema principal es que se utiliza un algoritmo con crecimiento cuadrático, aumentar la velocidad del hardware solamente proporciona una mejora limitada mientras la cantidad de registros continúa creciendo. Con un crecimiento cuadrático, una máquina el doble de rápida solo permite ordenar unas 1,41 veces más registros en el mismo tiempo, mientras que el programa pasó de 20.000 a 1.200.000 registros, es decir, 60 veces más datos, lo que en un algoritmo cuadrático significa cerca de 3.600 veces más trabajo.

Un ejemplo propio sería un sistema de una tienda que debe ordenar **500.000 productos por precio antes de generar un catálogo que debe publicarse a las 6:00 a. m.** Si se utiliza un algoritmo correcto pero con complejidad Θ(n²), el sistema podría generar correctamente el catálogo, pero no terminar a tiempo. En este caso, cumplir con el resultado no es suficiente porque también existe una restricción de tiempo.

Por lo tanto, en Tamiza se debe buscar una solución que sea correcta y que, además, en tiempo de ejecución alcance a ordenar los 1.200.000 registros dentro de la ventana de cuatro horas.

---

# Parte 2 — Responsabilidad ambiental y ética

## Dimensión ambiental

Mientras el proceso nocturno corre, el servidor mantiene el procesador a alta carga y consume energía eléctrica todo ese tiempo, además de la refrigeración del centro de datos: más horas de ejecución son más kilovatios-hora.

Para dimensionarlo, supongamos un servidor que consume unos 400 W bajo carga (es un supuesto, no un dato medido). Si `insertion_sort` ocupa toda la ventana de cuatro horas cada madrugada, gasta cerca de 1,6 kWh por noche. Una sola noche parece poco, pero el proceso corre los 365 días del año: son unos 584 kWh al año y casi 2.900 kWh en cinco años, solo en ordenar una lista. Según las mediciones de la Parte 4, `merge_sort` haría el mismo trabajo en segundos, así que ese consumo prácticamente desaparece.

Como `insertion_sort` crece de forma cuadrática, si el número de registros aumenta un 10 % al año, el tiempo de ordenamiento aumenta cerca de un 21 % ((1,1)(1,1) = 1,21). El gasto se acumula noche tras noche y, encima, crece cada año. Un servidor más potente tampoco ayuda en lo ambiental: suele consumir más energía y es otro equipo que fabricar y desechar.

## Dimensión ética: perjuicios y quién asume el costo

**Perjuicio 1: el paciente de alto riesgo que queda fuera de la lista.** Pensemos en un paciente con índice de riesgo 950, que por sus resultados debería estar entre las primeras llamadas del día. Si el proceso no termina antes de las 6:00 a. m., el centro de contacto trabaja con una lista parcial y sin ordenar, y esa persona puede quedar por fuera. La llaman días después, o no la llaman, y mientras tanto su riesgo cardiovascular sigue sin atención. El costo lo asume el paciente, con su salud, y es el más grave porque no se puede revertir.

**Perjuicio 2: el operador del centro de contacto.** El operador empieza su turno a las 6:00 a. m. con una lista incompleta y desordenada. No tiene forma de saber a quién llamar primero, así que puede terminar llamando a personas de bajo riesgo antes que a las de alto riesgo sin darse cuenta. El costo lo asume directamente el operador, que trabaja sin un criterio confiable y carga con la presión de esas decisiones. En el plano institucional lo asume la Secretaría, que responde ante los pacientes y los entes de control por una atención mal priorizada.

**Perjuicio 3: el equipo de desarrollo.** Cada noche que el proceso falla, el equipo debe atender el incidente y revisar qué quedó sin procesar. Ese costo lo asume el equipo técnico, y es consecuencia de haber dejado en producción un algoritmo que nadie volvió a analizar cuando el volumen de datos cambió.

## La obligación que impone el orden de la lista

En Tamiza el orden no es un detalle de presentación: decide a quién se llama primero. Por eso no basta con que el proceso sea rápido; el resultado tiene que ser exacto y verificable. Un error en el ordenamiento, aunque el proceso termine a tiempo, pone a una persona de bajo riesgo por delante de alguien que necesitaba la cita con más urgencia.

Esto le impone a quien decide qué algoritmo corre obligaciones adicionales: probar la corrección del ordenamiento antes de cada cambio (incluyendo empates entre índices iguales), verificar al final de cada ejecución que la lista quedó realmente ordenada, y nunca entregar una lista parcial sin advertírselo al centro de contacto. La responsabilidad no termina en que el código funcione: incluye los recursos que consume y las consecuencias que tiene sobre personas concretas.

---

# Parte 3 — Casos de entrada e instrumentación

## Código utilizado

La implementación de los algoritmos se encuentra en [algoritmos.py](algoritmos.py), mientras que los generadores de los escenarios se encuentran en [datos.py](datos.py).

El experimento completo de esta parte se encuentra en [parte3_casos.py](parte3_casos.py).

---

## 3.1 Mejor, peor y promedio caso

Los tres casos se definen dejando fijo el tamaño de entrada `n` y mirando el costo (número de comparaciones o tiempo) sobre todas las entradas posibles de ese tamaño. Para `insertion_sort`, esas entradas son todas las formas de ordenar `n` índices distintos, es decir, las `n!` permutaciones.

* **Peor caso:** es el máximo del costo sobre todas las entradas de tamaño `n`. Funciona como una garantía: ninguna entrada de ese tamaño cuesta más.
* **Mejor caso:** es el mínimo del costo sobre todas las entradas de tamaño `n`.
* **Caso promedio:** es el promedio (valor esperado) del costo sobre todas las entradas de tamaño `n`, suponiendo que todas las permutaciones son igual de probables. No significa tomar el punto medio entre el mejor y el peor caso, sino calcular cuánto cuesta en promedio una entrada cualquiera de ese tamaño.

En este laboratorio se utilizaron tres escenarios:

* **A — Aleatorio:** los elementos se encuentran en un orden sin relación con el orden requerido.
* **B — Casi ordenado:** aproximadamente el 98 % de los registros ya se encuentra ordenado y el 2 % restante corresponde a nuevos registros agregados al final.
* **C — Inverso:** los elementos se encuentran en el sentido contrario al orden requerido.

Para decidir si un algoritmo puede utilizarse en producción bajo una ventana estricta de cuatro horas, se debe prestar especial atención al **peor caso**, porque no sería seguro asumir que siempre se recibirán entradas favorables. También es importante observar el comportamiento promedio, ya que representa el rendimiento esperado sobre entradas generales.

### Predicción previa

Antes de ejecutar las pruebas se esperaba que:

* **Casi ordenado** presentara el menor número de comparaciones y menor tiempo.
* **Inverso** presentara el mayor número de comparaciones y mayor tiempo.
* **Aleatorio** presentara un comportamiento intermedio.

Esta predicción se realizó antes de observar los resultados experimentales.

---

## 3.2 Resultados de las comparaciones

Las pruebas se realizaron con los tamaños:

`100, 200, 400, 800, 1600, 3200 y 6400`.

Los resultados fueron:

| Tamaño `n` |  Aleatorio | Casi ordenado |    Inverso |
| ---------: | ---------: | ------------: | ---------: |
|        100 |      2.542 |           100 |      4.950 |
|        200 |      9.970 |           203 |     19.900 |
|        400 |     40.436 |           417 |     79.800 |
|        800 |    160.484 |           866 |    319.600 |
|      1.600 |    648.481 |         1.851 |  1.279.200 |
|      3.200 |  2.533.103 |         4.172 |  5.118.400 |
|      6.400 | 10.276.753 |        10.277 | 20.476.800 |

El escenario **inverso** fue claramente el peor de los tres escenarios medidos. Para `n = 6400`, necesitó **20.476.800 comparaciones**.

El escenario **aleatorio** presentó un comportamiento intermedio, alcanzando **10.276.753 comparaciones** para `n = 6400`.

El escenario **casi ordenado** fue el más favorable, con solamente **10.277 comparaciones** para `n = 6400`.

Por lo tanto, los resultados confirman la predicción inicial:

**Inverso → peor comportamiento**

**Aleatorio → comportamiento intermedio**

**Casi ordenado → mejor comportamiento**

Es importante aclarar que el escenario aleatorio representa experimentalmente un comportamiento intermedio entre los casos favorable y desfavorable, mientras que el caso promedio en términos teóricos se refiere al costo esperado sobre las posibles entradas.

![Comparaciones de insertion sort](graficas/parte3_comparaciones.png)

---

## 3.3 Resultados del tiempo de ejecución

Los tiempos obtenidos fueron:

| Tamaño `n` | Aleatorio (s) | Casi ordenado (s) | Inverso (s) |
| ---------: | ------------: | ----------------: | ----------: |
|        100 |      0.000363 |          0.000012 |    0.000459 |
|        200 |      0.001024 |          0.000020 |    0.001826 |
|        400 |      0.003918 |          0.000047 |    0.007599 |
|        800 |      0.016087 |          0.000100 |    0.030986 |
|      1.600 |      0.066987 |          0.000213 |    0.129040 |
|      3.200 |      0.261485 |          0.000485 |    0.524873 |
|      6.400 |      1.074454 |          0.001209 |    2.106491 |

El escenario **inverso** presentó el mayor tiempo de ejecución. Para `n = 6400`, tardó **2.106491 segundos**.

El escenario **aleatorio** tardó **1.074454 segundos**.

El escenario **casi ordenado** solamente tardó **0.001209 segundos**.

La diferencia entre los escenarios aumenta considerablemente al crecer el tamaño de la entrada. Esto demuestra experimentalmente que `insertion_sort` es muy sensible al orden inicial de los datos.

![Tiempo de insertion sort](graficas/parte3_tiempo.png)

---

## 3.4 Comparación con la teoría

En el mejor caso, los registros ya están ordenados de acuerdo con el criterio requerido. En este caso, `insertion_sort` necesita aproximadamente una comparación por cada elemento, por lo que:

**T(n) = n - 1**

y:

**T(n) = Θ(n)**

Esto se refleja en el escenario casi ordenado, donde para `n = 6400` solamente se realizaron **10.277 comparaciones**.

En el peor caso, los elementos están en el orden contrario. En este escenario se realizan:

**1 + 2 + 3 + ... + (n - 1)**

comparaciones.

La suma es:

**n(n - 1) / 2**

Para `n = 6400`:

**6400 × 6399 / 2 = 20.476.800**

Este resultado coincide exactamente con la medición obtenida para el escenario inverso.

Por lo tanto:

**Peor caso = Θ(n²)**

El caso promedio también tiene comportamiento:

**Θ(n²)**

La justificación está en la Parte 4.1: en promedio cada elemento se desplaza la mitad del camino hacia el inicio, lo que da cerca de n(n − 1)/4 comparaciones, la mitad del peor caso. Para `n = 6400` eso son 10.238.400 comparaciones, más casi una por cada iteración que termina en `break` (≈ 6.391), es decir, ≈ 10.244.791. El escenario aleatorio midió 10.276.753, una diferencia de apenas 0,3 %. Además, la razón aleatorio/inverso es 10.276.753 / 20.476.800 ≈ 0,50, justo la mitad que predice la teoría.

Los resultados experimentales son coherentes con estas complejidades. El crecimiento del escenario inverso es cuadrático, mientras que el escenario casi ordenado presenta un crecimiento mucho menor.

---

# Parte 4 — Complejidad y comparación de algoritmos

## Código utilizado

La comparación experimental se encuentra en [parte4_complejidad.py](parte4_complejidad.py).

La implementación de `insertion_sort` y `merge_sort` se encuentra en [algoritmos.py](algoritmos.py), mientras que la generación del escenario aleatorio se encuentra en [datos.py](datos.py).

---

## 4.1 Desarrollo de la recurrencia de Merge Sort

La recurrencia de `merge_sort` es:

**T(n) = 2T(n/2) + Θ(n)**

Cada término representa:

* `2T(n/2)`: el algoritmo divide el problema en **dos subproblemas**, cada uno de tamaño `n/2`.
* `Θ(n)`: después de resolver las dos partes, se deben combinar los resultados. Esta combinación requiere recorrer los elementos y tiene costo lineal.

### Árbol de recurrencia

En el primer nivel:

**T(n) = 2T(n/2) + Θ(n)**

El costo fuera de la recursión es:

**Θ(n)**

En el segundo nivel aparecen dos problemas:

**2T(n/2) = 4T(n/4) + 2Θ(n/2)**

Como:

**2Θ(n/2) = Θ(n)**

el costo de este nivel también es:

**Θ(n)**

En el tercer nivel:

**4T(n/4) = 8T(n/8) + 4Θ(n/4)**

y:

**4Θ(n/4) = Θ(n)**

Por lo tanto, cada nivel del árbol tiene un costo total de:

**Θ(n)**

El proceso continúa hasta llegar a subproblemas de tamaño 1.

Para encontrar la cantidad de niveles:

**n / 2^k = 1**

Multiplicando por `2^k`:

**n = 2^k**

Aplicando logaritmo base 2:

**k = log₂(n)**

Por lo tanto, hay `log₂(n)` niveles internos (del nivel 0 al nivel `log₂(n) − 1`) y cada uno cuesta `cn`, donde `c` es la constante del costo lineal de la mezcla. En el nivel `log₂(n)` quedan las hojas: `2^(log₂ n) = n` subproblemas de tamaño 1, cada uno con costo constante.

El árbol completo, suponiendo que `n` es potencia de 2, es:

```text
Nivel        Nodos del árbol (costo de cada nodo)                Nodos   Costo del nivel
  0                           cn                                    1     cn
                        /             \
  1                 c(n/2)           c(n/2)                         2     2 · c(n/2) = cn
                   /     \          /     \
  2            c(n/4)  c(n/4)   c(n/4)  c(n/4)                      4     4 · c(n/4) = cn
                 ...     ...      ...     ...                     ...     ...
  k          2^k nodos, cada uno de tamaño n/2^k                  2^k     2^k · c(n/2^k) = cn
                 ...     ...      ...     ...                     ...     ...
log₂(n)     T(1)  T(1)  T(1)  T(1)  ...  T(1)  T(1)  (hojas)        n     n · Θ(1) = Θ(n)
                                                         ─────────────────────────────────
                                                         Total:  cn · log₂(n) + Θ(n)
```

El costo total es la suma de los costos de todos los niveles internos más el costo de las hojas:

```text
T(n) = Σ (k = 0 .. log₂(n) − 1) 2^k · c(n / 2^k)  +  n · Θ(1)
     = Σ (k = 0 .. log₂(n) − 1) cn                +  Θ(n)
     = cn · log₂(n)                               +  Θ(n)
```

Es decir, `n` de trabajo por cada uno de los `log₂(n)` niveles, más `n` hojas de costo constante. Como `cn · log₂(n)` crece más rápido que `Θ(n)`, el término de las hojas no cambia el orden de crecimiento, y por lo tanto:

**T(n) = Θ(n log n)**

Así, la complejidad temporal de `merge_sort` es:

**Mejor caso: Θ(n log n)**
**Caso promedio: Θ(n log n)**
**Peor caso: Θ(n log n)**

---

## Complejidad de Insertion Sort línea por línea

El análisis se hace sobre el código de `insertion_sort` en [algoritmos.py](algoritmos.py), con los números de línea del archivo. Sea `n = len(datos)`. El ciclo externo recorre `i = 1, 2, ..., n − 1`, y para cada iteración `i` se definen:

* `dᵢ`: número de desplazamientos, es decir, cuántas veces entra a la rama `if` y corre un elemento una posición a la derecha. Puede valer entre 0 e `i`.
* `bᵢ`: vale 1 si el `while` termina por el `break` (encontró la posición antes de llegar al inicio) y 0 si termina porque `j` llegó a −1.

Con esto, en la iteración `i` la condición `while j >= 0` se evalúa `dᵢ + 1` veces (una por cada desplazamiento más la evaluación con la que sale o entra al `break`), y la comparación entre elementos `copia[j] < clave` se ejecuta `dᵢ + bᵢ` veces.

| Línea | Código                         | Costo  | Veces que se ejecuta |
| ----: | ------------------------------ | ------ | -------------------- |
|    16 | `copia = datos.copy()`         | c₁ · n | 1                    |
|    17 | `comparaciones = 0`            | c₂     | 1                    |
|    19 | `for i in range(1, len(copia)):` | c₃   | n                    |
|    20 | `clave = copia[i]`             | c₄     | n − 1                |
|    21 | `j = i - 1`                    | c₅     | n − 1                |
|    23 | `while j >= 0:`                | c₆     | Σ (dᵢ + 1)           |
|    24 | `comparaciones += 1`           | c₇     | Σ (dᵢ + bᵢ)          |
|    26 | `if copia[j] < clave:`         | c₈     | Σ (dᵢ + bᵢ)          |
|    27 | `copia[j + 1] = copia[j]`      | c₉     | Σ dᵢ                 |
|    28 | `j -= 1`                       | c₁₀    | Σ dᵢ                 |
|    30 | `break`                        | c₁₁    | Σ bᵢ                 |
|    32 | `copia[j + 1] = clave`         | c₁₂    | n − 1                |
|    34 | `return copia, comparaciones`  | c₁₃    | 1                    |

Todas las sumatorias van de `i = 1` hasta `n − 1`. La línea 16 se ejecuta una vez, pero copiar la lista cuesta proporcional a `n`; la línea 19 se evalúa `n` veces (`n − 1` iteraciones más la evaluación final que termina el ciclo).

Sumando costo × veces:

```text
T(n) = c₁n + c₂ + c₃n + (c₄ + c₅ + c₁₂)(n − 1) + c₆ Σ(dᵢ + 1)
       + (c₇ + c₈) Σ(dᵢ + bᵢ) + (c₉ + c₁₀) Σdᵢ + c₁₁ Σbᵢ + c₁₃
```

Agrupando los términos que no dependen del orden de los datos en `a·n + b`, y llamando `D = Σ dᵢ` al total de desplazamientos:

```text
T(n) = a·n + b + e·D + f·Σbᵢ

donde  e = c₆ + c₇ + c₈ + c₉ + c₁₀   y   f = c₇ + c₈ + c₁₁
```

Como cada `bᵢ` vale 0 o 1, `Σbᵢ ≤ n − 1`, así que ese término es a lo sumo lineal. Lo que decide el orden de crecimiento es `D`, el total de desplazamientos. Lo que cambia entre los casos es cuánto vale `D`.

### Mejor caso

La lista ya viene de mayor a menor (como el 98 % del escenario B). Cada `clave` es menor que el elemento anterior, así que `copia[j] < clave` es falso en la primera comparación y sale por el `break`: dᵢ = 0 y bᵢ = 1.

```text
D = 0,   Σbᵢ = n − 1
T(n) = a·n + b + f(n − 1) = (a + f)·n + (b − f)
```

Es una función lineal: T(n) = Θ(n). El número de comparaciones es `Σ(dᵢ + bᵢ) = n − 1`, y efectivamente el código da 99 comparaciones para una lista ordenada de 100 elementos.

### Peor caso

La lista viene de menor a mayor (escenario C). Cada `clave` es mayor que todos los elementos anteriores, así que se desplazan todos y el ciclo termina porque `j` llega a −1: dᵢ = i y bᵢ = 0.

```text
D = 1 + 2 + ... + (n − 1) = n(n − 1) / 2
T(n) = e · n(n − 1)/2 + a·n + b = (e/2)·n² + (a − e/2)·n + b
```

El término dominante es `n²`: T(n) = Θ(n²). Las comparaciones son exactamente `n(n − 1)/2`, que para `n = 6400` da 20.476.800, igual a lo medido en la Parte 3.

### Caso promedio

Se supone que las `n!` permutaciones de la entrada son igual de probables. En la iteración `i`, los `i` elementos anteriores ya están ordenados entre sí, y la `clave` tiene la misma probabilidad de quedar en cualquiera de las `i + 1` posiciones relativas entre ellos. Dicho de otra forma, cada uno de los `i` elementos anteriores es menor que la `clave` con probabilidad ½, y por lo tanto hay que desplazarlo con probabilidad ½. Así:

```text
E[dᵢ] = i / 2
```

Es decir, en promedio cada elemento se mueve la mitad del camino hacia el inicio. Sumando:

```text
E[D] = Σ (i = 1 .. n − 1) i/2 = n(n − 1) / 4
E[T(n)] = e · n(n − 1)/4 + (término a lo sumo lineal) = (e/4)·n² + O(n)
```

Por lo tanto T(n) = Θ(n²) también en el caso promedio. El costo es aproximadamente la mitad del peor caso: cambia la constante, pero no el orden de crecimiento.

Contraste con lo medido: las comparaciones esperadas son `n(n − 1)/4` más casi una por cada salida por `break` (`Σ i/(i+1) ≈ n − ln n`). Para `n = 6400` eso da ≈ 10.244.791, y el escenario aleatorio midió 10.276.753 (0,3 % de diferencia). Para `n = 100` da ≈ 2.570, y se midieron 2.542.

### Tabla de complejidades

| Algoritmo      | Mejor caso | Caso promedio | Peor caso  |
| -------------- | ---------- | ------------- | ---------- |
| Insertion Sort | Θ(n)       | Θ(n²)         | Θ(n²)      |
| Merge Sort     | Θ(n log n) | Θ(n log n)    | Θ(n log n) |

---

## 4.2 Resultados experimentales de tiempo

Se utilizaron los mismos tamaños de la Parte 3 para ambos algoritmos, sobre el escenario A (aleatorio). Cada tiempo es la mediana de 3 ejecuciones sobre el mismo lote; las comparaciones no varían entre repeticiones porque el lote es el mismo.

| Tamaño `n` | Insertion Sort (s) | Merge Sort (s) | Comparaciones Insertion | Comparaciones Merge |
| ---------: | -----------------: | -------------: | ----------------------: | ------------------: |
|        100 |           0.000241 |       0.000171 |                   2.542 |                 547 |
|        200 |           0.000928 |       0.000333 |                   9.970 |               1.283 |
|        400 |           0.003924 |       0.000749 |                  40.436 |               2.972 |
|        800 |           0.016047 |       0.001611 |                 160.484 |               6.744 |
|      1.600 |           0.066484 |       0.003456 |                 648.481 |              15.046 |
|      3.200 |           0.263151 |       0.007790 |               2.533.103 |              33.246 |
|      6.400 |           1.066551 |       0.016382 |              10.276.753 |              72.967 |

![Comparación de tiempos entre insertion sort y merge sort](graficas/parte4_tiempo.png)

La curva de Insertion Sort se dobla hacia arriba: cada vez que `n` se duplica, su tiempo se multiplica por aproximadamente 4 (de 3.200 a 6.400 pasa de 0.263151 s a 1.066551 s, ×4,05; de 1.600 a 3.200, ×3,96). Para `n = 6400` alcanza 1.066551 segundos.

La curva de Merge Sort es casi una línea recta pegada al eje: cada vez que `n` se duplica, su tiempo se multiplica por algo más de 2 (de 3.200 a 6.400 pasa de 0.007790 s a 0.016382 s, ×2,10). Para `n = 6400` alcanza solamente 0.016382 segundos.

La distancia entre las dos curvas crece con `n`. En la última medición, `merge_sort` fue aproximadamente:

**1.066551 / 0.016382 ≈ 65,1 veces más rápido**

que `insertion_sort`.

**Contraste con la Parte 4.1.** Lo que hace cada curva es justo lo que predicen las complejidades calculadas. Si un algoritmo es Θ(n²), duplicar `n` multiplica el tiempo por 2² = 4, que es lo que se mide en `insertion_sort`. Si es Θ(n log n), duplicar `n` lo multiplica por 2 · log₂(2n)/log₂(n), que para estos tamaños es ≈ 2,1 a 2,2, y es lo que se mide en `merge_sort`. Las comparaciones de `merge_sort` para `n = 6400` (72.967) también quedan por debajo de `n · log₂(n) ≈ 80.921`, de acuerdo con la cota. Por lo tanto, la conclusión que se lee en la gráfica coincide con la teoría: para el volumen de Tamiza, merge_sort es el mejor de los dos algoritmos.

**¿Por qué las curvas casi se tocan en los tamaños pequeños?** Hay dos razones, y ambas se ven en la tabla:

1. **Cada comparación de merge sort cuesta más.** Con `n = 100`, `insertion_sort` hace 2.542 comparaciones y `merge_sort` solo 547 (4,6 veces menos), pero en tiempo `merge_sort` es apenas 1,4 veces más rápido (0.000241 s contra 0.000171 s). Dividiendo, `insertion_sort` gasta ≈ 95 ns por comparación y `merge_sort` ≈ 313 ns, más de tres veces más. Eso pasa porque, alrededor de cada comparación, `merge_sort` crea sublistas nuevas con `lista[:mitad]`, hace 2n − 1 llamadas recursivas (199 para `n = 100`) y va construyendo la lista combinada con `append`, mientras que `insertion_sort` solo mueve valores dentro de la misma lista. Con pocos elementos, la ventaja de hacer menos comparaciones todavía no alcanza a compensar ese costo extra; a partir de `n = 800` ya es ≈ 10 veces más rápido.
2. **La escala de la gráfica.** El eje vertical es lineal y llega hasta ≈ 1,07 s por el punto de `insertion_sort` en `n = 6400`. Para `n ≤ 800` todos los tiempos están por debajo de 0,017 s, menos del 2 % de la altura del eje, así que en la imagen ambos puntos parecen estar en cero aunque sus valores sean distintos.

---

# Parte 4.3 — Concepto técnico para el equipo de ingeniería

**Para:** equipo de ingeniería — Secretaría de Salud departamental
**Asunto:** algoritmo de ordenamiento del proceso nocturno de Tamiza y propuesta de servidor del doble de velocidad

**Recomendación.** Reemplazar `insertion_sort` por `merge_sort` como única implementación del ordenamiento de Tamiza, y no aprobar la compra del servidor como solución.

**Criterio: una sola implementación para cualquier canal.** El lote puede llegar aleatorio (A), casi ordenado (B) o invertido (C), y el canal puede cambiar sin aviso. Como la ventana de cuatro horas es estricta, el criterio fue escoger el algoritmo con el menor peor caso, no el que gana en el escenario más favorable. Medí ambos algoritmos sobre los tres escenarios con `n = 6400` (salida de [parte4_complejidad.py](parte4_complejidad.py), mediana de 3 repeticiones):

| Escenario         | Insertion Sort (s) | Merge Sort (s) |
| ----------------- | -----------------: | -------------: |
| A — Aleatorio     |           1.091844 |       0.015970 |
| B — Casi ordenado |           0.001244 |       0.010738 |
| C — Inverso       |           2.110377 |       0.010989 |

`insertion_sort` va de 0,0012 s a 2,11 s según el canal, casi 1.700 veces de diferencia. `merge_sort` se mantiene entre 0,011 s y 0,016 s en los tres. En el escenario B `insertion_sort` sí es unas 8,6 veces más rápido, pero esa ventaja depende de que el reproceso siga entregando la lista casi ordenada: si ese flujo cambia, el sistema cae al caso A o C sin que nadie lo note. Con `merge_sort` no hace falta detectar el canal ni mantener tres versiones.

**¿Cabe en la ventana con 1.200.000 registros?** Lo siguiente es una estimación por extrapolación, no una medición: el experimento llegó hasta 6.400 registros, y supongo que la forma de las curvas se mantiene y que el servidor de producción es comparable a mi equipo. Pasar de 6.400 a 1.200.000 multiplica `n` por k = 187,5.

* `insertion_sort`, escenario A (`parte4_tiempo.png`, `n = 6400`: 1.066551 s). Por ser cuadrático, el tiempo se multiplica por k² ≈ 35.156: ≈ 37.496 s ≈ 10,4 horas.
* `insertion_sort`, escenario C (`parte3_tiempo.png`, `n = 6400`: 2.106491 s): ≈ 74.056 s ≈ 20,6 horas.
* `merge_sort`, escenario A (`parte4_tiempo.png`, `n = 6400`: 0.016382 s). Se multiplica por k · log₂(1.200.000)/log₂(6.400) ≈ 187,5 × 1,60: ≈ 4,9 segundos.

El algoritmo actual no cabe en la ventana; el recomendado usa una fracción mínima de ella.

**Sobre el servidor del doble de velocidad.** Con el dato de `parte4_tiempo.png` para `n = 6400` (1.066551 s), un servidor dos veces más rápido bajaría la estimación del escenario A de 10,4 a 5,2 horas, y la del escenario C (desde `parte3_tiempo.png`, `n = 6400`) de 20,6 a 10,3 horas. Ambas siguen por fuera de las cuatro horas. Con un crecimiento cuadrático, duplicar la velocidad solo permite ordenar √2 ≈ 1,41 veces más registros: según mis mediciones, la máquina actual alcanzaría unos 744.000 registros aleatorios en cuatro horas y la nueva unos 1.052.000, todavía menos de 1.200.000, y el programa sigue creciendo.

**Consideraciones distintas del tiempo.** `merge_sort` necesita memoria adicional proporcional a `n` para las sublistas y la mezcla. Para 1.200.000 índices son del orden de decenas de megabytes: manejable, pero debe confirmarse en la prueba de carga. Además, como la mezcla usa `>=`, el ordenamiento es estable: los registros con el mismo índice de riesgo conservan el orden en que llegaron, lo que da un criterio predecible para los empates.

**Siguiente paso.** Implementar `merge_sort`, validar la estimación con una prueba de carga cercana a 1.200.000 registros y verificar automáticamente que la lista quedó ordenada antes de entregarla al centro de contacto.

---

# Conclusión general

El laboratorio permitió comprobar la importancia de analizar tanto la corrección como la eficiencia de un algoritmo antes de implementarlo en un sistema real.

En la Parte 3 se comprobó que `insertion_sort` depende considerablemente del orden inicial de los datos. Para `n = 6400`, el escenario casi ordenado necesitó solamente 10.277 comparaciones y 0.001209 segundos, mientras que el escenario inverso necesitó 20.476.800 comparaciones y 2.106491 segundos.

Los resultados coinciden con la teoría: `insertion_sort` tiene un mejor caso de Θ(n), pero un caso promedio y peor caso de Θ(n²).

En la Parte 4, la comparación entre ambos algoritmos mostró una ventaja clara para `merge_sort`. Para `n = 6400`, `insertion_sort` tardó 1.066551 segundos, mientras que `merge_sort` tardó 0.016382 segundos, siendo aproximadamente 65,1 veces más rápido en esta prueba. Además, `merge_sort` mantuvo tiempos parecidos en los tres escenarios, mientras que `insertion_sort` dependió por completo del canal de entrada.

La complejidad teórica explica esta diferencia: `insertion_sort` crece de manera cuadrática, mientras que `merge_sort` crece como Θ(n log n).

La extrapolación realizada para 1.200.000 registros también muestra por qué la elección del algoritmo es importante. Bajo las hipótesis utilizadas, `insertion_sort` podría tardar aproximadamente 10,4 horas en el escenario aleatorio y 20,6 horas en el inverso, superando la ventana de cuatro horas incluso con un servidor del doble de velocidad, mientras que `merge_sort` tendría una estimación de aproximadamente 4,9 segundos. Estas cifras son estimaciones y deben validarse mediante una prueba de carga real.

En conclusión, para Tamiza se recomienda utilizar merge_sort y realizar pruebas adicionales con un volumen de datos cercano al de producción. La mejora algorítmica debe ser la principal estrategia y el aumento de capacidad del servidor debe considerarse como un complemento.
