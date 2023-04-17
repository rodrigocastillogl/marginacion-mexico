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

## Índice de Marginación

Es preciso emplear métodos de análisis multivariado y reducción de dimensionalidad. El objetivo último es una medición resultante única derivada de alguna
forma de agregación de los indicadores. El CONAPO construye una medida denominada *Indice de Marginación* (IM), que permite identificar las disparidades
socio-económicas relevante como herramienta analítica y operativa para la definición y focalización de políticas públicas.

El IM se construye empleando el método de distancia de Pena-Trapero (conocido como método ${DP}_2$); se define:

$$IM = \sum_{j=1}^n \frac{d_{ij}}{\sigma_j} \left( 1 - R^2_{j,j-1,..., 1} \right)$$

donde $d_{ij} = |I_j^i - I_j^r|$ es la distancia en la $j$-ésima variable (indicador) del municipio $i$ respecto a la referencia $I^r = (I_1^r, I_2^r, ...)$ , 
$\sigma_j$ es la desviación estándar de la $j$-ésima variable y $R^2_i$ es el coeficientecde determinación de la regresión del indicador $I_j$ con respecto
a los otros indicadores ($I_{j−1}$, $I_{j−2}$, ..., $I_1$).

Luego de la obtención del IM, los valores se clasificaron con el método de Dalenius y Hodges para obtener el grado de marginación (GM). Se clasifican en cinco
categorías ordinales: muy bajo, bajo, medio, alto, muy alto.

## Descripción de los datos

En la Figura se muestra el *Pairsplot* de los 9 indicadores de pobreza. Se observa que, en la mayoría de los casos (excepto para el indicador `PL500`), las distribuciones
estimadas exhiben un comportamiento unimodal. Se puede ver que en algunos indicadores como `SBASC` y `VHAC`, la distribución estimada es bastante simétrica, mientras que
en otros casos existe, aunque no de manera muy notable, cierta asimetría. en las distribuciones de los indicadores. Haremos entonces, supuestos de normalidad y adelante
se aplicará PCA.

![Table 1](https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/pairsplot.png)

En la Tabla se muestran 7 estadísticas que resumen los indicadores de pobreza a nivel municipal. Existen diferencias significativas entre la variabilidad de algunos
indicadores, esto se puede ver también en los *Boxplots*. Es por esto que se estandarizan los indicadores (media igual a cero y desviación estándar igual a 1); esto es
muy importante para PCA, donde los indicadores con una variabilidad alta pueden opacar a otros indicadores.

![Table 1](https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/table.png)

![Boxplot](https://github.com/rodrigocastillogl/marginacion_mexico/blob/main/imgs/boxplot.png)
 
## Análisis de datos