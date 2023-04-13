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
forma de agregación de los indicadores. El CONAPO construye una medida denominada *Indice de Marginación* (IM). El IM permite identificar las disparidades
socio-económicas existentes en un momento determinado, relevante como herramienta analítica y operativa para la definición y focalización de políticas públicas.

## Descripción de los datos

En la tabla se muestran 7 estadísticas que resumen los indicadores de pobreza a nivel municipal. Existen diferencias significativas entre la variabilidad de algunos
indicadores, esto se puede verificar en los Boxplots. Es por esto que se estandarizan los indicadores (media igual a cero y desviación estándar igual a 1); esto es
muy importante para PCA, donde los indicadores con una variabilidad alta pueden opacar a otros indicadores.

![image](./imgs/table.pdf?raw=true)