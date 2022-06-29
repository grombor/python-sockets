import pytest
from server_files.user import AccountClass, UserAccountClass


def test_AccountClass_has_init():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "__init__") and hasattr(acc, "acc_name") and hasattr(acc, "is_admin"):
        assert True
    else: assert False


def test_AccountClass_has_acc_name():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "acc_name"):
        assert True
    else: assert False


def test_AccountClass_has_acc_pass():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "acc_pass"):
        assert True
    else: assert False


def test_AccountClass_has_is_admin():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "is_admin"):
        assert True
    else:
        assert False


def test_AccountClass_is_admin_is_false_as_default():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "is_admin"):
        if not getattr(acc, "is_admin"):
            assert True
    else:
        assert False


def test_AccountClass_acc_name_is_str_and_works_poper():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "acc_name"):
        if (type(getattr(acc, "acc_name")) is str) and getattr(acc, "acc_name") == "test":
            assert True
    else:
        assert False


def test_AccountClass_has_name_getter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "get_acc_name"):
        assert True
    else: assert False


def test_AccountClass_has_name_setter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "set_acc_name"):
        assert True
    else: assert False


def test_AccountClass_has_is_admin_getter():
    acc = UserAccountClass("test", "test")
    if hasattr(acc, "get_is_admin"):
        assert True
    else: assert False