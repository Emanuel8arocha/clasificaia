"""ClasificaIA: API de clasificación de flores Iris con FastAPI (proyecto base).
Endpoints:
GET / página web con el formulario (app/index.html)
GET /health estado del servicio y versión del modelo
POST /predict recibe 4 medidas y devuelve la especie y la confianza
GET /docs documentación automática de FastAPI
El modelo se entrena antes con modelo/entrenar.py y se lee de app/modelo.joblib.
"""
import hmac
import os
from pathlib import Path
import joblib
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

# ---------------------------------------------------------------- Modelo
CARPETA = Path(__file__).parent
# Se carga UNA sola vez al iniciar el servidor (no en cada petición: sería lento).
ARTEFACTO = joblib.load(os.getenv("MODELO_PATH", CARPETA / "modelo.joblib"))

# ---------------------------------------------------------------- Seguridad (Hito 4)
# MOSTRAR_DOCS=0 en producción oculta /docs (menos información para un atacante).
MOSTRAR_DOCS = os.getenv("MOSTRAR_DOCS", "1") == "1"
# API_KEY: si se define (variable de entorno en Render, nunca en el código), /predict
# exige la cabecera x-api-key con ese valor. Vacía = API abierta (Hitos 1 a 3).
API_KEY = os.getenv("API_KEY", "")

app = FastAPI(
    title="ClasificaIA",
    version=ARTEFACTO.get("version", "1.0.0"),
    docs_url="/docs" if MOSTRAR_DOCS else None,
    redoc_url=None,
    openapi_url="/openapi.json" if MOSTRAR_DOCS else None,
)


def requiere_llave(x_api_key: str = Header(default="")):
    """Dependencia de FastAPI: 401 si falta la llave y 403 si es incorrecta."""
    if not API_KEY:
        return  # sin llave configurada: acceso libre
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Falta la cabecera x-api-key")
    if not hmac.compare_digest(x_api_key, API_KEY):  # comparación en tiempo constante
        raise HTTPException(status_code=403, detail="Llave inválida")


# ---------------------------------------------------------------- Entrada
class Vino(BaseModel):
    """Características fisicoquímicas de un vino.
    Field(ge=..., le=...): si el valor sale del rango, FastAPI responde 422
    sin llegar al modelo.
    >>> En su proyecto: aquí van las variables de entrada de SU modelo.
    """

    acidez_fija: float = Field(ge=3, le=20)             # g/dm³
    acidez_volatil: float = Field(ge=0, le=2.5)         # g/dm³
    acido_citrico: float = Field(ge=0, le=1.5)          # g/dm³
    azucar_residual: float = Field(ge=0, le=30)         # g/dm³
    cloruros: float = Field(ge=0, le=1)                 # g/dm³
    dioxido_azufre_libre: float = Field(ge=0, le=100)   # mg/dm³
    dioxido_azufre_total: float = Field(ge=0, le=400)   # mg/dm³
    densidad: float = Field(ge=0.98, le=1.01)           # g/cm³
    ph: float = Field(ge=2, le=5)
    sulfatos: float = Field(ge=0, le=3)                 # g/dm³
    alcohol: float = Field(ge=5, le=20)                 # % vol


# ---------------------------------------------------------------- Endpoints
@app.get("/health")
def salud():
    """Lo consultan Docker, Kubernetes y Render para saber si el servicio está vivo."""
    return {
        "status": "ok",
        "version": ARTEFACTO["version"],
        "exactitud": ARTEFACTO["exactitud"],
    }


@app.post("/predict", dependencies=[Depends(requiere_llave)])
def predecir(f: Vino):
    """Devuelve la clase más probable y su probabilidad (200), o 422 si los datos no

    son válidos.
    """
    # El modelo espera una lista de filas; aquí hay una sola fila con 11 columnas
    # en el MISMO orden que en el entrenamiento.
    x = [[
        f.acidez_fija, f.acidez_volatil, f.acido_citrico, f.azucar_residual,
        f.cloruros, f.dioxido_azufre_libre, f.dioxido_azufre_total,
        f.densidad, f.ph, f.sulfatos, f.alcohol,
    ]]
    probabilidades = ARTEFACTO["modelo"].predict_proba(x)[0]
    i = int(probabilidades.argmax())  # índice de la clase ganadora
    return {
        "clase": ARTEFACTO["clases"][i],
        "confianza": round(float(probabilidades[i]), 3),
    }


@app.get("/", response_class=HTMLResponse)
def inicio():
    """Sirve la página web; esta y la API comparten origen, así que no hay CORS."""
    return (CARPETA / "index.html").read_text(encoding="utf-8")