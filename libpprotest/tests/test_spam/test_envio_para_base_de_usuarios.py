from unittest.mock import Mock

import pytest

# from libpprotest.spam.enviador_de_email import Enviador
from libpprotest.spam.main import EnviadorDeSpam
from libpprotest.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='seumail@seudominio'),
            Usuario(nome='Luciano', email='seumail@seudominio')
        ],
        [
            Usuario(nome='Renzo', email='seumail@seudominio'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'seumail@seudominio',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Renzo', email='seumail@seudominio')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'seumail2@seudominio',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'seumail2@seudominio',
        'seumail@seudominio',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
