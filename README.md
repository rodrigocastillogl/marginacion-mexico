# Análisis de Datos de marginación en México

## Introducción

En este trabajo se presenta una exploración y análisis de datos de indicadores de pobreza de México en el año 2020 (Dados por municipio).
Se brinda una descripción del enfoque utilizado para abordar el problema de definición de la calidad de vida y una descripción de los indicadores involucrados en el estudio.
Adicionalmente, se propone un índice de marginación basado en Análisis de Componentes Principales (PCA) y se compara con el índice calculado por el Consejo Nacional de la Población (CONAPO).
Por último, se utilizan método de agrupamiento para observar patrones en la marginación a nivel nacional y posiblemente asignar una medida de calidad de vida.

## Indicadores

Los nueve indicadores considerados por la CONAPO (y accesibles en su [sitio web](https://www.gob.mx/conapo/documentos/indices-de-marginacion-2020-284372)), 
corresponden a nueve formas de marginación en las dimensiones: educación, vivienda, distribución de la población e ingresos monetarios, y son los siguientes:

1. Porcentaje de la población analfabeta de 15 años o más (`ANALF`).
2. Porcentaje de la población de 15 años o más sin educación básica (`SBASC`).
3. Porcentaje de la población que habita en viviendas particulares sin drenaje ni sanitario (`OVSDE`).
4. Porcentaje de la población que habita en viviendas particulares sin energía eléctrica (`OVSEE`).
5. Porcentaje de la población que habita en viviendas particulares sin agua entubada (`OVSAE`).
6. Porcentaje de la población que habita en viviendas particulares con piso de tierra (`OVPT`).
7. Porcentaje de la población que habita en viviendas particulares con hacinamiento (`VHAC`).
8. Población en localidades con menos de 5000 habitantes (`PL5000`).
9. Población ocupada con ingresos menores a 2 salarios mínimos (`PO2SM`).


## Descripción de los datos

En la Figura se muestra el *Pairsplot* de los 9 indicadores de pobreza. Se observa que, en la mayoría de los casos (excepto para el indicador `PL500`), las distribuciones
estimadas exhiben un comportamiento unimodal. Se puede ver que en algunos indicadores como `SBASC` y `VHAC`, la distribución estimada es bastante simétrica, mientras que
en otros casos existe, aunque no de manera muy notable, cierta asimetría en las distribuciones de los indicadores. Haremos entonces, supuestos de normalidad y adelante
se aplicará PCA.

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/pairsplot.png" width = 70% height = 70%>
</p>

En la Tabla se muestran 7 estadísticas que resumen los indicadores de pobreza a nivel municipal. Existen diferencias significativas entre la variabilidad de algunos
indicadores, esto se puede ver también en los *Boxplots*. Es por esto que se estandarizan los indicadores (media igual a cero y desviación estándar igual a 1); esto es
muy importante para PCA, donde los indicadores con una variabilidad alta pueden opacar a otros indicadores.

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/table.png" width = 80% height = 80%>
</p>

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/boxplot.png" width = 70% height = 70%>
 </p>

 ## Índice de Marginación

Es preciso emplear métodos de análisis multivariado y reducción de dimensionalidad. El objetivo último es una medición resultante única derivada de alguna
forma de agregación de los indicadores. El CONAPO construye una medida denominada *Indice de Marginación* (IM), que permite identificar las disparidades
socio-económicas relevante como herramienta analítica y operativa para la definición y focalización de políticas públicas.

El IM se construye empleando el método de distancia de Pena-Trapero (conocido como método ${DP}_2$); se define:

$$IM = \sum_{j=1}^d \frac{d_{ij}}{\sigma_j} \left( 1 - R^2_{j,j-1,..., 1} \right)$$

donde $d_{ij} = |I_j^i - I_j^r|$ es la distancia en la $j$-ésima variable (indicador) del municipio $i$ respecto a la referencia $I^r = (I_1^r, I_2^r, ...)$ , 
$\sigma_j$ es la desviación estándar de la $j$-ésima variable y $R^2_{j,j-1,..., 1}$ es el coeficientecde determinación de la regresión del indicador $I_j$ con respecto
a los otros indicadores ($I_{j−1}$, $I_{j−2}$, ..., $I_1$).

Luego de la obtención del IM, los valores se clasificaron con el método de Dalenius y Hodges para obtener el grado de marginación (GM). Se clasifican en cinco
categorías ordinales: muy bajo, bajo, medio, alto, muy alto.

## Análisis de datos

### Análisis de Componentes Principales

En PCA transformamos linealmente un conjunto de $d$ variables correlacionadas en otro conjunto de $p$ variables no correlacionadas (con $p \leq d$); esto a
partir de los valores y vectores propios de la matriz de correlación. La siguiente Tabla muestra los valores propios (varianza de los componentes) y la
varianza explicada; gran parte de la variabilidad de los datos se encuentra en su proyección de los datos en los 2 primeros CP.

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/table_pca.png" width = 60% height = 60%>
</p>

La siguiente Figura muestra la proyección de los datos los dos primeros CP; se despliegan clasificados según el GM generado por el CONAPO. Podemos observar que las fronteras
de clasificación (a pesar de no ser del todo distinguibles) marcan intervalos a lo largo del primer CP, con una ligera inclinación en orientación al segundo CP.

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/plot_pca.png" width = 80% height = 80%>
</p>

### Índice de Marginación basado en PCA

Proyectar los datos en uno de los CP es una suma pondera de los indicadores. Así, para el primer CP se puede considerar un índice de marginación sintético dado por:

$$A_1^i = - \sum_{j=1}^d \alpha_{1j} I_j^i$$

donde $A_j^i$ es el índice sintético calculado para el $i$-ésimo municipio usando su proyección en el primer componente principal, $α_{1j}$ es el valor de la $j$-ésima
coordenada del primer CP y $I_j^i$ es el valor del $j$-ésimo indicador para el $i$-ésimo municipio.

El mismo procedimiento se puede emplear para calcular $A_2^i$, $A_3^i$, ..., $A_9^i$ correspondientes a los otros CP. Es posible hacer una suma ponderada sobre estos
índices $A_k^i$ para $k = 1, 2, ..., m$, siendo el $m$ el número de CP usados. Los pesos de la ponderación están dados por la fracción de varianza explicada de
cada CP ($\lambda_k$). Definimos entonces un índice sintético basado en PCA como:

$${IM}^i_{PCA} \ = \ \sum_{k=1}^m \lambda_k A_k^i \ = \ - \sum_{k=1}^m \lambda_k \left( \sum_{j=1}^d \alpha_{kj} I_j^i \right)$$

Este índice se calculó para todos los municipios utilizando dos CP ($m = 2$). El índice basado en PCA muestra una correspondencia fuertemente lineal con el índice basado en
distancia ${DP}_2$ ($R = 0.996$, véase la siguiente Figura).

<p align="center">
<img src = "https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/comparison.png" width = 80% height = 80%>
</p>


## Conclusiones

* Se observa que los valores del primer CP son casi constantes (suma ponderada con el mismo peso en todos los indicadores), por lo que la proyección de
cada observación sobre el primer CP se puede interpretar como un promedio de los indicadores de un municipio particular.

* También, la proyección de los datos sobre el segundo componente principal se puede interpretar como una medida de contraste o diferencia entre el promedio de los indicadores `OVSDE`, `OVSEE` e `OVSAE` (servicios en vivienda: drenaje, electricidad y agua) y el promedio de los indicadores `SBASC`,`PL5000` e `PO2SM` (nivel de escolaridad e ingresos).

* El índice de marginación basado en PCA muestra una correspondencia fuertemente lineal con el índice $IM$ propuesto por CONAPO.
