import pytest

from server_files.server import Server
from server_files.user import UserAccountClass


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


def test_server_has_show_version(test_server_class):
    assert hasattr(test_server_class, 'show_version')


def test_server_show_version(test_server_class):
    assert type(test_server_class().show_version()) == bytes


def test_server_has_stop(test_server_class):
    assert hasattr(test_server_class, 'stop')


def test_server_has_show_uptime(test_server_class):
    assert hasattr(test_server_class, 'show_uptime')


def test_server_has_login(test_server_class):
    assert hasattr(test_server_class, 'login')


def test_server_has_create_user(test_server_class):
    assert hasattr(test_server_class, 'create_user')


def test_server_has_add_user(test_server_class):
    assert hasattr(test_server_class, 'add_user')


def test_server_has_read_from_file(test_server_class):
    assert hasattr(test_server_class, 'read_from_file')


def test_server_has_save_to_file(test_server_class):
    assert hasattr(test_server_class, 'save_to_file')


def test_server_has_new_user(test_server_class):
    assert hasattr(test_server_class, 'new_user')


def test_server_has_new_user(test_server_class):
    assert hasattr(test_server_class, 'send_msg_to_user')


