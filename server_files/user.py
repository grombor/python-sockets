import json
from abc import ABC, abstractmethod
from typing import List

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


    def __init__(self, username: str, password: str, is_admin: bool = False, messages: List = List[any]):
        """ Init method. """
        self._username = username
        self._password = password
        self._is_admin = is_admin
        self.messages = messages


    def __str__(self) -> str:
        return f"username: {self._username}, password: {self._password}, is admin: {self._is_admin}, messages: {len(self.messages)}"

    def __repr__(self):
        return f"{self._username=}"


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

    def set_is_admin(self, is_admin: bool):
        """ Getter of is_admin  attribute. """
        self._is_admin = is_admin


    def get_messages(self):
        """ Returns a list with a user offline messages."""
        return self.messages


    def set_message(self, msg):
        """ Sets a new offline message for user if has less than 5 offline messages. """
        if len(self.messages) > 5:
            return None
        else:
            self.messages.append(msg)
            return "The message has been sent."


    def to_json(self):
        """ Returns user class in JSON format """
        json_object = {
            "username": self._username,
            "password": self._password,
            "is_admin": self._is_admin,
            "messages": self.messages
        }
        return json_object


    def show_offline_messages(self):
        """ Prints users offline messages in detail. """
        messages = self.get_messages()
        msg_text = f"You have {len(messages)} new messages."
        for msg in messages:
            msg_text += f"\n{messages.index(msg)}: {msg}"
        return msg_text
