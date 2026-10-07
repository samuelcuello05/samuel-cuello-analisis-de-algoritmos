# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Samuel Cuello · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-07 23:59 · **Versión revisada:** commit `2c564bf`

Muy buen trabajo: un informe completo, con argumentos apoyados en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 24 / 25 |
| Calidad de la explicación teórica | 24 / 25 |
| Corrección de la implementación | 19 / 20 |
| Calidad del análisis de las gráficas | 19 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **95 / 100** |
| **Nota (0–5)** | **4.75** |

## 1. Corrección conceptual (24 / 25)
**Lo que hizo bien:**
- Distingue entre que el resultado sea correcto y que llegue dentro de las cuatro horas, y nombra la ventana como la restricción que se incumple.
- Explica con números por qué un servidor el doble de rápido no basta: solo permite ordenar unas 1,41 veces más registros, mientras que los datos crecieron 60 veces.
- Da un segundo ejemplo propio (500.000 productos para un catálogo a las 6:00 a. m.), con datos y restricción.
- Relaciona el tiempo con la energía usando un supuesto declarado (400 W) y muestra cómo se acumula noche tras noche durante años.
- Describe perjuicios concretos (el paciente con riesgo 950, el operador, el equipo de desarrollo) e indica en cada uno quién asume el costo.
- Explica que, como el orden decide a quién se llama primero, no basta con que sea rápido: debe ser exacto y verificado.

**Lo que puede mejorar:**
- El segundo ejemplo (el catálogo) dice que el algoritmo cuadrático no terminaría a tiempo, pero no estima cuánto tardaría; un número aproximado lo haría más sólido.

## 2. Calidad de la explicación teórica (24 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio caso con un `n` fijo y dice sobre qué se toma cada uno. Justifica que usaría el peor caso por la ventana estricta.
- Escribe la predicción antes de medir y la contrasta con los resultados.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y resuelve el árbol nivel por nivel, con el número de niveles, las hojas y la suma total hasta `Θ(n log n)`.
- Calcula insertion sort línea a línea: cuántas veces se ejecuta cada línea, la suma de costos y el resultado para mejor, peor y promedio caso.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- La tabla de líneas usa una notación algo pesada (`dᵢ`, `bᵢ`). Un pequeño ejemplo numérico con una lista corta la haría más fácil de seguir.

## 3. Corrección de la implementación (19 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida y cuentan solo comparaciones entre elementos. No usa `sorted()` ni `sort()`, y la mezcla de `merge_sort` es propia y recursiva.
- Los tres generadores dan listas de tamaño `n` con valores distintos y la semilla hace los resultados repetibles.
- Todas las funciones tienen tipos y descripciones con Args y Returns.

**Lo que puede mejorar:**
- En `generar_casi_ordenado` queda una variable (`cantidad_restante`) que se calcula y nunca se usa.
- En `merge_sort`, al sumar las comparaciones, el operador `+` queda al inicio de la línea; es un detalle menor de estilo.

## 4. Calidad del análisis de las gráficas (19 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos el inverso como peor caso, el casi ordenado como mejor y el aleatorio como el más cercano al promedio (la mitad del peor), y lo contrasta con su predicción.
- Describe lo que hace cada curva y lo une con `Θ(n²)` y `Θ(n log n)`, y explica por qué las curvas casi se tocan con pocos datos.
- El concepto técnico recomienda `merge_sort` como única implementación, justifica el criterio con una tabla de los tres escenarios, responde sobre el servidor citando gráfica y tamaño, y estima la ventana de cuatro horas declarando que es una estimación.
- Discute la memoria adicional y la estabilidad.

**Lo que puede mejorar:**
- La estimación para 1.200.000 registros parte de una sola medición en `n = 6400`. Podría apoyarse también en mediciones de varios tamaños y decir qué tan segura es.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos coinciden con lo pedido, y las gráficas están incrustadas con rutas que funcionan.
- Cada parte práctica enlaza su código, y hay instrucciones claras para reproducir.
- Hay once commits con mensajes descriptivos.

**Lo que puede mejorar:**
- Siete de esos commits quedaron con la misma hora exacta, así que no muestran el avance real. Haga commits a medida que trabaja.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente, los scripts corren sin errores y generan las tres gráficas.

## Para el próximo laboratorio
- Haga commits pequeños a lo largo del trabajo, para que el historial refleje el avance.
- Cuando dé un segundo ejemplo, agregue una estimación aproximada de cuánto tardaría.
- Apoye las extrapolaciones en varios tamaños medidos y diga qué tan confiables son.
- Revise el código en busca de variables que no se usan.
