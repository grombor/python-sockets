import pytest
from client_files.client import Client


@pytest.fixture
def test_client_class():
    return Client


def test_client_class_has_connect(test_client_class):
    assert hasattr(test_client_class, 'greetings')


def test_client_class_has_send(test_client_class):
    assert hasattr(test_client_class, 'wrap')


def test_client_send_message_is_byte(test_client_class):
    assert type(test_client_class().wrap("test")) == bytes


def test_client_class_get_message(test_client_class):
    assert hasattr(test_client_class, 'get_message')


def test_client_class_is_command(test_client_class):
    assert hasattr(test_client_class, 'is_command')


def test_client_class_login(test_client_class):
    assert hasattr(test_client_class, 'login')


def test_client_class_login(test_client_class):
    assert hasattr(test_client_class, 'new_user')


def test_client_class_login(test_client_class):
    assert hasattr(test_client_class, 'update_user')




