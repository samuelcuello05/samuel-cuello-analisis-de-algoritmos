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

Para preparar el entorno se puede crear y activar un entorno virtual:

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

Posteriormente se instala `matplotlib`:

```bash
python -m pip install matplotlib
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

La generación de los datos se realiza antes de iniciar la medición. Por esta razón, el tiempo medido corresponde a la ejecución del algoritmo de ordenamiento y no al tiempo necesario para crear la entrada.

---

# Parte 1 — Corrección vs. eficiencia

La **corrección** de un algoritmo significa que este produce el resultado esperado para todas las entradas válidas. En el caso de la plataforma Tamiza, el algoritmo debe ordenar correctamente los registros de acuerdo con el índice de riesgo, de mayor a menor.

La **eficiencia** se refiere a los recursos utilizados para obtener ese resultado, principalmente el tiempo de ejecución y la memoria. Por esta razón, un algoritmo puede ser correcto y al mismo tiempo ser poco eficiente para una situación real.

En Tamiza existe una restricción estricta: el proceso nocturno debe ejecutarse entre las **2:00 a. m. y las 6:00 a. m.**, por lo que existe una ventana máxima de **cuatro horas**. Si el algoritmo consigue ordenar correctamente los registros, pero tarda más de cuatro horas, el sistema no cumple con el requisito operativo.

La propuesta de utilizar un servidor con el doble de velocidad puede disminuir el tiempo de ejecución, pero no cambia la complejidad del algoritmo. Si el problema principal es que se utiliza un algoritmo con crecimiento cuadrático, aumentar la velocidad del hardware solamente proporciona una mejora limitada mientras la cantidad de registros continúa creciendo.

Un ejemplo propio sería un sistema de una tienda que debe ordenar **500.000 productos por precio antes de generar un catálogo que debe publicarse a las 6:00 a. m.** Si se utiliza un algoritmo correcto pero con complejidad Θ(n²), el sistema podría generar correctamente el catálogo, pero no terminar a tiempo. En este caso, cumplir con el resultado no es suficiente porque también existe una restricción de tiempo.

Por lo tanto, en Tamiza se debe buscar una solución que sea correcta y, además, suficientemente eficiente para procesar grandes cantidades de registros dentro de la ventana establecida.

---

# Parte 2 — Responsabilidad ambiental y ética

La eficiencia de un algoritmo también tiene relación con el consumo de recursos tecnológicos. Cuando un algoritmo tarda más tiempo, el procesador y los demás componentes del sistema permanecen trabajando durante un período mayor. Si este proceso se ejecuta diariamente, el consumo adicional puede acumularse con el tiempo.

Un primer perjuicio concreto es el **mayor consumo de energía eléctrica**. Si el procesamiento tarda más debido a una elección algorítmica poco eficiente, los servidores deben permanecer ejecutándose durante más tiempo. El costo directo de este consumo lo asumiría la organización responsable de la plataforma.

Un segundo perjuicio es el **incremento innecesario de los costos de infraestructura**. Una organización podría intentar compensar un algoritmo poco eficiente comprando servidores más potentes. Esto representa una inversión que puede ser innecesaria si el problema de fondo se encuentra en el algoritmo. En el caso de una plataforma de una entidad pública, este costo puede afectar los recursos disponibles para otros servicios.

También existe un perjuicio relacionado con la confiabilidad del sistema. Si el proceso no termina dentro de la ventana de cuatro horas, pueden quedar registros sin procesar o generar una lista incompleta. Esto puede afectar directamente a las personas que esperan ser contactadas.

La situación tiene además una dimensión ética porque el orden de la lista determina **a quién se llama primero**. Los registros con un mayor índice de riesgo deben recibir prioridad. Por esta razón, una falla que afecte el orden o impida terminar el proceso puede provocar que una persona con mayor riesgo sea atendida después de otra con menor prioridad.

Por lo tanto, la responsabilidad del equipo de desarrollo no consiste únicamente en producir un algoritmo que funcione. También debe considerar el uso responsable de los recursos, el impacto ambiental acumulado y las consecuencias que una decisión técnica puede generar sobre las personas.

---

# Parte 3 — Casos de entrada e instrumentación

## Código utilizado

La implementación de los algoritmos se encuentra en [algoritmos.py](algoritmos.py), mientras que los generadores de los escenarios se encuentran en [datos.py](datos.py).

El experimento completo de esta parte se encuentra en [parte3_casos.py](parte3_casos.py).

---

## 3.1 Mejor, peor y promedio caso

Para un tamaño de entrada fijo `n`, el **mejor caso** corresponde a la entrada que necesita la menor cantidad de operaciones o comparaciones para ser procesada.

El **peor caso** corresponde a la entrada que necesita la mayor cantidad de operaciones o comparaciones.

El **caso promedio** corresponde al comportamiento esperado al considerar las diferentes entradas posibles de tamaño `n`. No significa simplemente tomar el punto medio entre el mejor y el peor caso, sino analizar el costo esperado sobre las entradas posibles.

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

Por lo tanto, existen aproximadamente `log₂(n)` niveles y cada uno cuesta `Θ(n)`.

Entonces:

**T(n) = Θ(n) + Θ(n) + ... + Θ(n)**

con `log₂(n)` niveles.

Por lo tanto:

**T(n) = Θ(n log n)**

Así, la complejidad temporal de `merge_sort` es:

**Mejor caso: Θ(n log n)**
**Caso promedio: Θ(n log n)**
**Peor caso: Θ(n log n)**

---

## Complejidad de Insertion Sort línea por línea

`insertion_sort` recorre los elementos desde el segundo elemento hasta el último.

El ciclo externo realiza:

**n - 1**

iteraciones.

### Mejor caso

Cuando los datos ya están ordenados de acuerdo con el criterio requerido, el ciclo `while` realiza solamente una comparación entre elementos en cada iteración.

Por lo tanto:

**1 + 1 + 1 + ... + 1**

para `n - 1` elementos.

Entonces:

**T(n) = n - 1**

y:

**T(n) = Θ(n)**

### Peor caso

Cuando los datos están en orden inverso, para el segundo elemento se realiza una comparación, para el tercero dos comparaciones, para el cuarto tres, y así sucesivamente.

La cantidad total es:

**1 + 2 + 3 + ... + (n - 1)**

Utilizando la fórmula de la suma:

**n(n - 1) / 2**

Desarrollando:

**(n² - n) / 2**

El término dominante es `n²`, por lo que:

**T(n) = Θ(n²)**

### Caso promedio

En promedio, cada elemento debe compararse con una cantidad proporcional a los elementos que ya fueron procesados. Por lo tanto, el crecimiento promedio también es cuadrático:

**T(n) = Θ(n²)**

### Tabla de complejidades

| Algoritmo      | Mejor caso | Caso promedio | Peor caso  |
| -------------- | ---------- | ------------- | ---------- |
| Insertion Sort | Θ(n)       | Θ(n²)         | Θ(n²)      |
| Merge Sort     | Θ(n log n) | Θ(n log n)    | Θ(n log n) |

---

## 4.2 Resultados experimentales de tiempo

Se utilizaron los mismos tamaños para ambos algoritmos y el escenario aleatorio:

| Tamaño `n` | Insertion Sort (s) | Merge Sort (s) |
| ---------: | -----------------: | -------------: |
|        100 |           0.000244 |       0.000166 |
|        200 |           0.000921 |       0.000344 |
|        400 |           0.003771 |       0.000753 |
|        800 |           0.015894 |       0.001673 |
|      1.600 |           0.065387 |       0.003601 |
|      3.200 |           0.259574 |       0.007969 |
|      6.400 |           1.074403 |       0.016237 |

La curva de **Insertion Sort** aumenta rápidamente a medida que crece `n`. Para `n = 6400` alcanza **1.074403 segundos**.

La curva de **Merge Sort** presenta un crecimiento mucho más lento. Para `n = 6400` alcanza solamente **0.016237 segundos**.

La diferencia entre ambos algoritmos aumenta con el tamaño de entrada. En la última medición, `merge_sort` fue aproximadamente:

**1.074403 / 0.016237 ≈ 66,2 veces más rápido**

que `insertion_sort`.

![Comparación de tiempos entre insertion sort y merge sort](graficas/parte4_tiempo.png)

Los resultados experimentales coinciden con el análisis teórico. `insertion_sort` tiene comportamiento Θ(n²) en promedio y peor caso, por lo que su curva crece rápidamente. `merge_sort`, con comportamiento Θ(n log n), presenta una curva mucho más favorable para entradas grandes.

Por lo tanto, para el escenario de Tamiza, **merge_sort es el algoritmo más apropiado de los dos**.

Las pequeñas diferencias observadas en tamaños pequeños pueden estar relacionadas con factores externos al algoritmo, como procesos del sistema operativo, administración de memoria y costos internos de Python. Al aumentar el tamaño de entrada, la diferencia causada por la complejidad algorítmica se vuelve más evidente.

---

# Parte 4.3 — Concepto técnico para el equipo de ingeniería

Para la plataforma Tamiza se recomienda utilizar **merge_sort** en lugar de `insertion_sort` para ordenar los registros de riesgo.

La principal razón es la diferencia de complejidad. `insertion_sort` presenta Θ(n²) en el caso promedio y en el peor caso, mientras que `merge_sort` mantiene Θ(n log n) en los tres casos. Esta diferencia resulta especialmente importante porque la plataforma debe procesar aproximadamente **1.200.000 registros** dentro de una ventana estricta de cuatro horas.

Las mediciones realizadas permiten observar esta diferencia incluso con una cantidad de datos mucho menor. Para `n = 6400`, `insertion_sort` tardó **1.074403 segundos**, mientras que `merge_sort` tardó **0.016237 segundos**. Por lo tanto, en esta medición `merge_sort` fue aproximadamente **66,2 veces más rápido**.

A partir del dato medido de `n = 6400`, se puede realizar una estimación del comportamiento para 1.200.000 registros. Para `insertion_sort`, tomando el comportamiento Θ(n²):

**T(1.200.000) ≈ 1.074403 × (1.200.000 / 6.400)²**

**T(1.200.000) ≈ 37.771,98 segundos**

Esto corresponde aproximadamente a:

**10,49 horas**

Por lo tanto, esta extrapolación indica que `insertion_sort` podría superar ampliamente la ventana disponible de cuatro horas.

Para `merge_sort`, utilizando su comportamiento Θ(n log n):

**T(1.200.000) ≈ 0.016237 × (1.200.000 / 6.400) × (log₂(1.200.000) / log₂(6.400))**

La estimación resultante es aproximadamente:

**4,86 segundos**

Estos valores son **estimaciones por extrapolación y no mediciones directas**, porque el experimento realizado solamente llegó hasta 6400 registros. Una prueba con 1.200.000 registros sería necesaria para conocer el comportamiento real bajo condiciones de producción.

Respecto a la propuesta de comprar un servidor con el doble de velocidad, los resultados muestran que el problema no debería solucionarse únicamente aumentando la capacidad del hardware. Incluso si el servidor redujera aproximadamente a la mitad los tiempos de ejecución, `insertion_sort` seguiría teniendo un crecimiento Θ(n²). En cambio, `merge_sort` cambia el comportamiento asintótico a Θ(n log n), lo cual representa una mejora estructural.

Una consideración adicional al tiempo es el **uso de memoria**. `merge_sort` necesita memoria adicional para realizar la combinación de las partes, mientras que `insertion_sort` utiliza poca memoria adicional. Sin embargo, para el volumen de datos de Tamiza, la reducción del tiempo de ejecución resulta más importante que esta desventaja, siempre que la infraestructura disponga de memoria suficiente.

También se debe considerar el **mantenimiento y el riesgo operativo**. Un algoritmo con mejor complejidad permite que el sistema sea menos dependiente de futuras ampliaciones de hardware y ofrece un comportamiento más predecible cuando aumente la cantidad de registros. Esto disminuye el riesgo de que el procesamiento supere la ventana nocturna.

Por estas razones, la recomendación técnica es **implementar `merge_sort`** y posteriormente realizar una prueba de carga con un volumen de datos cercano al real. El aumento de capacidad del servidor puede complementar la solución, pero no debería utilizarse como sustituto de una mejora algorítmica.

---

# Conclusión general

El laboratorio permitió comprobar la importancia de analizar tanto la corrección como la eficiencia de un algoritmo antes de implementarlo en un sistema real.

En la Parte 3 se comprobó que `insertion_sort` depende considerablemente del orden inicial de los datos. Para `n = 6400`, el escenario casi ordenado necesitó solamente **10.277 comparaciones y 0.001209 segundos**, mientras que el escenario inverso necesitó **20.476.800 comparaciones y 2.106491 segundos**.

Los resultados coinciden con la teoría: `insertion_sort` tiene un mejor caso de Θ(n), pero un caso promedio y peor caso de Θ(n²).

En la Parte 4, la comparación entre ambos algoritmos mostró una ventaja clara para `merge_sort`. Para `n = 6400`, `insertion_sort` tardó **1.074403 segundos**, mientras que `merge_sort` tardó **0.016237 segundos**, siendo aproximadamente 66,2 veces más rápido en esta prueba.

La complejidad teórica explica esta diferencia: `insertion_sort` crece de manera cuadrática, mientras que `merge_sort` crece como Θ(n log n).

La extrapolación realizada para 1.200.000 registros también muestra por qué la elección del algoritmo es importante. Bajo las hipótesis utilizadas, `insertion_sort` podría tardar aproximadamente 10,49 horas, superando la ventana de cuatro horas, mientras que `merge_sort` tendría una estimación de aproximadamente 4,86 segundos. Estas cifras son estimaciones y deben validarse mediante una prueba de carga real.

En conclusión, para Tamiza se recomienda utilizar **merge_sort** y realizar pruebas adicionales con un volumen de datos cercano al de producción. La mejora algorítmica debe ser la principal estrategia y el aumento de capacidad del servidor debe considerarse como un complemento.
