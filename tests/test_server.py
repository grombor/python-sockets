import pytest

from server_files.server import Server


@pytest.fixture
def test_server_class():
    return Server


def test_server_has_start_server(test_server_class):
    assert hasattr(test_server_class, 'start')


def test_server_has_greetings(test_server_class):
    assert hasattr(test_server_class, 'greetings')


def test_server_has_send_message(test_server_class):
    assert hasattr(test_server_class, 'wrap')


def test_server_has_send_message_is_bytes(test_server_class):
    assert type(test_server_class().wrap('test')) == bytes


def test_server_has_get_commands(test_server_class):
    assert hasattr(test_server_class, 'get_commands')


def test_server_has_get_commands(test_server_class):
    assert test_server_class().get_commands() == Server()._commands.keys()


def test_server_handle_commands(test_server_class):
    assert hasattr(test_server_class, 'handle_commands')


def test_server_show_help(test_server_class):
    assert hasattr(test_server_class, 'show_help')

