import pytest

from libpprotest.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'seumail@seudominio']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'nome@dominio',
        'Curso Python Pro',
        'Inscrições Abertas'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'teste']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'nome@dominio',
            'Curso Python Pro',
            'Inscrições Abertas'
        )
