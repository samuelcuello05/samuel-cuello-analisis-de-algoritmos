# Retroalimentación — Fundamentos, complejidad y recurrencias

**Estudiante:** Samuel Cuello · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `fc1feba`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 25 |
| Calidad de la explicación teórica | 18 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **74 / 100** |
| **Nota (0–5)** | **3.70** |

## 1. Corrección conceptual (18 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que se produzca dentro de las cuatro horas, y nombra la ventana como la restricción que se incumple.
- Explica que un servidor el doble de rápido no cambia el crecimiento cuadrático del algoritmo.
- Da un segundo ejemplo propio (500.000 productos para un catálogo a las 6:00 a. m.), con datos y restricción.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- Para cada perjuicio hay que decir con claridad quién asume el costo. En el de la lista incompleta nombra a las personas que esperan la llamada, pero no dice si el costo lo asume el paciente, el operador, la Secretaría o el equipo de desarrollo.
- Los perjuicios que describe son sobre todo de energía y dinero. Falta un caso concreto de una persona afectada (por ejemplo, un paciente de alto riesgo que recibe la llamada tarde).
- Falta explicar mejor por qué el consumo de energía crece al repetirse todas las madrugadas durante años, y qué obligación adicional impone que el orden sea exacto, no solo rápido.

## 2. Calidad de la explicación teórica (18 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio caso con un tamaño `n` fijo, y justifica que usaría el peor caso por la ventana estricta.
- Escribió la predicción antes de medir y la contrastó con los resultados.
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica cada término y desarrolla el árbol nivel por nivel hasta `Θ(n log n)`.
- Incluye la tabla de complejidades por caso.

**Lo que puede mejorar:**
- El cálculo de insertion sort no es línea a línea: debía indicar cuántas veces se ejecuta cada línea de su código y sumar esos costos. Lo hizo contando comparaciones por caso.
- El caso promedio se afirma como cuadrático sin mostrar por qué (en promedio cada elemento se mueve la mitad del camino).
- En el árbol faltó escribir explícitamente el costo total como suma de niveles (`n` por `log n`) con el número de hojas.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida y cuentan solo comparaciones entre elementos. No usa `sorted()` ni `sort()`.
- Los tres generadores dan listas de tamaño `n` con valores distintos y usan semilla.

**Lo que puede mejorar:**
- Varias funciones (`medir_escenario`, `medir_algoritmo`, las que grafican y `merge_sort_recursivo`) no tienen todos los tipos indicados y sus descripciones no siguen el formato Google (Args y Returns).
- Detalles de estilo: falta una línea en blanco entre funciones en `algoritmos.py` y falta salto de línea al final de los archivos.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes con unidades y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con datos el inverso como peor caso, el casi ordenado como mejor y el aleatorio como intermedio.
- Describe lo que hace cada curva en la comparación y la une con `Θ(n²)` y `Θ(n log n)`.
- Extrapola a 1.200.000 registros con su razonamiento y declara que es una estimación.

**Lo que puede mejorar:**
- En 4.3 falta resolver el compromiso que pide el caso: el canal de entrada puede cambiar sin aviso y no quieren tres implementaciones. Debía explicar por qué una sola, `merge_sort`, resuelve eso.
- Al responder sobre el servidor del doble de velocidad, cite la gráfica y el tamaño de la que tomó el dato.
- No explica por qué los tiempos de las curvas pequeñas casi se tocan; la explicación genérica sobre "factores externos" no se apoya en lo que mide.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- La carpeta y los archivos coinciden con lo pedido, y las gráficas están incrustadas con rutas que funcionan.
- Cada parte práctica enlaza su código y hay instrucciones para reproducir.

**Lo que puede mejorar:**
- Los siete commits del laboratorio quedaron con la misma hora, así que no muestran el avance real. Haga commits a medida que trabaja.

## ¿El código funciona?
Sí. Los dos algoritmos ordenan correctamente y los scripts corren sin errores y generan las gráficas.

## Para el próximo laboratorio
- Indique siempre quién asume el costo de cada perjuicio y dé un ejemplo de una persona concreta afectada.
- Cuando se pida un análisis línea a línea, escriba cuántas veces se ejecuta cada línea del código y sume.
- Agregue tipos y descripciones completas (Args, Returns) a todas las funciones.
- En el concepto técnico, responda cada punto de la consulta, incluida la incertidumbre del canal de entrada.
- Haga commits pequeños a lo largo del trabajo.
