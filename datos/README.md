Propuesta

#  **Proyecto: Predicción de la calidad del vino**

Equipo 2

**Nombre del proyecto:** Calidad de vino

**Algoritmo:** Árbol de decisión

## **1. Planteamiento del problema**

El proyecto consiste en desarrollar una aplicación que permita predecir la calidad de un vino a partir de sus características fisicoquímicas, como la acidez, el pH, la densidad y el contenido de alcohol. El propósito es utilizar técnicas de aprendizaje automático para generar predicciones basadas en el análisis de los datos.

## **2. Datos**

Se utilizará el conjunto de datos **Wine Quality**, que contiene muestras de vino con diferentes variables fisicoquímicas, entre ellas:
- Acidez fija y volátil.
- Azúcar residual.
- Cloruros.
- Densidad.
- pH.
- Sulfatos.
- Contenido de alcohol.
Estos datos servirán para entrenar y probar el modelo de aprendizaje automático.

## **3. Algoritmo**

Se implementará un **árbol de decisión (Decision Tree)** mediante el lenguaje de programación Python y la biblioteca Scikit-learn.
Este algoritmo analizará las características de cada muestra de vino para identificar patrones en los datos y clasificar o predecir su calidad.

## **4. Métricas de evaluación**

Se utilizarán las siguientes métricas para evaluar el rendimiento del modelo:
- **Accuracy (Exactitud):** medirá el porcentaje de predicciones correctas realizadas por el modelo.
- **F1-score:** permitirá evaluar el equilibrio entre la precisión y la capacidad del modelo para identificar correctamente las diferentes categorías de calidad.

## **5. Recursos de cómputo y herramientas**

Para el desarrollo del proyecto se utilizarán los siguientes recursos:
- **Lenguaje:** Python.
- **Bibliotecas:** Pandas, NumPy y Scikit-learn.
- **Hardware:** CPU con aproximadamente 2 a 4 GB de RAM.
- **Control de versiones:** GitHub.
- **Despliegue:** Render.
- **Contenedores:** Docker.

El entrenamiento del modelo se realizará mediante CPU, ya que los requerimientos computacionales del conjunto de datos son relativamente bajos.

## **6. Riesgos iniciales**

Los principales riesgos identificados durante el desarrollo del proyecto son:
- **Desbalance de datos:** algunas calificaciones podrían tener más muestras que otras.
- **Sobreajuste:** el modelo podría aprender demasiado los datos de entrenamiento y presentar dificultades al realizar predicciones con datos nuevos.
- **Errores en los registros:** podrían existir valores incorrectos o inconsistentes en el conjunto de datos.
- **Dificultades de integración y despliegue:** podrían presentarse problemas al conectar el modelo con la aplicación web o al publicarla en la nube.
**Medidas de prevención:** se realizará una limpieza de datos, se aplicarán pruebas de evaluación y se verificará el funcionamiento de la aplicación antes de su despliegue.

## **7. Objetivo general**

Desarrollar una aplicación web desplegada en la nube que permita predecir la calidad del vino mediante un modelo de aprendizaje automático basado en árboles de decisión.
La aplicación utilizará datos relacionados con las características fisicoquímicas del vino para generar predicciones de manera rápida y sencilla. Además, permitirá que los usuarios consulten los resultados desde cualquier dispositivo con acceso a internet.

## **Distribución de tareas**

- **Integrante A:** se encargará de recopilar los datos y construir el árbol de decisión para predecir la calidad del vino.
- **Integrante B:** estará a cargo de adaptar la aplicación web para ingresar las características del vino y mostrar los resultados.
- **Integrante C:** se encargará de comprobar que el sistema funcione correctamente y colaborar en su configuración y despliegue.