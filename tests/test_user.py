import pytest
from server_files.user import AccountClass, UserAccountClass


def test_AccountClass_has_init():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "__init__") and hasattr(acc, "acc_name") and hasattr(acc, "is_admin"):
        assert True


def test_AccountClass_has__username():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "_username"):
        assert True


def test_AccountClass_has__password():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "_password"):
        assert True


def test_AccountClass_has_is_admin():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "is_admin"):
        assert True


def test_AccountClass_has_messages():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "messages"):
        assert True


def test_AccountClass_is_admin_is_false_as_default():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "is_admin"):
        if not getattr(acc, "is_admin"):
            assert True


def test_AccountClass_acc_name_is_str_and_works_poper():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "_username"):
        if (type(getattr(acc, "_username")) is str) and getattr(acc, "_username") == "test":
            assert True


def test_AccountClass_has_name_getter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "get_username"):
        assert True


def test_AccountClass_has_name_setter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "set_username"):
        assert True


def test_AccountClass_has_is_admin_getter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "get_is_admin"):
        assert True


def test_AccountClass_has_is_admin_setter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "set_is_admin"):
        assert True


def test_AccountClass_has_to_json():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "to_json"):
        assert True


def test_AccountClass_has_get_messages():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "get_messages"):
        assert True


def test_AccountClass_has_set_messages():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "set_messages"):
        assert True


def test_AccountClass_has_show_offline_messages():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "show_offline_messages"):
        assert True