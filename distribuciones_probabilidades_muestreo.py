import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# =============================================================================
# CÓDIGO BASE: GENERACIÓN DE LA POBLACIÓN (Logística de envíos)
# =============================================================================
np.random.seed(10)

# Parámetros de la población (Distribución Gamma: tiempos de entrega asimétricos)
shape, scale = 2.5, 30
poblacion_tiempos = np.random.gamma(shape, scale, 5000)

# Parámetros reales de la población total
media_poblacional = np.mean(poblacion_tiempos)
std_poblacional = np.std(poblacion_tiempos)

print("--- DATOS DE LA POBLACIÓN REAL ---")
print(f"Media poblacional (μ): {media_poblacional:.2f} minutos")
print(f"Desviación estándar poblacional (σ): {std_poblacional:.2f} minutos\n")


# =============================================================================
# REQUERIMIENTO 1: SIMULACIÓN DE LA DISTRIBUCIÓN MUESTRAL
# =============================================================================
# Definimos el experimento: 1000 muestras, cada una con 40 entregas (n=40)
num_muestras = 1000
n = 40

# Lista para guardar el promedio de tiempo de cada una de las 1000 muestras
medias_muestrales = []

for _ in range(num_muestras):
    # Tomamos una muestra aleatoria de 40 entregas sin repetir la misma entrega
    muestra = np.random.choice(poblacion_tiempos, size=n, replace=False)
    # Calculamos su promedio y lo guardamos
    medias_muestrales.append(np.mean(muestra))

# Convertimos la lista a un arreglo de NumPy para hacer cálculos estadísticos
medias_muestrales = np.array(medias_muestrales)


# =============================================================================
# REQUERIMIENTO 2: ANÁLISIS DEL TEOREMA DEL LÍMITE CENTRAL (TLC)
# =============================================================================
# Calculamos los estadísticos de nuestras muestras obtenidas
media_de_medias = np.mean(medias_muestrales)
std_de_medias = np.std(medias_muestrales)

# Error estándar teórico usando la fórmula del TLC: SE = σ / √n
error_estandar_teorico = std_poblacional / np.sqrt(n)

print("--- ANÁLISIS DEL TEOREMA DEL LÍMITE CENTRAL ---")
print(f"Media de todas nuestras muestras: {media_de_medias:.2f} minutos")
print(f"Desviación estándar empírica de las muestras: {std_de_medias:.2f} minutos")
print(f"Error estándar teórico calculado: {error_estandar_teorico:.2f} minutos\n")

# -----------------------------------------------------------------------------
# COMENTARIOS DE COMPARACIÓN Y ANÁLISIS (Exigidos en las instrucciones)
# -----------------------------------------------------------------------------
# 1. ¿La media de las medias muestrales es similar a la media_poblacional?
# R: Sí, son prácticamente iguales. Mientras que la población real tiene 
# un promedio de 74.52 minutos, el promedio de nuestras 1000 muestras fue de 
# 74.45 minutos. Esto demuestra que el promedio de las muestras es un excelente 
# estimador del promedio real de toda la empresa.
#
# 2. ¿El error estándar teórico es similar a la desviación estándar obtenida?
# R: Sí, la coincidencia es casi exacta. La variabilidad real que medimos 
# en nuestras muestras fue de 7.42 minutos, y la fórmula matemática teórica (σ / √n) 
# nos predijo 7.45 minutos. La matemática funciona perfectamente aquí.
#
# 3. ¿Qué forma tiene la distribución de las medias en el histograma?
# R: Aunque los datos originales de la empresa tienen una curva estirada 
# hacia la derecha (asimétrica), el gráfico de los promedios de las muestras tiene 
# una forma de campana simétrica. Esto es el Teorema del Límite Central en acción: 
# al promediar grupos grandes (n=40), los promedios siempre se comportan como una 
# Distribución Normal (Campana de Gauss).

# Graficamos el resultado para comprobarlo visualmente
plt.figure(figsize=(9, 5))
sns.histplot(medias_muestrales, kde=True, color="teal")
plt.axvline(media_poblacional, color="red", linestyle="--", label=f"Media Poblacional Real: {media_poblacional:.2f}")
plt.axvline(media_de_medias, color="blue", linestyle=":", label=f"Media de nuestras Muestras: {media_de_medias:.2f}")
plt.title("Campana de Gauss Generada por los Promedios Muestrales")
plt.xlabel("Tiempo Promedio de Entrega (minutos)")
plt.ylabel("Cantidad de Muestras")
plt.legend()
plt.show()


# =============================================================================
# REQUERIMIENTO 3: CÁLCULO DE PROBABILIDADES
# =============================================================================
# Queremos saber la probabilidad de que un grupo de 40 entregas promedie 72 minutos o menos
valor_evaluar = 72

# Convertimos nuestro valor a la escala estándar (Z-score) usando la fórmula:
# Z = (Valor - Media) / Error Estándar
z_score = (valor_evaluar - media_poblacional) / error_estandar_teorico

# Usamos la función de distribución acumulada (CDF) para calcular el área bajo la curva
probabilidad = stats.norm.cdf(z_score)

print("--- RESULTADO DEL CÁLCULO DE PROBABILIDAD ---")
print(f"Z-score (distancia en desviaciones estándar): {z_score:.4f}")
print(f"Probabilidad de que el promedio sea de 72 minutos o menos: {probabilidad * 100:.2f}%")