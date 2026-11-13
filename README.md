Equipo: 2
Propuesta: Predicción de la calidad del vino mediante aprendizaje automático 
Proyecto: Calidad de vino 
Algoritmo: Árbol de decisión  

Problema: El proyecto consiste en desarrollar una aplicación que permita predecir la calidad de un vino a partir de sus características fisicoquímicas, como la acidez, el pH, la densidad y el contenido de alcohol. El propósito es utilizar aprendizaje automático para realizar predicciones basadas en los datos. 

Datos: Se utilizará el conjunto de datos Wine Quality, que contiene muestras de vino con variables como acidez fija y volátil, azúcar residual, cloruros, densidad, pH, sulfatos y alcohol. Estos datos servirán para entrenar y probar el modelo. 

Algoritmo: Se implementará un árbol de decisión mediante Python y la biblioteca Scikitlearn. El algoritmo analizará las características de cada muestra para clasificar y predecir su calidad. 

Métrica objetivo: Se utilizará principalmente la exactitud (Accuracy) para medir el porcentaje de predicciones correctas, también se considerará el F1-score para evaluar el rendimiento del modelo. 

Recursos de cómputo: Se utilizará Python con las bibliotecas Pandas, NumPy y Scikitlearn. El entrenamiento se realizará mediante CPU con aproximadamente 2 a 4 GB de RAM, para el desarrollo se utilizará GitHub y para el despliegue de la aplicación se contempla Render y Docker. 

Riesgos iniciales: Los principales riesgos son el desbalance de las calificaciones en los datos, el sobreajuste del modelo, posibles errores en los registros y dificultades durante la integración o el despliegue en la nube. Para reducirlos, se limpiarán los datos y se realizarán pruebas de evaluación y funcionamiento. 

Objetivo: Desarrollar una aplicación web desplegada en la nube que permita predecir la calidad del vino mediante un modelo de aprendizaje automático basado en árboles de decisión. La aplicación utilizará datos relacionados con las características fisicoquímicas del vino para generar predicciones de manera rápida y fácil. También permitirá que los usuarios consulten los resultados desde cualquier dispositivo con acceso a internet. 