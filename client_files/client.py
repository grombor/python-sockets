import json
import socket

from client_files.config import *


class Client:
    """
    Client class is responsible for the operation of the client.
    """


    def greetings(self):
        """ Shows greetings. """
        return print(f".:: Welcome to the {HOST} server! Type '-help' for info. ::.\n")


    def wrap(self, msg: str, data=None, id='client'):
        msg = {
            # "id": id,
            "message": msg,
            "data": data
        }
        return json.dumps(msg).encode(CODING)


    def get_message(self):
        return str(input("send: "))


    def is_command(self, command):
        return command[:1] == "-"


    def login(self) -> str:
        print("Login to server:")
        login = input("Enter username: ")
        password = input("Enter password: ")
        msg = "-login"
        data = "@".join([login, password])
        return msg, data


