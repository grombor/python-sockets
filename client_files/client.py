import json
import socket

from client_files.config import *


class Client:
    """
    Client class is responsible for the operation of the client.
    """


    def greetings(self):
        """ Shows greetings. """
        return f".:: Welcome to the {HOST} server! Type '--help' for info. ::.\n"


    def wrap(self, msg: str, id='client', cmd=None, is_admin=False):
        msg = {
            "id": id,
            "message": msg,
            "is_admin": is_admin,
            "cmd": cmd
        }
        return json.dumps(msg).encode(CODING)


    def get_message(self):
        return str(input("send: "))

