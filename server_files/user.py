import json
from abc import ABC, abstractmethod

users = []
logged_in_user = None

class AccountClass(ABC):
    """ Abstract account class interface. """

    @abstractmethod
    def __init__(self):
        """ Init method. """
        pass

    @abstractmethod
    def get_username(self):
        """ Getter of account name. """
        pass

    @abstractmethod
    def set_username(self):
        """ Setter of account name. """
        pass

    @abstractmethod
    def get_password(self):
        """ Setter of account name. """
        pass

    @abstractmethod
    def set_password(self):
        """ Setter of account name. """
        pass

    @abstractmethod
    def get_is_admin(self):
        """ Getter of is_admin  attribute. """
        pass

    @abstractmethod
    def to_json(self):
        """ Returns user class in JSON format """
        pass


class UserAccountClass(AccountClass):
    """ User account class. """

    messages = list()

    def __init__(self, username: str, password: str, is_admin: bool = False):
        """ Init method. """
        self._username = username
        self._password = password
        self._is_admin = is_admin


    def __str__(self) -> str:
        return f"username: {self._username}, password: {self._password}, is admin: {self._is_admin}"


    def get_username(self) -> str:
        """ Getter of account name. """
        return self._username


    def set_username(self, name) -> None:
        """ Setter of account name. """
        self._username = name


    def set_password(self, password):
        self._password = password


    def get_password(self):
        return self._password


    def get_is_admin(self):
        """ Getter of is_admin  attribute. """
        return self._is_admin

    def set_is_admin(self):
        """ Getter of is_admin  attribute. """
        return self._is_admin


    def to_json(self):
        """ Returns user class in JSON format """
        json_object = {
            "username": self._username,
            "password": self._password,
            "is_admin": bool(self._is_admin)
        }
        return json_object
