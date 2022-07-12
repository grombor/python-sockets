import json
# import socket

from client_files.config import *


class Client:
    """
    Client class is responsible for the operation of the client.
    """


    def greetings(self):
        """ Shows greetings. """
        return print(f".:: Welcome to the {HOST} server! Type '-help' for info. ::.\n")


    def wrap(self, msg: str, data=''):
        msg = {
            "message": msg,
            "data": data
        }
        return json.dumps(msg).encode(CODING)


    def get_message(self):
        return str(input("send: "))


    def is_command(self, command):
        return command[:1] == "-"


    def login(self) -> str:
        login = input("Enter username: ")
        password = input("Enter password: ")
        msg = "-login"
        data = "@".join([login, password])
        return msg, data


    def new_user(self) -> str:
        login = input("Enter username: ")
        password = input("Enter password: ")
        is_admin = input("Admin account? [True/False]")
        msg = "-new_user"
        data = "@".join([login, password, is_admin])
        return msg, data


    def update_user(self):
        data = []
        data.append(input("Enter username: "))
        data.append(input("Enter a new username: "))
        data.append(input("Enter a new password: "))
        data.append(input("Admin account? [True/False]"))
        data = '@'.join(data)
        return "-update_user", data


