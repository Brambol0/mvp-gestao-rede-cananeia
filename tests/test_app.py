
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_pagina_inicial_status_200(client):
    resposta = client.get("/")
    assert resposta.status_code == 200


def test_pagina_inicial_conteudo(client):
    resposta = client.get("/")
    assert b"Sistema de Gest" in resposta.data


def test_rota_inexistente_status_404(client):
    resposta = client.get("/pagina-inexistente")
    assert resposta.status_code == 404
