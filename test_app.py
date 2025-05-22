import pytest
from app import app, mensagens

@pytest.fixture(autouse=True)
def limpar_mensagens():
    mensagens.clear()  # limpa antes de cada teste

@pytest.fixture
def cliente():
    with app.test_client() as client:
        yield client

def test_get_mensagens_vazio(cliente):
    resposta = cliente.get('/mensagens')
    assert resposta.status_code == 200
    assert resposta.get_json() == []

def test_post_mensagem_sucesso(cliente):
    dados = {'texto': 'Mensagem de teste'}
    resposta = cliente.post('/mensagens', json=dados)
    assert resposta.status_code == 201
    json = resposta.get_json()
    assert json['id'] == 1
    assert json['texto'] == 'Mensagem de teste'

def test_post_mensagem_sem_texto(cliente):
    resposta = cliente.post('/mensagens', json={})
    assert resposta.status_code == 400
    assert resposta.get_json()['erro'] == 'Campo "texto" é obrigatório'
