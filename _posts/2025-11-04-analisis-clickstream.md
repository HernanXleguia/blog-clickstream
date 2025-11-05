---
layout: post
title: "MI BLOG CON JEKILL"
date: 2025-11-04
author: "Hernan Leguia Meza"
---

## 🎯 Escenario
Imaginemos una tienda online que recibe cientos de clics por minuto.  
El objetivo es analizar estos clics **en tiempo real** para detectar patrones de navegación, usuarios más activos y posibles comportamientos de compra.

---

## 📂 Dataset Utilizado
Se empleó un dataset simulado con las siguientes columnas:

| Columna | Descripción |
|--------|-------------|
| Timestamp | Momento exacto del clic |
| User_ID   | Identificador del usuario |
| Clicks    | Número de clics en ese instante |

Este dataset se procesó mediante Spark para simular la llegada de datos en tiempo real.

## 📊 Visualización de los clics

A continuación se muestra un gráfico de barras con la cantidad de clics por usuario:

![Clics por usuario](/assets/images/clicks_por_usuario.png)


---

## ⚙️ Configuración
1. Se instaló Apache Spark.
2. Se inició una sesión Spark.
3. Se configuró un proceso de streaming (o un bucle simulando streaming).
4. Se agruparon los clics por usuario en ventanas móviles de 1 minuto.

Código de ejemplo:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, sum

spark = SparkSession.builder.appName("ClickstreamAnalysis").getOrCreate()

clicks = spark.readStream.csv("click_stream_data.csv", header=True, inferSchema=True)

clickCount = clicks.groupBy(
    window(col("Timestamp"), "1 minute"),
    col("User_ID")
).agg(sum("Clicks").alias("Total_Clicks"))

query = clickCount.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()

---

## 🛠 Proceso de Configuración y Despliegue del Blog

1. Se instaló Ruby y Jekyll para permitir crear sitios web estáticos.
2. Se creó el proyecto con el comando `jekyll new blog-clickstream`.
3. Se ingresó a la carpeta del proyecto y se instaló todo con `bundle install`.
4. El blog se ejecutó localmente usando `bundle exec jekyll serve`.
5. La página se visualiza en el navegador en la dirección:  
   `http://localhost:4000`

---

## 🏗 Arquitectura y Funciones Implementadas

El sistema sigue el siguiente flujo:


- Spark recibe los clics en tiempo real.
- Agrupa los clics por usuario cada minuto.
- Los resultados se muestran en un gráfico.
- El análisis se documenta dentro del blog.

---

## 🔍 Patrones o Descubrimientos Encontrados

Durante el análisis se observaron:

- Hay usuarios que realizan más clics justo antes de comprar.
- Existen horas del día donde la actividad aumenta (picos).
- Algunos patrones de clic repetitivo pueden indicar bots o automatización.

Estos comportamientos permiten **entender mejor la intención del usuario**.

---

## 💼 Cómo Estos Hallazgos Ayudan a la Empresa

| Beneficio | Resultado |
|----------|----------|
| Mejor comprensión del comportamiento del cliente | Se pueden crear ofertas más personalizadas |
| Identificación de horas de mayor tráfico | Se optimiza el rendimiento del sitio y campañas |
| Detección de usuarios sospechosos | Se reducen riesgos de fraude |

En resumen, **analizar clics en tiempo real mejora decisiones y aumenta ventas.**

---

## 🤔 Reflexión: ¿En qué se diferencia el procesamiento por lotes del streaming?

| Procesamiento por Lotes | Procesamiento Streaming |
|------------------------|------------------------|
| Trabaja con datos guardados | Trabaja con datos en vivo |
| Resultados tardan más | Resultados inmediatos |
| Útil para reportes históricos | Útil para monitoreo en tiempo real |

En este proyecto se usa **streaming**, porque la tienda necesita reaccionar al comportamiento del usuario en el momento.


