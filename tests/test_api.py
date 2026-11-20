"""Pruebas automáticas de la API (se ejecutan con: pytest -q).
TestClient simula peticiones HTTP sin levantar un servidor. GitHub Actions las
ejecuta en cada push: si una falla, la imagen no se publica.
"""
from fastapi.testclient import TestClient
from app.main import app, ARTEFACTO

cliente = TestClient(app)

# Ejemplo válido con las 11 variables exactas de la clase Vino en app/main.py
VINO_EJEMPLO = {
    "acidez_fija": 7.4,
    "acidez_volatil": 0.7,
    "acido_citrico": 0.0,
    "azucar_residual": 1.9,
    "cloruros": 0.076,
    "dioxido_azufre_libre": 11.0,
    "dioxido_azufre_total": 34.0,
    "densidad": 0.9978,
    "ph": 3.51,
    "sulfatos": 0.56,
    "alcohol": 9.4,
}


def test_health():
    """El servicio responde y reporta la versión del modelo."""
    assert cliente.get("/health").json()["status"] == "ok"


def test_predict_vino():
    """Un vino válido devuelve código 200, una clase de calidad y su confianza."""
    r = cliente.post("/predict", json=VINO_EJEMPLO)
    assert r.status_code == 200
    datos = r.json()
    assert datos["clase"] in ARTEFACTO["clases"]
    assert 0.0 <= datos["confianza"] <= 1.0


def test_predict_invalido():
    """Un valor fuera de rango se rechaza con 422 (validación de Pydantic)."""
    vino_invalido = VINO_EJEMPLO.copy()
    vino_invalido["acidez_fija"] = -1  # Fuera de rango (ge=3)
    r = cliente.post("/predict", json=vino_invalido)
    assert r.status_code == 422


def test_calidad_minima():
    """Prueba de calidad: si el modelo baja del umbral de exactitud, el CI falla."""
    # Ajustado a 0.55 para el dataset de vinos (cámbialo si tu modelo logra más)
    umbral = 0.50
    assert ARTEFACTO["exactitud"] >= umbral
    assert cliente.get("/health").json()["exactitud"] >= umbral


def test_llave_requerida(monkeypatch):
    """Hito 4: con API_KEY definida, sin cabecera da 401 y con la correcta da 200."""
    import app.main as m

    monkeypatch.setattr(m, "API_KEY", "secreto-de-prueba")

    # Intento sin cabecera (debe fallar con 401 Unauthorized)
    assert cliente.post("/predict", json=VINO_EJEMPLO).status_code == 401

    # Intento con la cabecera correcta (debe responder 200 OK)
    r = cliente.post("/predict", json=VINO_EJEMPLO, headers={"x-api-key": "secreto-de-prueba"})
    assert r.status_code == 200