# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j8vIw9I-NCmuk1MWvSylJgSYyZRNDEit
"""

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    """
    suma = 0
    for valor in numeros:
        suma += valor
    resultado_promedio = suma / len(numeros)
    return resultado_promedio

def obtener_mediana(numeros):
    """
    Obtiene la mediana de una lista de números.
    """
    numeros = sorted(numeros)
    cantidad = len(numeros)
    if cantidad % 2 == 0:
        central = []
        valor1 = numeros[(cantidad // 2) - 1]
        valor2 = numeros[cantidad // 2]
        central.append(valor1)
        central.append(valor2)
        resultado_mediana = int(calcular_promedio(central))
    else:
        resultado_mediana = numeros[(cantidad // 2)]
    return resultado_mediana

def calcular_moda(numeros):
    """
    Calcula la moda de una lista de números.
    """
    frecuencia = {}

    for valor in numeros:
        if valor in frecuencia:
            frecuencia[valor] += 1
        else:
            frecuencia[valor] = 1

    modas = []

    valores_frecuencia = list(frecuencia.values())
    datos = list(frecuencia.keys())
    frecuencia_ordenada = sorted(valores_frecuencia)
    mayor_frecuencia = frecuencia_ordenada[-1]

    for i in range(len(valores_frecuencia)):
        if valores_frecuencia[i] == mayor_frecuencia:
            modas.append(datos[i])

    return modas

def calcular_rango(numeros):
    """
    Calcula el rango de una lista de números.
    """
    numeros_ordenados = sorted(numeros)
    minimo = numeros_ordenados[0]
    maximo = numeros_ordenados[-1]

    diferencia = maximo - minimo

    return diferencia

def calcular_varianza(numeros):
    """
    Calcula la varianza de una lista de números.
    """
    promedio_valor = calcular_promedio(numeros)
    cantidad = len(numeros)
    suma_desviaciones = 0
    for valor in numeros:
        desviacion = (valor - promedio_valor) ** 2
        suma_desviaciones += desviacion

    resultado_varianza = suma_desviaciones / cantidad

    return resultado_varianza

def calcular_desviacion_estandar(numeros):
    """
    Calcula la desviación estándar de una lista de números.
    """
    valor_varianza = calcular_varianza(numeros)
    resultado_desviacion = valor_varianza ** 0.5
    return resultado_desviacion

def calcular_rango_intercuartilico(numeros):
    """
    Calcula el rango intercuartílico de una lista de números.
    """
    if len(numeros) % 2 == 0:
        Q1_indice1 = len(numeros) // 4
        Q1_indice2 = Q1_indice1 - 1
        Q3_indice1 = (len(numeros) * 3) // 4
        Q3_indice2 = Q3_indice1 - 1
        Q1 = (float(numeros[Q1_indice1]) + float(numeros[Q1_indice2])) / 2
        Q3 = (float(numeros[Q3_indice1]) + float(numeros[Q3_indice2])) / 2

    else:
        Q1_indice = len(numeros) // 4
        Q3_indice = (len(numeros) * 3) // 4
        Q1 = float(numeros[Q1_indice])
        Q3 = float(numeros[Q3_indice])

    rango_intercuartil = Q3 - Q1
    return rango_intercuartil

def calcular_mad(numeros):
    """
    Calcula la desviación mediana absoluta (MAD) de una lista de números.
    """
    valor_mediana = obtener_mediana(numeros)
    desviaciones = []
    for valor in numeros:
        desviaciones.append(abs(valor - valor_mediana))
    mad = obtener_mediana(desviaciones)
    return mad

def calcular_covarianza(x, y):
    """
    Calcula la covarianza entre dos listas de números.
    """
    promedio_x = calcular_promedio(x)
    promedio_y = calcular_promedio(y)
    cantidad = len(x)
    suma_covarianza = 0
    for valor_x, valor_y in zip(x, y):
        suma_covarianza += (valor_x - promedio_x) * (valor_y - promedio_y)
    resultado_covarianza = suma_covarianza / cantidad
    return resultado_covarianza

def calcular_coeficiente_correlacion(x, y):
    """
    Calcula el coeficiente de correlación entre dos listas de números.
    """
    valor_covarianza = calcular_covarianza(x, y)
    varianza_x = calcular_varianza(x)
    varianza_y = calcular_varianza(y)
    resultado_correlacion = valor_covarianza / (varianza_x * varianza_y)
    return resultado_correlacion