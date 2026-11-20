"""Entrena el modelo de ClasificaIA y lo guarda en un archivo.

Calidad de vino (Equipo 2): predice la calidad de un vino a partir de sus
características fisicoquímicas con un árbol de decisión (Scikit-learn).

Uso: python modelo/entrenar.py [archivo_salida]
"""
import sys
from datetime import datetime, timezone

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ---------------------------------------------------------------- Configuración
# Archivo donde se guarda el modelo; la API lo lee al iniciar.
SALIDA = sys.argv[1] if len(sys.argv) > 1 else "app/modelo.joblib"
SEMILLA = 42  # misma semilla = mismo resultado (reproducible)
DATOS_CSV = "datos/winequality-red.csv"

# ---------------------------------------------------------------- 1. Datos
# Wine Quality: muestras de vino con 11 medidas fisicoquímicas y una
# calificación de calidad (enteros, aprox. de 3 a 8).
# >>> En su proyecto: aquí cargan SUS datos (CSV, dataset de scikit-learn, etc.).
df = pd.read_csv(DATOS_CSV, sep=";")
df = df.drop_duplicates().dropna()  # limpieza: quita repetidos y vacíos
X = df.drop(columns=["quality"])
y = df["quality"].values
CARACTERISTICAS = list(X.columns)
NOMBRES_CLASES = [str(c) for c in sorted(set(y))]  # ["3", "4", "5", ...]
UNIDADES = {
    "fixed acidity": "g/dm³",
    "volatile acidity": "g/dm³",
    "citric acid": "g/dm³",
    "residual sugar": "g/dm³",
    "chlorides": "g/dm³",
    "free sulfur dioxide": "mg/dm³",
    "total sulfur dioxide": "mg/dm³",
    "density": "g/cm³",
    "pH": "adimensional",
    "sulphates": "g/dm³",
    "alcohol": "% vol",
}

# 70 % para entrenar y 30 % para evaluar. stratify mantiene la proporción de
# cada clase en ambos conjuntos; el modelo nunca ve los datos de prueba.
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.3, random_state=SEMILLA, stratify=y)

# ---------------------------------------------------------------- 2. Modelo
# Árbol de decisión. No necesita escalar las medidas (decide por umbrales).
# max_depth limita la profundidad para reducir el sobreajuste.
# >>> En su proyecto: cambian el algoritmo por el suyo.
modelo = DecisionTreeClassifier(max_depth=5, random_state=SEMILLA)
modelo.fit(X_tr, y_tr)

# ---------------------------------------------------------------- 3. Evaluación
predicciones = modelo.predict(X_te)
exactitud = accuracy_score(y_te, predicciones)  # proporción de aciertos
f1 = f1_score(y_te, predicciones, average="weighted", zero_division=0)
print(classification_report(
    y_te, predicciones, target_names=NOMBRES_CLASES, zero_division=0))

# ---------------------------------------------------------------- 4. Guardar
# Se guarda un diccionario: el modelo y los datos que la API necesita mostrar.
joblib.dump({
    "modelo": modelo,
    "clases": NOMBRES_CLASES,
    "caracteristicas": CARACTERISTICAS,
    "unidades": UNIDADES,
    "exactitud": round(float(exactitud), 4),
    "f1": round(float(f1), 4),
    "version": datetime.now(timezone.utc).strftime("%Y%m%d-%H%M"),
}, SALIDA)
print(f"exactitud={exactitud:.3f} f1={f1:.3f} guardado en {SALIDA}")