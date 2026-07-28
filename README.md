# Desafio: Distribuciones de Probabilidad y Muestreo
(Nota: sin tildes ni caracteres especiales)
Este repositorio contiene la resolucion del desafio enfocado en la demostracion del Teorema del Limite Central (TLC) y el calculo de probabilidades aplicadas al analisis de tiempos de entrega en un entorno de logistica nacional.

---

## Descripcion del Proyecto

En operaciones logisticas, los tiempos de entrega individuales suelen presentar alta variabilidad y distribuciones no normales (asimetricas), influenciadas por factores como el trafico, el clima o la carga operativa. 

El objetivo de este proyecto es demostrar empiricamente como, al agrupar observaciones en muestras de tamaño suficiente (n = 40), la distribucion de las medias muestrales converge hacia una Distribucion Normal, lo que permite predecir comportamientos operativos y calcular probabilidades de cumplimiento de metas de servicio con base cientifica.

---

## Requerimientos y Metodologia

El proyecto aborda los siguientes tres ejes fundamentales:

1. Simulacion de la Distribucion Muestral:
   - Generacion de una poblacion sintetica de N = 5000 entregas mediante una distribucion Gamma (shape = 2.5, scale = 30).
   - Extraccion de 1000 muestras aleatorias de tamaño n = 40.
   - Almacenamiento y calculo de la media para cada muestra (medias_muestrales).

2. Analisis del Teorema del Limite Central (TLC):
   - Comparacion de la media de medias muestrales frente a la media poblacional.
   - Comparacion de la desviacion estandar empirica de las muestras frente al Error Estandar teorico (SE = sigma / sqrt(n)).
   - Visualizacion de la convergencia hacia la curva Normal mediante histogramas y curvas de densidad (KDE).

3. Calculo de Probabilidades:
   - Estandarizacion del valor objetivo (72 minutos) mediante la metrica Z-score.
   - Calculo de la probabilidad acumulada P(X_bar <= 72) utilizando la funcion de distribucion acumulada (CDF) de la distribucion normal estandar.

---

## Requisitos e Instalacion

Para ejecutar este codigo de forma local, asegurate de contar con Python 3.8+ y las siguientes bibliotecas instaladas:

```bash
pip install pandas numpy matplotlib seaborn scipy
