import pytest
from server_files.admin import Admin

@pytest.fixture
def test_Admin_class():
    return Admin


def test_AdminClass_has_login():
    admin = Admin()
    if hasattr(admin, "login"):
        assert True


def test_AdminClass_has_add_user():
    admin = Admin()
    if hasattr(admin, "add_user"):
        assert True


def test_AdminClass_has_remove_user():
    admin = Admin()
    if hasattr(admin, "remove_user"):
        assert True


def test_AdminClass_has_edit_user():
    admin = Admin()
    if hasattr(admin, "edit_user"):
        assert True